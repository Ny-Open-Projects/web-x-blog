#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
queue.py — 面试卡批量生产的队列与断点续跑管理器（模型无关）

任何 agent 都能接手：只需读 RUNBOOK.md，然后 `python3 queue.py next` 取任务，
做完 `python3 queue.py done <task_id>` 落盘。状态存在 state.json，天然断点续跑。

设计要点（针对 429 与中断）：
  1. 幂等：同一 task 重复 done 不会产生重复卡片
  2. 限流：一个 wave 最多 3 个并行 agent，每个 agent 最多 N 篇
  3. 冷却：wave 之间强制 sleep，避免连续打 API 触发 429
  4. 断点：任何时刻 Ctrl-C，已 done 的全部保留
  5. 退避：连续失败自动降速（指数退避），成功则恢复

用法：
  python3 queue.py init                # 初始化（扫描源文件、建 state）
  python3 queue.py next --wave 3       # 取一个 wave 的任务（默认 3 并行）
  python3 queue.py done <task_id> [--cards 3]   # 标记完成
  python3 queue.py fail <task_id> [--reason "429"]  # 标记失败（触发退避）
  python3 queue.py status              # 进度总览
  python3 queue.py reset --task <id>   # 把某任务放回队列重做
  python3 queue.py doctor              # 自检
"""

import argparse
import json
import os
import random
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# 项目根目录：默认取本脚本的上级目录，也可用环境变量覆盖
# （技能自带副本放在 ~/.workbuddy/skills/mt-to-interview-cards/_pipeline/，
#   对任意项目跑时用 MT_ROOT=<项目根> 指定即可）
ROOT = Path(os.environ.get("MT_ROOT", Path(__file__).resolve().parent.parent)).resolve()
SOURCE = ROOT / "source"
TARGET = ROOT / "target"
PIPE = Path(os.environ.get("MT_PIPE", Path(__file__).resolve().parent))
LOGS = Path(os.environ.get("MT_LOGS", ROOT / "_logs"))
STATE = Path(os.environ.get("MT_STATE", PIPE / "state.json"))
METRICS = PIPE / "metrics.jsonl"

# 只处理技术章；01/02(部分)/03/20/21 为软技能或元内容，已在 TRIAGE.md 判定
TECH_CHAPTERS = [f"{i:02d}" for i in range(4, 20)]
TECH_CHAPTERS += ["02"]  # 02 只有 2-1、2-2 是技术，其余已在台账剔除

# 频率控制（关键参数）
MAX_PARALLEL = 1          # 并行 agent 上限 —— 2026-10-03 实测：3 并行触发 429 额度耗尽，降为串行
MAX_FILES_PER_AGENT = 2   # 每个 agent 一轮最多处理几篇（串行下再收窄）
COOLDOWN_SEC = 180        # wave 之间的冷却秒数（翻倍，配合串行）
BACKOFF_BASE = 45         # 失败退避基数秒（指数增长）
MAX_BACKOFF = 900         # 退避上限 15 分钟


def now():
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def log(msg):
    print(f"[{now()}] {msg}", flush=True)


# ---------- 体量分层（决定出卡节奏与深挖门槛） ----------
def size_tier(nbytes):
    if nbytes < 3000:
        return "S", "L1~L2", 1, False   # (档位, 深度上限, 建议卡数, 是否出深挖)
    if nbytes < 6000:
        return "M", "L2", 2, False
    if nbytes < 12000:
        return "L", "L2~L3", 3, True
    return "XL", "L3~L4", 5, True


# ---------- 状态 ----------
def load_state():
    if STATE.exists():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"version": 1, "created": now(), "tasks": {}, "next_num": 1, "waves": 0}


def save_state(st):
    st["updated"] = now()
    tmp = STATE.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(st, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(STATE)   # 原子替换，避免半截文件


def metric(**kw):
    kw["ts"] = now()
    with METRICS.open("a", encoding="utf-8") as f:
        f.write(json.dumps(kw, ensure_ascii=False) + "\n")


# ---------- init ----------
def is_tech_source(path: Path):
    """TRIAGE 判定：只有 02-1 / 02-2 是技术"""
    rel = path.relative_to(SOURCE)
    ch = rel.parts[0]
    if ch not in TECH_CHAPTERS:
        return False
    if ch == "02":
        return rel.name.startswith("2-1 ") or rel.name.startswith("2-2 ")
    return True


def cmd_init(args):
    st = load_state()
    tasks = st["tasks"]
    added = 0
    seen_title = {}      # 章号+序号 -> 已收录的规范标题（用于识别重复录制）
    dups = []
    for ch in sorted(TECH_CHAPTERS):
        d = SOURCE / ch
        if not d.is_dir():
            continue
        for p in sorted(d.glob("*.txt")):
            if not is_tech_source(p):
                continue
            rel = str(p.relative_to(ROOT))
            if rel in tasks:
                continue
            # 解析 "04-11 xxx-讯捷*.txt" → key="04-11", title="xxx"
            m = re.match(r"^(\d+)-(\d+)\s*(.*)$", p.stem)
            if m:
                key = f"{m.group(1)}-{m.group(2)}"
                title = re.sub(r"-迅捷文字转语音-.*$", "", m.group(3)).strip()
            else:
                key, title = f"{ch}-{p.stem[:6]}", p.stem

            # 同一 章-序号+标题 出现多次 = ASR 分段重复录制，只收第一份
            tkey = (ch, key, title)
            if tkey in seen_title:
                dups.append((rel, seen_title[tkey]))
                continue
            seen_title[tkey] = rel

            nbytes = p.stat().st_size
            tier, depth, ncards, deep = size_tier(nbytes)
            tasks[rel] = {
                # ID 全局唯一：章号 + 序号（章内唯一即为全局唯一，章号已在 key 内）
                "id": key,
                "chapter": ch,
                "source": rel,
                "title": title,
                "bytes": nbytes,
                "tier": tier,
                "depth_cap": depth,
                "suggest_cards": ncards,
                "allow_deep": deep,
                "status": "pending",
                "attempts": 0,
                "last_error": None,
                "cards": [],
            }
            added += 1
    save_state(st)
    log(f"init 完成：新增任务 {added}，去重跳过 {len(dups)}，任务总数 {len(tasks)}")
    for rel, keep in dups:
        log(f"  ↳ 重复录制已跳过：{rel}")
        log(f"     保留：{keep}")
    return 0


# ---------- next ----------
def cmd_next(args):
    st = load_state()
    pend = [t for t in st["tasks"].values() if t["status"] == "pending"]
    if not pend:
        log("队列为空——全部完成或已剔除。")
        return 0

    # 退避：检查最近失败时间
    last_fail = st.get("last_fail_ts")
    if last_fail:
        gap = time.time() - datetime.fromisoformat(last_fail).timestamp()
        need = min(BACKOFF_BASE * (2 ** st.get("consec_fail", 1)), MAX_BACKOFF)
        if gap < need:
            wait = int(need - gap)
            log(f"退避中：还需等待 {wait}s（连续失败 {st.get('consec_fail',1)} 次）")
            if not args.force:
                return 2

    # 分波：每 agent 最多 MAX_FILES_PER_AGENT 篇
    per = args.per_agent or MAX_FILES_PER_AGENT
    parallel = min(args.wave or MAX_PARALLEL, MAX_PARALLEL)
    budget = per * parallel

    # 排序：先厚后薄（厚文件信息量大，先验证难度），同厚按章聚拢
    pend.sort(key=lambda t: (-t["bytes"], t["chapter"]))
    batch = pend[:budget]
    waves = [batch[i:i + per] for i in range(0, len(batch), per)]

    st["waves"] = st.get("waves", 0) + 1
    st["consec_fail"] = 0
    st.pop("last_fail_ts", None)
    for t in batch:
        t["status"] = "running"
        t["attempts"] = (t.get("attempts") or 0) + 1
    save_state(st)

    log(f"wave {st['waves']}：派出 {len(batch)} 篇（{len(waves)} 个 agent，每 agent ≤{per} 篇）")
    for i, w in enumerate(waves, 1):
        log(f"  ── agent {i} ──")
        for t in w:
            log(f"     [{t['tier']:>2}|{t['depth_cap']:>6}|{t['bytes']:>6}B|"
                f"卡{t['suggest_cards']} 张{'+深挖' if t['allow_deep'] else '    '}] {t['source']}")
    metric(event="wave", wave=st["waves"], files=len(batch), agents=len(waves))
    return 0


def find_task(st, key):
    """按多种写法查找任务，避免 worker 因写法不对而卡住。

    2026-10-03 worker 报的真实陷阱：`state.json` 的 **dict key 是 source 路径**，
    但 `done` / `fail` 比对的是 **`id` 字段**（形如 `11-4`，不补零）。
    传 source 路径会报「任务不存在」→ 任务僵在 running。

    现支持三种写法（任一命中即可）：
      ① `11-4`      —— id 字段（推荐）
      ② `source/11/11-4 xxx.txt` —— state 的 key
      ③ 末段含 `11-4` 的任意字符串（模糊兜底，唯一命中才认）
    """
    tasks = st["tasks"].values()
    # ① 精确 id
    m = [t for t in tasks if t["id"] == key]
    if m:
        return m[0]
    # ② 精确 source（key 或 source 字段）
    m = [t for t in tasks if t.get("source") == key or key.endswith(t.get("source", ""))]
    if m:
        return m[0]
    # ③ 模糊：只认唯一命中
    cand = [t for t in tasks if t["id"] and t["id"] in key]
    if len(cand) == 1:
        return cand[0]
    if len(cand) > 1:
        log(f"「{key}」模糊匹配到多个任务：{[t['id'] for t in cand]}，请写明确的 id")
    return None


# ---------- done / fail ----------
def cmd_done(args):
    st = load_state()
    t = find_task(st, args.task_id)
    if t is None:
        log(f"任务不存在：{args.task_id}")
        log(f"  提示：正确写法是任务 id（如 8-14 / 11-4），不是 source 路径")
        return 1
    t["status"] = "done"
    t["cards"] = args.cards.split(",") if args.cards else []
    t["done_at"] = now()
    t["last_error"] = None
    save_state(st)
    metric(event="done", task=t["id"], cards=len(t["cards"]), attempts=t["attempts"])
    done_n = sum(1 for x in st["tasks"].values() if x["status"] == "done")
    log(f"完成 {t['id']}（{t['source']}），产出 {len(t['cards'])} 张卡。本批累计 {done_n} 篇。")
    return 0


def cmd_fail(args):
    st = load_state()
    t = find_task(st, args.task_id)
    if t is None:
        log(f"任务不存在：{args.task_id}")
        log(f"  提示：正确写法是任务 id（如 8-14 / 11-4），不是 source 路径")
        return 1
    t["status"] = "pending"          # 放回队列
    t["last_error"] = args.reason
    st["consec_fail"] = st.get("consec_fail", 0) + 1
    st["last_fail_ts"] = now()
    need = min(BACKOFF_BASE * (2 ** st["consec_fail"]), MAX_BACKOFF)
    save_state(st)
    metric(event="fail", task=t["id"], reason=args.reason, consec=st["consec_fail"])
    log(f"失败 {t['id']}：{args.reason} → 放回队列，连续失败 {st['consec_fail']} 次，"
        f"下次取任务需等待 {need}s（用 --force 可跳过）")
    return 0


def cmd_status(args):
    st = load_state()
    tasks = list(st["tasks"].values())
    total = len(tasks)
    done = sum(1 for t in tasks if t["status"] == "done")
    pend = sum(1 for t in tasks if t["status"] == "pending")
    run = sum(1 for t in tasks if t["status"] == "running")
    cards = sum(len(t.get("cards") or []) for t in tasks)

    by_tier = {}
    for t in tasks:
        b = by_tier.setdefault(t["tier"], {"n": 0, "done": 0})
        b["n"] += 1
        if t["status"] == "done":
            b["done"] += 1

    print(f"\n{'='*54}")
    print(f"  面试卡批量生产 · 进度总览")
    print(f"{'='*54}")
    print(f"  任务总数   {total}")
    print(f"  已完成     {done}  ({done*100//max(total,1)}%)")
    print(f"  进行中     {run}")
    print(f"  待处理     {pend}")
    print(f"  已产卡片   {cards} 张")
    print(f"  已跑 wave  {st.get('waves',0)}")
    if st.get("consec_fail"):
        print(f"  ⚠ 连续失败 {st['consec_fail']} 次，最近原因：{st.get('last_fail_ts')}")
    print(f"\n  按体量分档：")
    for k in ("XL", "L", "M", "S"):
        if k in by_tier:
            b = by_tier[k]
            bar = "█" * int(b["done"] * 20 / max(b["n"], 1))
            print(f"    {k:>2} ({b['n']:>3} 篇) {bar} {b['done']}/{b['n']}")
    print(f"\n  实际落盘卡片：{len(list(TARGET.rglob('*.md'))) if TARGET.exists() else 0} 个 .md")
    print(f"{'='*54}\n")
    return 0


def cmd_reset(args):
    st = load_state()
    for t in st["tasks"].values():
        if t["id"] == args.task:
            t["status"] = "pending"
            t["last_error"] = None
            log(f"{t['id']} 已放回队列")
    save_state(st)
    return 0


def cmd_doctor(args):
    ok = True
    log(f"项目根目录：{ROOT}")
    log(f"脚本目录：  {PIPE}")
    for p in (PIPE, LOGS):
        if not p.exists():
            log(f"✗ 缺目录 {p}"); ok = False
    if not SOURCE.is_dir():
        log(f"✗ 缺源目录 {SOURCE}")
        log("  → 若这是技能自带副本，请设 MT_ROOT=<项目根目录>（该目录须含 source/ 与 target/）")
        return 1
    for ch in TECH_CHAPTERS:
        if not (SOURCE / ch).is_dir():
            log(f"⚠ 缺源目录 source/{ch}（该章不存在，跳过）")
    if not STATE.exists():
        log("✗ state.json 不存在，请先 `python3 queue.py init`")
        return 1
    st = load_state()
    ids = [t["id"] for t in st["tasks"].values()]
    dup = len(ids) != len(set(ids))
    log(f"✓ state.json 可读，任务 {len(st['tasks'])} 个")
    log(f"{'✗' if dup else '✓'} 任务 ID 唯一：{'否（重复！）' if dup else '是'}")
    log(f"✓ 目标目录 {TARGET} {'存在' if TARGET.exists() else '不存在（首次 init 时会自动创建）'}")
    return 1 if dup else (0 if ok else 1)


def main():
    ap = argparse.ArgumentParser(description="面试卡批量生产队列管理器")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init").set_defaults(func=cmd_init)
    sub.add_parser("status").set_defaults(func=cmd_status)
    sub.add_parser("doctor").set_defaults(func=cmd_doctor)

    p = sub.add_parser("next"); p.add_argument("--wave", type=int, default=MAX_PARALLEL)
    p.add_argument("--per-agent", type=int, default=MAX_FILES_PER_AGENT)
    p.add_argument("--force", action="store_true"); p.set_defaults(func=cmd_next)

    p = sub.add_parser("done"); p.add_argument("task_id")
    p.add_argument("--cards", default=""); p.set_defaults(func=cmd_done)

    p = sub.add_parser("fail"); p.add_argument("task_id")
    p.add_argument("--reason", default="unknown"); p.set_defaults(func=cmd_fail)

    p = sub.add_parser("reset"); p.add_argument("--task", required=True)
    p.set_defaults(func=cmd_reset)

    args = ap.parse_args()
    sys.exit(args.func(args) or 0)


if __name__ == "__main__":
    main()
