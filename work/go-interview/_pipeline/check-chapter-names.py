#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ERRORS.md 章节名巡检（只报不改）—— r4-A 2026-10-05

背景：ERRORS.md 的段标题格式在历史上有三代写法混杂：
  A 新式：`## 第 8 章 并发模型与调度器·哪些情况下容易发生内存泄漏？（一）（源 8-11，卡 1325）`
          = `## <章节名>·<篇目标题>（源 <源id>，卡 <卡号>）`
  B 半式：`## 第 12 章 Redis 大 Key 的影响与处理（源 12-60，卡 1019）`
          = 只有「第 N 章」前缀，**没有 `·`**，章名位被篇目标题占用
  C 旧式：`## 链表反转与遍历复杂度（源 17-2，卡 159）`
          = 连「第 N 章」前缀都没有

本工具做四件事：
  1. 枚举所有段标题（行首 `## ` 且以 `（源 …，卡 …）` 结尾）
  2. 分桶 A / B / C，给总数
  3. 对 A 桶按章号统计「章节名」变体分布，并与权威章节名表比对
  4. 交叉校验「标题里的章号」vs「源 id 里的章号」（不一致 = 疑似错标）

用法：
  python3 _pipeline/check-chapter-names.py              # 出报告
  python3 _pipeline/check-chapter-names.py --selftest   # 只跑自测
  python3 _pipeline/check-chapter-names.py --md         # 报告用 markdown 表
"""

import re
import sys
import collections
from pathlib import Path

PROJ = Path(__file__).resolve().parent.parent
ERRORS = PROJ / "_pipeline" / "ERRORS.md"

# 权威章节名表（_pipeline/TODO-worker.md「📖 权威章节名表」，2026-10-05 定）
AUTHORITY = {
    1: "第 1 章 课程导学",
    2: "第 2 章 Go 语言概览与特性",
    3: "第 3 章 简历与求职准备",
    4: "第 4 章 Go 基础语法与标准库",
    5: "第 5 章 Go 语言进阶",
    6: "第 6 章 Go 语言高级特性",
    7: "第 7 章 常用库与框架",
    8: "第 8 章 并发模型与调度器",
    9: "第 9 章 数据类型底层原理",
    10: "第 10 章 并发编程",
    11: "第 11 章 性能优化",
    12: "第 12 章 数据库",
    13: "第 13 章 Elasticsearch",
    14: "第 14 章 消息中间件",
    15: "第 15 章 微服务",
    16: "第 16 章 设计模式",
    17: "第 17 章 数据结构与算法",
    18: "第 18 章 Linux / 网络",
    19: "第 19 章 项目与系统设计",
    20: "第 20 章 求职与录用",
}

# 章节名分隔符候选（历史上可能被误写的各种「点/间隔号」）
SEPS = {"\u00b7": "·(U+00B7 中点)", "\u30fb": "・(U+30FB 片假名中点)",
        "\u2022": "•(U+2022 项目符号)", "\u25e6": "◦", "\uff0e": "．(全角句点)",
        "\u2027": "‧(U+2027)"}

SEG_RE = re.compile(r"^## (?P<rest>.+)（源 (?P<src>[^）]+)，卡 (?P<card>[^）]+)）\s*$")
A_RE = re.compile(r"^(?P<chap>第 (?P<num>\d+) 章 )(?P<name>.+?)·(?P<title>.+)$")
B_RE = re.compile(r"^(?P<chap>第 (?P<num>\d+) 章 )(?P<title>.+)$")
C_RE = re.compile(r"^(?P<title>.+)$")


def parse_header(line: str):
    """把一行段标题解析为 dict；不是段标题则返回 None。"""
    m = SEG_RE.match(line)
    if not m:
        return None
    rest, src, card = m.group("rest"), m.group("src"), m.group("card")
    src_ch = None
    mm = re.match(r"(\d+)-", src)
    if mm:
        src_ch = int(mm.group(1))
    a = A_RE.match(rest)
    if a:
        return dict(bucket="A", chapter=a.group("num") and int(a.group("num")),
                    chapname=a.group("chap") + a.group("name"),
                    title=a.group("title"), src=src, src_ch=src_ch, card=card)
    b = B_RE.match(rest)
    if b:
        return dict(bucket="B", chapter=int(b.group("num")),
                    chapname=b.group("chap").rstrip(),  # 只有「第 N 章」
                    title=b.group("title"), src=src, src_ch=src_ch, card=card)
    c = C_RE.match(rest)
    return dict(bucket="C", chapter=None, chapname=None,
                title=c.group("title"), src=src, src_ch=src_ch, card=card)


def scan(text: str):
    rows = []
    for i, line in enumerate(text.split("\n"), 1):
        if not line.startswith("## "):
            continue
        r = parse_header(line)
        if r:
            r["line"] = i
            r["raw"] = line
            rows.append(r)
    return rows


# ─────────────────────────── 自测 ───────────────────────────
def selftest() -> int:
    fails = 0

    def eq(desc, got, want):
        nonlocal fails
        if got != want:
            fails += 1
            print(f"  ✗ {desc}\n      得到 {got!r}\n      期望 {want!r}")

    def ok(desc, cond):
        nonlocal fails
        if not cond:
            fails += 1
            print(f"  ✗ {desc}")

    print("check-chapter-names.py 自测")
    print("-" * 56)

    # ① A 桶：章名·篇目
    r = parse_header("## 第 8 章 并发模型与调度器·哪些情况下容易发生内存泄漏？（一）（源 8-11，卡 1325）")
    eq("A 桶 bucket", r["bucket"], "A")
    eq("A 桶 章号", r["chapter"], 8)
    eq("A 桶 章节名", r["chapname"], "第 8 章 并发模型与调度器")
    eq("A 桶 篇目", r["title"], "哪些情况下容易发生内存泄漏？（一）")
    eq("A 桶 源id", r["src"], "8-11")
    eq("A 桶 源章号", r["src_ch"], 8)

    # ② A 桶：篇目里含全角括号「（一）」，不能被当成分隔符/章号
    r = parse_header("## 第 16 章 设计模式·如何使用Go语言实现装饰器模式？（源 16-10，卡 1375）")
    eq("A 桶（含「？」篇目）章号", r["chapter"], 16)
    eq("A 桶（含「？」篇目）章节名", r["chapname"], "第 16 章 设计模式")

    # ③ B 桶：只有「第 N 章」前缀，无 ·
    r = parse_header("## 第 12 章 Redis 大 Key 的影响与处理（源 12-60，卡 1019）")
    eq("B 桶 bucket", r["bucket"], "B")
    eq("B 桶 章号", r["chapter"], 12)
    eq("B 桶 章节名（裸章号）", r["chapname"], "第 12 章")
    eq("B 桶 篇目", r["title"], "Redis 大 Key 的影响与处理")

    # ④ B 桶 + 篇目自带「（一）」
    r = parse_header("## 第 16 章 设计模式有哪些（一）（源 16-2，卡 1044）")
    eq("B 桶（一）篇目", r["title"], "设计模式有哪些（一）")

    # ⑤ C 桶：无章号前缀
    r = parse_header("## 链表反转与遍历复杂度（源 17-2，卡 159）")
    eq("C 桶 bucket", r["bucket"], "C")
    eq("C 桶 章节名=None", r["chapname"], None)
    eq("C 桶 章号=None", r["chapter"], None)
    eq("C 桶 源章号（仍可推断）", r["src_ch"], 17)

    # ⑥ C 桶：标题带 emoji / 全角冒号
    r = parse_header("## 🔴🔴 字符串切片会钉住整个底层数组（源 17-14，卡 238）")
    eq("C 桶 emoji 标题", r["title"], "🔴🔴 字符串切片会钉住整个底层数组")

    # ⑦ 非段标题（普通小节标题）不应被吃进来
    eq("非段标题（无 源/卡）", parse_header("## 反纠错（这些原文说对了，不要改）"), None)
    eq("非段标题（只有源）", parse_header("## IO 多路复用（源 18-34）"), None)

    # ⑧ 源 id 为复合（多篇合并段）
    r = parse_header("## 第 15 章 K8s 真跑回补（源 15-16/15-17/15-18/15-19，卡 1039/1040/1041/1042）")
    eq("复合源id 源章号", r["src_ch"], 15)
    eq("复合源id 章号", r["chapter"], 15)

    # ⑨ 分隔符两侧带空格的写法（ch12 真实写法）——章名会被解析出尾随空格
    r = parse_header("## 第 12 章 深度分页优化 · 覆盖索引/主键游标（源 12-46，卡 913）")
    eq("带空格分隔符 章号", r["chapter"], 12)
    ok("带空格分隔符 章名带尾随空格（正是要报的脏数据）",
       r["chapname"] == "第 12 章 深度分页优化 ")
    eq("带空格分隔符 篇目保留前导空格", r["title"], " 覆盖索引/主键游标")

    # ⑩ 章名分隔符若非 U+00B7，A 桶不该命中（应落到 B 或 C）
    r = parse_header("## 第 12 章 数据库・深度分页优化（源 12-46，卡 913）")
    ok("非 U+00B7 分隔符 → 不入 A 桶", r is not None and r["bucket"] != "A")

    print("-" * 56)
    print(f"自测：{'全部通过' if fails == 0 else str(fails) + ' 项失败'}（共 10 组断言）")
    return fails


# ─────────────────────────── 报告 ───────────────────────────
def report(as_md: bool) -> int:
    text = ERRORS.read_text(encoding="utf-8")
    rows = scan(text)
    total = len(rows)

    buckets = collections.Counter(r["bucket"] for r in rows)

    # A 桶：按章号统计章节名变体
    bych = collections.defaultdict(collections.Counter)
    for r in rows:
        if r["bucket"] == "A":
            bych[r["chapter"]][r["chapname"]] += 1

    # 交叉校验：标题章号 vs 源 id 章号
    mismatch = [r for r in rows
                if r["chapter"] is not None and r["src_ch"] is not None
                and r["chapter"] != r["src_ch"]]

    # 章名前缀写法变体（「第 N 章」本身是否有空格差异）
    prefix_var = collections.Counter()
    for r in rows:
        if r["bucket"] in ("A", "B"):
            m = re.match(r"(第\s*\d+\s*章)", r["chapname"])
            if m:
                prefix_var[m.group(1)] += 1

    print("=" * 60)
    print("ERRORS.md 章节名巡检报告（只报不改）")
    print("=" * 60)
    print(f"段标题总数（行首 '## ' 且以 '（源 …，卡 …）' 结尾）：{total}")
    print(f"  分桶：A 新式 章名·篇目 = {buckets['A']}"
          f"｜B 只有「第 N 章」无 · = {buckets['B']}"
          f"｜C 无章号前缀(旧式) = {buckets['C']}")
    print()

    print("── A 桶：章节名变体分布（按章号）──")
    multi = 0
    for num in sorted(bych):
        variants = bych[num]
        flag = ""
        auth = AUTHORITY.get(num)
        if num in AUTHORITY and len(variants) == 1 and list(variants)[0] == auth:
            flag = "  ✓ 与权威表一致"
        elif len(variants) > 1:
            multi += 1
            flag = f"  ⚠ {len(variants)} 种变体"
        elif num in AUTHORITY and list(variants)[0] != auth:
            flag = f"  ⚠ 与权威表不同（表={auth}）"
        print(f"  第 {num} 章（{sum(variants.values())} 条）{flag}")
        for k, v in sorted(variants.items(), key=lambda x: (-x[1], x[0])):
            note = ""
            if k != k.rstrip():
                note = "  ← 章名尾部含空格"
            print(f"      {v:>3} × 「{k}」{note}")
    print()

    print("── 章号前缀写法变体（A/B 桶）──")
    for k, v in sorted(prefix_var.items(), key=lambda x: -x[1]):
        print(f"  {v:>3} × 「{k}」")
    bad_prefix = [k for k in prefix_var if not re.fullmatch(r"第 \d+ 章", k)]
    print(f"  非标准写法（应为『第 N 章』）：{bad_prefix if bad_prefix else '无'}")
    print()

    print("── 交叉校验：标题章号 ≠ 源 id 章号（疑似错标）──")
    if mismatch:
        for r in mismatch:
            print(f"  ⚠ 行 {r['line']}：标题第 {r['chapter']} 章 vs 源 {r['src']}（章 {r['src_ch']}）"
                  f" → {r['raw'][:80]}")
    else:
        print(f"  无（{sum(1 for r in rows if r['chapter'] is not None)} 条有章号的标题全部与源 id 章号一致）")
    print()

    print("── 权威表命中率（各章 A 桶标准写法条数）──")
    for num in sorted(AUTHORITY):
        auth = AUTHORITY[num]
        hit = sum(1 for r in rows if r["bucket"] == "A" and r["chapname"] == auth)
        mark = "✓" if hit else ("—" if num not in bych else "✗")
        print(f"  {mark} ch{num:>2}  「{auth}」× {hit}")
    print()

    # 各章 × 桶 交叉表（C 桶用源 id 章号推断）
    cross = collections.defaultdict(collections.Counter)
    for r in rows:
        ch = r["chapter"] if r["chapter"] is not None else r["src_ch"]
        cross[ch][r["bucket"]] += 1
    print("── 各章 × 桶 交叉表（C 桶章号由源 id 推断）──")
    print(f"  {'章':>4} {'总':>4} {'A 章名·篇目':>10} {'B 只章号':>8} {'C 无前缀':>8}   权威表命中")
    for ch in sorted(k for k in cross if k is not None):
        c = cross[ch]
        hit = sum(1 for r in rows if r["bucket"] == "A" and r["chapname"] == AUTHORITY.get(ch))
        print(f"  {ch:>4} {sum(c.values()):>4} {c['A']:>10} {c['B']:>8} {c['C']:>8}   "
              f"{'✓ ' + str(hit) if hit else '✗ 0'}")
    unknown = cross.get(None, collections.Counter())
    if unknown:
        print(f"  {'?':>4} {sum(unknown.values()):>4}  源 id 无法解析章号")
    print()

    # 分隔符写法分布（A 桶）
    sep_style = collections.Counter()
    for r in rows:
        if r["bucket"] == "A":
            sep_style["第 N 章 <名> · <篇目>（两侧空格）" if " · " in r["raw"]
                      else "第 N 章 <名>·<篇目>（无空格）"] += 1
    print("── A 桶分隔符写法 ──")
    for k, v in sep_style.most_common():
        print(f"  {v:>3} × {k}")
    trail = [r for r in rows if r["bucket"] == "A" and r["chapname"] != r["chapname"].rstrip()]
    print(f"  章名尾部带空格（需清理）：{len(trail)} 条 —— 行号 "
          f"{[r['line'] for r in trail]}")
    print()

    # 变体总数（跨章去重前）
    all_variants = sum(len(v) for v in bych.values())
    print(f"── 汇总 ──")
    print(f"  A 桶章节名「写法」总数（跨章不去重，逐章相加）= {all_variants}")
    print(f"  其中多写法章号 = {multi} 个（{sorted(bych[n] and n for n in bych if len(bych[n])>1)}）")
    print(f"  权威表有定义但 A 桶 0 命中的章 = "
          f"{sorted(n for n in AUTHORITY if n not in bych)}")
    return 0


def main():
    if "--selftest" in sys.argv:
        sys.exit(selftest() and 1 or 0)
    if "--selftest-only" in sys.argv:
        sys.exit(selftest())
    selftest()
    print()
    report("--md" in sys.argv)


if __name__ == "__main__":
    main()
