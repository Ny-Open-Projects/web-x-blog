#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
watchdog.py — 额度耗尽自愈守护

背景：2026-10-03 凌晨 4 个 worker 同时 `429 额度已用尽` 全部失败。
本脚本把这类中断变成**可观测、可恢复**的状态，而不是"跑着跑着全没了"。

它做三件事（每轮间隔 120 秒）：
  1. 检查 WorkBuddy 会话日志里近期的 429 / 额度错误
  2. 命中则：把僵死 running 任务解冻回 pending、写 SNAPSHOT.json、拉黑标记
  3. 每 10 轮刷新一次 SNAPSHOT.json（无论是否出错）

用法：
  python3 watchdog.py            # 前台跑（Ctrl-C 退出）
  python3 watchdog.py --once     # 只检查一次
  python3 watchdog.py --status   # 看守护状态
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(os.environ.get("MT_ROOT", Path(__file__).resolve().parent.parent)).resolve()
PIPE = Path(os.environ.get("MT_PIPE", Path(__file__).resolve().parent))
LOGS = Path(os.environ.get("MT_LOGS", ROOT / "_logs"))
STATE = Path(os.environ.get("MT_STATE", PIPE / "state.json"))
SNAPSHOT = PIPE / "SNAPSHOT.json"
PAUSE_FLAG = PIPE / ".paused"          # 存在 = 额度耗尽，已暂停
QUOTA_HINT = PIPE / "QUOTA.md"

INTERVAL = 120          # 轮询间隔秒
SNAPSHOT_EVERY = 10     # 每 N 轮刷一次快照

# 429 / 额度相关的日志特征
PATTERNS = [
    re.compile(r"429\s*额度已用尽"),
    re.compile(r"额度已用尽"),
    re.compile(r"rate.?limit", re.I),
    re.compile(r"too many requests", re.I),
]
# 明确不算额度问题的（速率超限 ≠ 总额度耗尽，要区分）
RATE_ONLY = re.compile(r"(too many requests|rate.?limit)", re.I)


def now():
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def log(msg):
    line = f"[{now()}] {msg}"
    print(line, flush=True)
    try:
        LOGS.mkdir(parents=True, exist_ok=True)
        with (LOGS / "watchdog.log").open("a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception:
        pass


# 只看「本次运行开始之后」的新增内容。
# 教训：2026-10-03 凌晨的 429 记录会一直在旧日志里，
#   若按「近 3 小时」扫，一启动就误报 431 条 —— 必须记住起点位置。
_SINCE = None            # (path, size) 已读到的偏移量
_START_TS = time.time()


def recent_agent_logs(hours=6):
    """找近期的会话日志文件（WorkBuddy 按日期分目录）"""
    base = Path.home() / ".workbuddy" / "logs"
    if not base.is_dir():
        return []
    cutoff = time.time() - hours * 3600
    out = []
    for p in base.rglob("*.log"):
        try:
            if p.stat().st_mtime > cutoff:
                out.append(p)
        except Exception:
            continue
    return out[-30:]      # 最多看最近 30 个，避免扫太多


def mark_baseline():
    """记录当前所有日志的读取位置，作为「本次运行起点」"""
    global _SINCE
    _SINCE = {}
    for p in recent_agent_logs():
        try:
            _SINCE[str(p)] = p.stat().st_size
        except Exception:
            pass
    log(f"已记录 {len(_SINCE)} 个日志的基线偏移（此前内容不再计入）")


def new_text(p):
    """只返回该文件自基线之后新增的内容。
    基线缺失时（如 --once 模式）先补记基线再返回空，避免把旧日志当新增。"""
    global _SINCE
    if _SINCE is None:
        mark_baseline()
        return ""
    try:
        size = p.stat().st_size
    except Exception:
        return ""
    off = _SINCE.get(str(p), 0)
    if size <= off:
        return ""
    try:
        with p.open("r", encoding="utf-8", errors="ignore") as f:
            f.seek(off)
            txt = f.read()
    except Exception:
        return ""
    _SINCE[str(p)] = size
    return txt


def scan_429():
    """扫描近期日志里的 429 / 额度错误，返回命中列表"""
    hits, quota_exhausted = [], False
    for p in recent_agent_logs():
        txt = new_text(p)          # 只看新增
        if not txt:
            continue
        for pat in PATTERNS:
            for m in pat.finditer(txt):
                # 区分「总额度耗尽」与「速率超限」
                ctx = txt[max(0, m.start() - 80):m.end() + 80]
                is_quota = bool(re.search(r"额度已用尽|quota|加量包", ctx, re.I))
                hits.append((p.name, m.group(0), ctx.replace("\n", " ")[:150]))
                if is_quota or not RATE_ONLY.search(m.group(0)):
                    quota_exhausted = True
    return hits, quota_exhausted


def unfreeze():
    """把僵死的 running 任务解冻回 pending"""
    if not STATE.exists():
        return 0
    try:
        st = json.loads(STATE.read_text(encoding="utf-8"))
    except Exception:
        return 0
    n = 0
    for t in st["tasks"].values():
        if t["status"] == "running":
            t["status"] = "pending"
            t["last_error"] = "watchdog-额度耗尽中断，已解冻"
            n += 1
    if n:
        st["consec_fail"] = 0
        st.pop("last_fail_ts", None)
        tmp = STATE.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(st, ensure_ascii=False, indent=2), encoding="utf-8")
        tmp.replace(STATE)
    return n


def write_snapshot(note=""):
    import glob
    if not STATE.exists():
        return
    st = json.loads(STATE.read_text(encoding="utf-8"))
    snap = {
        "snapshot_at": now(),
        "note": note,
        "done": sum(1 for t in st["tasks"].values() if t["status"] == "done"),
        "pending": sum(1 for t in st["tasks"].values() if t["status"] == "pending"),
        "running": sum(1 for t in st["tasks"].values() if t["status"] == "running"),
        "cards_main": len([f for f in glob.glob(str(ROOT / "target/go/*.md"))
                           if not f.endswith(".deep.md")]),
        "cards_deep": len(glob.glob(str(ROOT / "target/go/*.deep.md"))),
        "done_list": sorted(t["id"] for t in st["tasks"].values() if t["status"] == "done"),
    }
    SNAPSHOT.write_text(json.dumps(snap, ensure_ascii=False, indent=2), encoding="utf-8")


def write_quota_hint(hits):
    text = f"""# ⚠️ 额度耗尽，已于 {now()} 自动暂停

## 发生了什么

检测到 WorkBuddy 会话日志出现额度类错误，**所有并行 worker 都会被 429 打断**。
守护已自动：解冻僵死任务 → 刷新状态快照 → 停止派新任务。

## 命中记录（最近 {len(hits)} 条）

| 日志 | 命中 | 上下文 |
|---|---|---|
"""
    for name, pat, ctx in hits[-8:]:
        text += f"| `{name}` | `{pat}` | {ctx[:100]} |\n"
    text += f"""
## 你要做的

1. **买加量包 / 等额度恢复**：https://www.codebuddy.cn/profile/usage
2. 恢复后**删掉本文件**，然后：
   ```bash
   cd "{ROOT}"
   # 继续跑（串行，MAX_PARALLEL=1）
   /Users/Wang/.workbuddy/binaries/python/versions/3.13.12/bin/python3 _pipeline/queue.py status
   ```
3. 或直接对 agent 说「继续」，agent 会读 `SNAPSHOT.json` 接上

## 状态没有丢

- 已完成的卡片都在 `target/go/`
- 任务状态在 `_pipeline/state.json`（原子写入 + 幂等 done）
- 断点信息在 `_pipeline/SNAPSHOT.json`
- **重跑 `queue.py next` 即可续，不会重复劳动**
"""
    QUOTA_HINT.write_text(text, encoding="utf-8")


def status():
    snap = json.loads(SNAPSHOT.read_text(encoding="utf-8")) if SNAPSHOT.exists() else {}
    print(f"守护状态：{'⏸ 已暂停（额度耗尽）' if PAUSE_FLAG.exists() else '▶️ 运行中'}")
    if snap:
        print(f"快照时间：{snap.get('snapshot_at')}")
        print(f"  已完成 {snap.get('done')} / 剩余 {snap.get('pending')}")
        print(f"  卡片 {snap.get('cards_main')} 主 + {snap.get('cards_deep')} 深挖")
        if snap.get("note"):
            print(f"  备注：{snap['note']}")
    if QUOTA_HINT.exists():
        print(f"  额度提示：{QUOTA_HINT}")
    wl = LOGS / "watchdog.log"
    if wl.exists():
        print("\n--- 日志尾部 ---")
        print("\n".join(wl.read_text(encoding="utf-8").splitlines()[-10:]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--once", action="store_true")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--resume", action="store_true", help="额度恢复后清掉暂停标记")
    a = ap.parse_args()

    if a.status:
        status()
        return 0
    if a.resume:
        PAUSE_FLAG.unlink(missing_ok=True)
        QUOTA_HINT.unlink(missing_ok=True)
        log("已清除暂停标记，恢复运行")
        write_snapshot("额度恢复，手动 resume")
        return 0
    if a.once:
        hits, quota = scan_429()
        log(f"单次检查：命中 {len(hits)} 条，额度耗尽={quota}")
        if quota:
            n = unfreeze()
            log(f"解冻 {n} 个僵死任务")
            write_snapshot("额度耗尽")
            write_quota_hint(hits)
        return 0

    mark_baseline()
    log("守护启动，每 %ds 检查一次（Ctrl-C 退出）" % INTERVAL)
    i = 0
    while True:
        i += 1
        try:
            hits, quota = scan_429()
            if quota:
                n = unfreeze()
                PAUSE_FLAG.write_text(now(), encoding="utf-8")
                write_snapshot(f"额度耗尽自动暂停（第 {i} 轮）")
                write_quota_hint(hits)
                log(f"⏸ 额度耗尽：命中 {len(hits)} 条，解冻 {n} 个任务，已暂停")
                log(f"   处理：买加量包后 python3 watchdog.py --resume")
                return 0
            if i % SNAPSHOT_EVERY == 0:
                write_snapshot("定时刷新")
                log(f"第 {i} 轮：正常，快照已刷新")
            time.sleep(INTERVAL)
        except KeyboardInterrupt:
            log("守护退出")
            return 0
        except Exception as e:
            log(f"守护异常（忽略继续）：{e}")
            time.sleep(INTERVAL)


if __name__ == "__main__":
    sys.exit(main())
