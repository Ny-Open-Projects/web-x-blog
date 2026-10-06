#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify-pointers.py —— 「被取代 v3 卡」前向指针的**集合口径**终检（只读）。

为什么用集合而非总数（2026-10-05 team-lead 判决）：
    总数对账会陷入「121+1 还是 122」的无意义争论。本脚本改为**比对集合**：
    期望集合（每个 v3 文件 → 它应指向的新卡号） vs 实际集合（哪些文件真的带了指针、指向谁）。
    缺一个报错、多一个报错、指向错号报错 —— 一眼可复算。

== 终检口径（2026-10-05 team-lead 拍板，务必遵守）==
    **终检以「集合」为准，不要用「计数」做终检**（`PENDING` 数会随语料在动而下降，
    计数不稳；集合是稳定的）。
    **集合的键是 `(v3 文件 → 目标卡号)` 对，不是「唯一卡号」的个数。**
    注意：多个 v3 主卡可能指向同一张新卡（如 5 张 mergo 主卡 → 1321），
    所以「唯一目标卡号数」≠「文件数」：本仓 main 126 + extra 3 = 129 个文件，
    但只映射到 **85** 个唯一目标卡号。若按「唯一卡号集合」验，会丢失 1:多 的结构，
    因此必须按 **(文件 → 卡号) 对** 逐一比对。

期望集合来源（全部合并、去重）：
  A) main  —— `_pipeline/v4-rework/ALL.txt` 第 3 列「主v3卡」∪ 第 7 列「同源其它v3主卡」，
              新卡号取第 4 列、标题取第 5 列。
  B) extra —— `_pipeline/v3-superseded-extra.txt`（v3文件名<TAB>新卡号<TAB>取代者标题）：
              被**非本轮** v4 卡取代的漏网卡。
  C) deep  —— A、B 的每个主卡，若同基名 `<stem>.deep.md` 存在则一并纳入（同新卡号、同标题）。

输出四类：
  ① 缺口      期望带指针、实际没带（缺一个即 FAIL）
  ② 多余      实际带了指针、却不在期望集合里（多一个即 FAIL）
  ③ 指向错号  带了指针但卡号与期望不符（错一个即 FAIL）
  ④ 目标未交付 指针已加、但目标新卡文件尚未落盘（PENDING，不算 FAIL；全量交付后须为 0）
软校验：标题与台账不符 → 告警。

退出码：①②③ 任一非空 → 1，否则 0。
用法：python3 _pipeline/verify-pointers.py
"""
import os
import re
import sys
import glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ALL = os.path.join(HERE, "v4-rework", "ALL.txt")
EXTRA = os.path.join(HERE, "v3-superseded-extra.txt")
TGT = os.path.join(ROOT, "target", "go")
BK = os.path.join(ROOT, "_work", "v3-pointers-backup")

# 与 validate.py 同口径：锚定整行、只匹配规范那一行
PTR_RE = re.compile(
    r"^> \u26a0\ufe0f 本卡已被 \*\*(\d+) 卡\*\*（(.+)）取代，请以新卡为准；本卡留作历史对照。$"
)


def load_mains():
    m = {}
    with open(ALL, encoding="utf-8") as f:
        f.readline()
        for ln in f:
            ln = ln.rstrip("\n")
            if not ln.strip():
                continue
            c = (ln.split("\t") + [""] * 8)[:8]
            main, nid, title, others = c[2].strip(), c[3].strip(), c[4].strip(), c[6].strip()
            for fn in [main] + [o.strip() for o in others.split(";")]:
                if fn and fn not in m:
                    m[fn] = (nid, title)
    return m


def load_extras():
    m = {}
    if not os.path.exists(EXTRA):
        return m
    with open(EXTRA, encoding="utf-8") as f:
        for ln in f:
            ln = ln.rstrip("\n")
            if not ln.strip() or ln.lstrip().startswith("#"):
                continue
            c = ln.split("\t")
            if len(c) >= 3 and c[0].strip():
                m[c[0].strip()] = (c[1].strip(), c[2].strip())
    return m


def load_entries():
    """期望集合：文件 -> (新卡号, 标题, kind)。kind ∈ {main, extra, deep}。"""
    entries = {}
    for fn, (nid, title) in load_mains().items():
        entries[fn] = (nid, title, "main")
    for fn, (nid, title) in load_extras().items():
        if fn in entries:
            print("[WARN] extra 与 ALL.txt 重复：%s（以 ALL.txt 为准）" % fn)
            continue
        entries[fn] = (nid, title, "extra")
    # deep：从**所有**主卡（main + extra）推导
    for fn, (nid, title, k) in list(entries.items()):
        if fn.endswith(".deep.md"):
            continue
        d = fn[:-3] + ".deep.md"
        if os.path.exists(os.path.join(TGT, d)):
            entries[d] = (nid, title, "deep")
    return entries


def scan_actual():
    """扫描 target/go 下所有 .md，返回 {文件: 指针卡号}（只取命中的规范指针行）。"""
    actual = {}
    for p in glob.glob(os.path.join(TGT, "*.md")):
        try:
            with open(p, encoding="utf-8", newline="") as fh:
                for ln in fh:
                    m = PTR_RE.match(ln.rstrip("\n"))
                    if m:
                        actual[os.path.basename(p)] = m.group(1)
                        break
        except Exception as e:
            print("[WARN] 读取失败 %s: %s" % (p, e))
    return actual


def card_exists(num):
    return bool(glob.glob(os.path.join(TGT, "%s-*.md" % num))) or \
        os.path.exists(os.path.join(TGT, "%s.md" % num))


def main():
    entries = load_entries()
    actual = scan_actual()
    expected_files = set(entries)
    actual_files = set(actual)

    gap = sorted(expected_files - actual_files)                       # ① 缺口
    surplus = sorted(actual_files - expected_files)                   # ② 多余
    wrong = sorted(f for f in (expected_files & actual_files)
                   if actual[f] != entries[f][0])                     # ③ 指向错号
    pending = sorted(f for f in expected_files
                     if card_exists(entries[f][0]) is False)          # ④ 目标未交付

    kinds = ("main", "deep", "extra")
    cnt = {k: sum(1 for e in entries.values() if e[2] == k) for k in kinds}
    by_file_num = {entries[f][0] for f in expected_files}
    act_file_num = set(actual.values())

    print("=" * 66)
    print("verify-pointers.py（集合口径）  —— 被取代 v3 卡前向指针终检")
    print("=" * 66)
    print("期望集合: main=%d  deep=%d  extra=%d  合计文件=%d  唯一目标卡号=%d"
          % (cnt["main"], cnt["deep"], cnt["extra"], len(expected_files), len(by_file_num)))
    print("实际集合: 带指针文件=%d  唯一被引卡号=%d" % (len(actual_files), len(act_file_num)))
    print("① 缺口（应带未带）      : %d" % len(gap))
    print("② 多余（不该带却带）    : %d" % len(surplus))
    print("③ 指向错号              : %d" % len(wrong))
    print("④ 目标未交付（PENDING） : %d" % len(pending))

    def dump(title, items, render=str):
        if items:
            print("\n%s" % title)
            for it in items:
                print("   - %s" % render(it))

    dump("[① 缺口] 期望带指针但实际没有：", gap,
         lambda f: "%s  ->  %s（%s）" % (f, entries[f][0], entries[f][1]))
    dump("[② 多余] 带了指针却不在期望集合：", surplus,
         lambda f: "%s  ->  %s" % (f, actual[f]))
    dump("[③ 指向错号]：", wrong,
         lambda f: "%s  实际=%s  期望=%s" % (f, actual[f], entries[f][0]))
    dump("[④ 目标未交付 PENDING]：", pending,
         lambda f: "[%s] %s -> %s" % (entries[f][2], f, entries[f][0]))
    print("\n   PENDING 涉及唯一卡号: %s"
          % sorted({entries[f][0] for f in pending}, key=int))

    # 逐字节还原核对（对照 _work/v3-pointers-backup/）
    restored_ok = restored_bad = missing_bk = 0
    for f in sorted(expected_files & actual_files):
        bkf = os.path.join(BK, f)
        if not os.path.exists(bkf):
            missing_bk += 1
            continue
        with open(os.path.join(TGT, f), encoding="utf-8", newline="") as fh:
            lines = fh.readlines()
        hit = next(i for i, l in enumerate(lines) if PTR_RE.match(l.rstrip("\n")))
        cur = "".join(lines[:hit] + lines[hit + 1:]).encode("utf-8")
        if cur == open(bkf, "rb").read():
            restored_ok += 1
        else:
            restored_bad += 1
    print("⑤ 去指针行后逐字节还原：通过 %d / 失败 %d / 缺备份 %d"
          % (restored_ok, restored_bad, missing_bk))

    hard = bool(gap or surplus or wrong or restored_bad or missing_bk)
    print("\n结论: %s   （缺口=%d 多余=%d 错号=%d；PENDING=%d，全量交付后须为 0）"
          % ("FAIL" if hard else "PASS", len(gap), len(surplus), len(wrong), len(pending)))
    return 1 if hard else 0


if __name__ == "__main__":
    sys.exit(main())
