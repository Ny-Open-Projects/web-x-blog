#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
checkdup.py — 编号冲突与交叉引用自检

背景：多 worker 并行出卡时，编号段可能撞车（实际已发生：701 段 4 文件、601-604 曾被两批同时占用）。
本脚本把「撞号」变成**可执行门禁**，而不是靠 worker 自觉。

用法：
  python3 checkdup.py            # 检查编号冲突 + 交叉引用有效性
  python3 checkdup.py --fix      # 自动改号（冲突时）
  python3 checkdup.py --allocate 10   # 申请 N 个安全编号（供 worker 调用）
"""

import argparse
import os
import re
import sys
from pathlib import Path

ROOT = Path(os.environ.get("MT_ROOT", Path(__file__).resolve().parent.parent)).resolve()
TARGET = ROOT / "target" / "go"
PIPE = ROOT / "_pipeline"          # 锁文件与预占表放这里

# 保留段：001 号样卡已定稿，不参与自动改号
RESERVED = {"001"}

# 允许「同号分卡」的编号：同一编号下多张**主卡**是合法的分卡，不是撞号。
# 判定依据由人工确认（见 TODO-worker.md 第 3 条：脚本查不出主题重复）。
# 例：126 下的 `lazy-singleton`（DCL 单例）与 `singleflight`（请求合并）
#     同源（16-5 附近）但主题完全不同，属 SPEC 允许的"一个技术点一张卡"。
# 维护方式：把确认过的编号加进来，并在这里写明各卡的主题。
# ⚠️ 加之前必须人工确认「同号 + 不同主题」，否则就是放过真撞车。
ALLOWED_SAME_NUM = {
    "126": "lazy-singleton(DCL 单例) / singleflight(请求合并) —— 同源不同主题",
}


DEEP_SUFFIX = ".deep.md"


def _stem(name):
    """去掉 .deep.md 后缀（注意后缀是 9 字符，含前导点）。"""
    return name[:-len(DEEP_SUFFIX)] if name.endswith(DEEP_SUFFIX) else name


def cards():
    """返回 {编号: [文件名, ...]}，含主卡与 .deep.md"""
    out = {}
    if not TARGET.is_dir():
        return out
    for p in sorted(TARGET.glob("*.md")):
        # 2026-10-04：编号段已扩展到 4 位（901~1004、1101+），故 3~4 位都接受。
        # 只写 \d{3} 会让 1001/1101 这类新卡**完全进不了冲突检测**（静默漏检）。
        m = re.match(r"^(\d{3,4})-", p.name)
        if m:
            out.setdefault(m.group(1), []).append(p.name)
    return out


def check_crossrefs():
    """检查卡内「见 XXX 卡」类引用是否指向真实存在的编号"""
    missing = []
    if not TARGET.is_dir():
        return missing
    # 2026-10-04：同步放宽到 3~4 位，否则 1101 卡里写「见 593 卡」能查、写「见 1101 卡」查不到。
    #
    # 2026-10-04 二次修订 —— **区分「前向引用」与「真悬空」**：
    # 背景：worker 三次报告"坏引用"，查证**三次都是合法前向引用**
    # （卡 A 引用了同批稍后才生成的卡 B，如 931→938、932→936/938、1009→1010）。
    # 每次都要 lead 人工判定，白耗注意力。**根因不是 worker 多事，是本工具把两者混为一谈。**
    # 判据：如果被引用的编号 **不在任何已存在的卡里**，但库中已有**比它更大的编号**
    #   → 它多半是"还没生成"（前向引用），标 ⏳，不算错；
    # 反之如果引用的编号**比全库最大编号还大**、或小到明显不存在（如 2048/767 这类误报）
    #   → 才更可能是真问题，标 ⚠。
    pat = re.compile(r"见\s*(\d{3,4})\s*卡")
    allnums = []
    for q in TARGET.glob("*.md"):
        m = re.match(r"^(\d{3,4})-", q.name)
        if m:
            allnums.append(int(m.group(1)))
    maxnum = max(allnums) if allnums else 0
    for p in sorted(TARGET.glob("*.md")):
        t = p.read_text(encoding="utf-8")
        for num in pat.findall(t):
            if (TARGET / num).exists() or list(TARGET.glob(f"{num}-*.md")):
                continue
            tag = "前面还有卡（疑似前向引用，等目标卡落盘即自动解析）" if int(num) < maxnum \
                  else "编号大于全库最大值（疑似误报或远期引用）"
            missing.append((p.name, num, tag))
    return missing


def allocate(n=1, do_reserve=True):
    """分配 n 个未占用编号，跨 100 递增。**带锁 + 预占**，防并发撞号。

    2026-10-03 踩坑：两个 worker 同时 `--allocate`，**拿到同一批号**
    （159 撞号）。根因是「查询未占用」与「标记占用」之间有窗口期。
    修法：加文件锁串行化，并在 `.reserved_ids` 里**预占**，
    即使落盘前又被抢号，收工时的 `checkdup` 仍会报出来（有兜底）。

    2026-10-04 修第二个坑：`report()`（**只读检查**）也在调本函数拿"建议编号"，
    于是每跑一次查重就往 `.reserved_ids` 追加 5 条 —— **只读命令在偷偷写状态**。
    累积到 657 条，其中 528 条是没有任何卡片的垃圾预占。
    修法：加 `do_reserve` 开关，**只有真正分配（--allocate）才写预占表**；
    只读展示一律 `do_reserve=False`。
    """
    import time
    lock = PIPE / ".allocate.lock"
    for _ in range(20):                 # 等锁最多 20 秒
        try:
            fd = os.open(str(lock), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.close(fd)
            break
        except FileExistsError:
            time.sleep(1)
    else:
        print("  ⚠ 拿不到分配锁（可能被占），仍继续分配 —— 收工时 checkdup 会报冲突")

    try:
        # 预占表也要算进「已占用」
        reserve = PIPE / ".reserved_ids"
        taken = set()
        if reserve.exists():
            taken = {x.strip() for x in reserve.read_text().splitlines() if x.strip()}
        used = set(cards().keys()) | taken
        out = []
        # 2026-10-04 改：项目已改为「每个 worker 绑定固定号段」的手工编号
        # （gpG=901 起 / gpM=1001 起 / gpL=1101 起），**正常情况下不要再调用 --allocate**。
        # 但仍保留可用性：3 位段用尽后自动落到 4 位段，避免静默产出空结果。
        ranges = [(100, 1000, 3), (1000, 2000, 4)]
        for start, stop, width in ranges:
            for i in range(start, stop):
                num = f"{i:0{width}d}"
                if num in RESERVED or num in used:
                    continue
                out.append(num)
                used.add(num)
                if len(out) >= n:
                    break
            if len(out) >= n:
                break
        # 写入预占表 —— **仅真正分配时写**；只读展示（do_reserve=False）绝不落盘
        if out and do_reserve:
            reserve.parent.mkdir(parents=True, exist_ok=True)
            with reserve.open("a", encoding="utf-8") as f:
                for num in out:
                    f.write(num + "\n")
        return out
    finally:
        try:
            lock.unlink()
        except Exception:
            pass


def check_topic_dup():
    """检查**同一源文件被做成多张卡**（软告警，需人工判断角度是否重复）。

    两次踩坑的教训（不要再走回头路）：
      ① **不能用「段落号相同」判重** —— 实测 002-g-signal(第36~50段) 与
         114-p-status(第36~42段) 起始段号都是 36，但来自不同源文件、主题完全不同。
      ② **不能用「标题分词指纹」判重** —— 中文标题无空格，2 字滑窗取到
         懒汉/汉式/式单 这种位置碎片，同题不同措辞就漏。

    可靠主键是**源文件路径**，但卡片头部目前没统一记录它（ 只记段号）。
    因此这里退而求其次：按**卡内出现的源目录线索**做弱聚合，并在没有线索时明确
    提示「无法自动判重，请靠流程（开工前查 state.json 的 running 任务）」。
    """
    if not TARGET.is_dir():
        return []
    by_src = {}
    pat = re.compile(r"source/(\d+)/|源文件[：:].*?(\d+)-\d+")
    for p in sorted(TARGET.glob("*.md")):
        if p.name.endswith(".deep.md"):
            continue
        t = p.read_text(encoding="utf-8")
        m = pat.search(t)
        if not m:
            continue
        key = m.group(1) or m.group(2)
        by_src.setdefault(key, set()).add(p.name)
    return [(k, sorted(v)) for k, v in by_src.items() if len(v) > 1]


def report():
    c = cards()
    print(f"卡片目录：{TARGET}")
    print(f"已用编号：{len(c)} 段，文件总数 {sum(len(v) for v in c.values())}")

    # 1. 同号多主卡 = 冲突（除非在 ALLOWED_SAME_NUM 白名单里）
    print("\n--- 编号冲突检查 ---")
    bad = False
    for num, files in sorted(c.items()):
        mains = [f for f in files if not f.endswith(".deep.md")]
        if len(mains) > 1:
            # ⚠️ 2026-10-04：v3→v4 迁移期，同号允许「英文名(v3) + 中文名(v4)」并存。
            # 这是**预期的迁移对**（v4 是 v3 的重做版），不是撞号。
            # 重做完成、v3 卡删除后，本条自动失效。
            if len(mains) == 2:
                has_cjk = [bool(re.search(r"[\u4e00-\u9fff]", f)) for f in mains]
                if has_cjk[0] != has_cjk[1]:      # 一中一英
                    print(f"  ⏳ {num}：v3(英) + v4(中) 并存 —— 迁移对，非冲突")
                    continue
            if num in ALLOWED_SAME_NUM:
                print(f"  ✓ {num}：{len(mains)} 个主卡并存（**已确认为分卡**，见白名单）")
                for f in mains:
                    print(f"      {f}")
                print(f"      依据：{ALLOWED_SAME_NUM[num]}")
            else:
                print(f"  ✗ 冲突 {num}：{len(mains)} 个主卡并存")
                for f in mains:
                    print(f"      {f}")
                print(f"    → 若确为分卡（同源不同主题），请把 {num} 加进 ALLOWED_SAME_NUM 并写明依据")
                bad = True
    if not bad:
        print("  ✓ 无同号多主卡冲突")

    # 2. .deep.md 必须有对应主卡
    print("\n--- 深挖卡挂靠检查 ---")
    bad2 = False
    for num, files in sorted(c.items()):
        allnames = set(files)
        for f in files:
            if f.endswith(DEEP_SUFFIX):
                main = _stem(f)
                if (main + ".md") not in allnames:
                    print(f"  ✗ 孤儿深挖：{f}（缺 {main}.md）")
                    bad2 = True
    if not bad2:
        print("  ✓ 所有 .deep.md 都有对应主卡")

    # 3. 交叉引用有效性
    print("\n--- 交叉引用检查 ---")
    miss = check_crossrefs()
    if miss:
        # 2026-10-04：区分「前向引用」（⏳ 正常，等目标卡落盘即解析）与「疑似误报/真问题」（⚠）
        fwd = [x for x in miss if "前向引用" in x[2]]
        oth = [x for x in miss if "前向引用" not in x[2]]
        for src, num, tag in oth:
            print(f"  ⚠ {src} 引用了不存在的「见 {num} 卡」 —— {tag}")
        for src, num, tag in fwd:
            print(f"  ⏳ {src} →「见 {num} 卡」尚未生成（{tag}）")
        print(f"  （⏳ {len(fwd)} 条前向引用属正常；⚠ {len(oth)} 条需人工确认）")
    else:
        print("  ✓ 所有「见 XXX 卡」引用均有效")

    # 4. 主题查重（软告警，需人工确认）
    print("\n--- 主题查重 ---")
    print("  ⚠ 本项**无法自动检查**，必须人工确认（这是设计限制，不是我写漏了）：")
    print("    · 本批选题是否与 running 任务同源文件？→ 开工前查 state.json")
    print("    · 已有同源文件的卡，我这张角度是否不同？→ ls target/go/ 读标题")
    tdup = check_topic_dup()
    if tdup:
        for key, files in tdup:
            print(f"  ? 源目录 {key} 出现 {len(files)} 张（**请人工判断角度是否重复**）：")
            for f in files:
                print(f"      {f}")
    else:
        print("  （卡内无源路径线索可聚合）")

    # 5. **自相矛盾检查**：被纠错否掉的旧结论，是否残留在别的小节
    #    动机：2026-10-03 301 卡改了第 4 条的结论（IO 密集不是"没用"），
    #    但「总结」和「.deep.md」里各藏着 3 处旧表述 —— 同一张卡自相矛盾，
    #    读者按总结背就正好背错。人眼查不出来，必须脚本查。
    print("\n--- 自相矛盾检查（旧结论残留）---")
    # 每个条目：易错的旧断言 → 必须被统一的新措辞替代
    # ⚠️ 只收窄到「GOMAXPROCS / IO 密集」这一组 ——
    #    之前把「收益消失」泛化后误报了 160 卡的一致性哈希选型表
    #    （那里「收益消失」是正确表述，不是被推翻的旧结论）。
    #    **教训：矛盾检查的关键词必须与"具体被推翻的结论"绑定，不能泛化成常见短语。**
    STALE = [
        (r"IO\s*密集调它没用", "改用「IO 密集先定位瓶颈再调」"),
        (r"IO\s*密集别动\s*`?GOMAXPROCS", "改用「取决于瓶颈位置」"),
        (r"纯 CPU 才靠调\s*`?GOMAXPROCS", "改用「纯 CPU 最确定；IO 先定位瓶颈」"),
    ]
    found = False
    for p in sorted(TARGET.glob("*.md")):
        t = p.read_text(encoding="utf-8")
        # 只查「正文」，跳过纠错节本身（那里可以引用旧说法做对照）
        body = t.split("## ⚠️ 原文纠错")[0]
        for pat, advice in STALE:
            for m in re.finditer(pat, body):
                line_no = body[:m.start()].count("\n") + 1
                lines = body.splitlines()
                line = lines[line_no - 1] if line_no <= len(lines) else ""
                # 排除「引用旧说法做对照」的表述。
                # ⚠️ 判据只能看**本行 + 同行前后**——曾用 90 字窗口，结果跨行误匹配：
                # 上一行写「…调它没用」，下一行写「改用…」，窗口同时命中两边 → 漏报。
                # 现在只在本行内判断，并在行内找「改用/不是…而是」等**明确纠错标记**。
                if line.lstrip().startswith(">"):
                    continue
                if re.search(r"不能(再|贸然)?说|改用|而非|不是.{0,15}(而是|是)|正确.{0,4}结论|已被|推翻|勿再|不要再|不是错|曾经的",
                             line):
                    continue
                print(f"  ✗ {p.name}:{line_no} 残留旧结论 → {advice}")
                print(f"      {line.strip()[:70]}")
                found = True
    if not found:
        print("  ✓ 无旧结论残留")

    # 6. 下次可用编号
    # ⚠️ 只读展示：必须 do_reserve=False，否则「查重」会顺手污染 .reserved_ids
    print(f"\n--- 建议可用编号：{', '.join(allocate(5, do_reserve=False))} ... ---")
    print("    （本项目现采用 worker 固定号段手工编号：gpG=901+ / gpM=1001+ / gpL=1101+）")
    return 1 if (bad or bad2 or miss or found) else 0   # 主题为软告警，不影响退出码


def fix():
    """把冲突的多主卡中，靠后的改到新编号，并同步卡内引用"""
    c = cards()
    changed = []
    for num, files in sorted(c.items()):
        mains = [f for f in files if not f.endswith(".deep.md")]
        if len(mains) <= 1:
            continue
        if num in ALLOWED_SAME_NUM:
            # 已确认是分卡，绝不能改号
            print(f"skip {num}（白名单分卡，不改号）: {len(mains)} 个主卡")
            continue
        keep, move = mains[0], mains[1:]
        newnums = allocate(len(move))
        for f, nn in zip(move, newnums):
            old_stem = Path(f).stem
            new_stem = nn + old_stem.split("-", 1)[1]
            (TARGET / f).rename(TARGET / (new_stem + ".md"))
            deep_old = old_stem + ".deep.md"
            if (TARGET / deep_old).exists():
                (TARGET / deep_old).rename(TARGET / (new_stem + ".deep.md"))
            changed.append((f, new_stem + ".md"))
            # 同步该卡内部的自引用
            p = TARGET / (new_stem + ".md")
            t = p.read_text(encoding="utf-8")
            t = re.sub(r"^# " + re.escape(old_stem), "# " + new_stem, t, flags=re.M)
            p.write_text(t, encoding="utf-8")
    if changed:
        print("已改号：")
        for a, b in changed:
            print(f"  {a}  ->  {b}")
    else:
        print("无需改号")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix", action="store_true")
    ap.add_argument("--allocate", type=int)
    a = ap.parse_args()
    if a.allocate:
        nums = allocate(a.allocate)
        print(" ".join(nums) if nums else "（无空位）")
        return 0
    if a.fix:
        return fix()
    return report()


if __name__ == "__main__":
    sys.exit(main())
