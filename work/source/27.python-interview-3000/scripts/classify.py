#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""为知识库生成「由浅入深」学习路径与标签索引。

分级规则(按题目难度星级):
    L1 基础   = ★~★★        (1-2 星,校招/转行必会)
    L2 进阶   = ★★★          (3 星,社招 1-3 年主线)
    L3 高级   = ★★★★~★★★★★  (4-5 星,大厂资深岗压轴)

产出(写入 docs/paths/):
    00_标签索引.md      全库标签 -> 题号(按层级分组),用于定向补弱
    01~06_学习路径.md   每大类一份「由浅入深」刷题顺序表

用法: python3 scripts/classify.py   (纯标准库,3.9+)
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
OUT = DOCS / "paths"

Q_SPLIT = re.compile(r"^### (Q\d+) · (.+)$", re.M)
META = re.compile(r"^>\s*难度:([★☆]+) \| 标签:(.+)$", re.M)

CATS = {
    "01_语言核心与底层": "语言核心与底层",
    "02_并发与网络工程": "并发与网络工程",
    "03_Web后端开发": "Web 后端开发",
    "04_数据库与缓存": "数据库与缓存",
    "05_数据分析与工程化": "数据分析与工程化",
    "06_Agent与LLM及系统设计": "Agent 与 LLM 及系统设计",
}


def tier_of(stars: int) -> int:
    if stars <= 2:
        return 1
    if stars == 3:
        return 2
    return 3


TIER_NAME = {1: "L1 基础(★~★★)", 2: "L2 进阶(★★★)", 3: "L3 高级(★★★★~★★★★★)"}


def parse():
    """返回 {category: [q, ...]},q 含 num/title/stars/tags/file。"""
    cats = defaultdict(list)
    for md in sorted(DOCS.rglob("*.md")):
        if md.parent == DOCS:  # 跳过 paths 等
            continue
        cat = md.parent.name
        text = md.read_text(encoding="utf-8")
        hits = list(Q_SPLIT.finditer(text))
        for i, hit in enumerate(hits):
            end = hits[i + 1].start() if i + 1 < len(hits) else len(text)
            block = text[hit.start():end]
            meta = META.search(block)
            fm = re.search(r"# file: (code/\S+)", block)
            cats[cat].append({
                "num": hit.group(1),
                "title": hit.group(2).strip(),
                "stars": meta.group(1).count("★") if meta else 0,
                "tags": [t.strip() for t in meta.group(2).split(",")] if meta else [],
                "file": fm.group(1) if fm else "",
            })
    return cats


def write_paths(cats):
    OUT.mkdir(parents=True, exist_ok=True)
    for i, (cat, cname) in enumerate(CATS.items(), 1):
        qs = cats.get(cat, [])
        lines = [f"# 第 {i} 类 · {cname} · 由浅入深学习路径", "",
                 f"> 共 {len(qs)} 题:L1 基础 {sum(1 for q in qs if tier_of(q['stars']) == 1)} 题 → "
                 f"L2 进阶 {sum(1 for q in qs if tier_of(q['stars']) == 2)} 题 → "
                 f"L3 高级 {sum(1 for q in qs if tier_of(q['stars']) == 3)} 题。",
                 "> 建议顺序:先按本表顺序过一遍(会的不看),再用 `quiz.py -t 标签` 定向补弱。", ""]
        for t in (1, 2, 3):
            tier_qs = [q for q in qs if tier_of(q["stars"]) == t]
            tier_qs.sort(key=lambda q: (q["stars"], q["num"]))
            lines.append(f"## {TIER_NAME[t]} · {len(tier_qs)} 题")
            lines.append("")
            for q in tier_qs:
                stars = "★" * q["stars"] or "☆"
                tags = ", ".join(q["tags"])
                lines.append(f"- **{q['num']}** `{stars}` {q['title']}  *({tags})*")
            lines.append("")
        out = OUT / f"{i:02d}_学习路径.md"
        out.write_text("\n".join(lines), encoding="utf-8")
        print(f"wrote {out.relative_to(ROOT)} ({len(qs)} 题)")


def write_tag_index(cats):
    tag_qs = defaultdict(list)
    for cat, qs in cats.items():
        for q in qs:
            for tg in q["tags"]:
                tag_qs[tg].append(q)
    rows = sorted(tag_qs.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    lines = ["# 全库标签索引", "",
             f"> {len(rows)} 个标签。高频标签即大厂高频考点;点击类目后用 `quiz.py -t 标签` 定向抽题。", ""]
    lines.append("| 标签 | 题数 | L1 | L2 | L3 | 涉及题号(最多 12 个) |")
    lines.append("|---|---|---|---|---|---|")
    for tg, qs in rows:
        l1 = sum(1 for q in qs if tier_of(q["stars"]) == 1)
        l2 = sum(1 for q in qs if tier_of(q["stars"]) == 2)
        l3 = sum(1 for q in qs if tier_of(q["stars"]) == 3)
        nums = " ".join(q["num"] for q in qs[:12]) + (" …" if len(qs) > 12 else "")
        lines.append(f"| {tg} | {len(qs)} | {l1} | {l2} | {l3} | {nums} |")
    out = OUT / "00_标签索引.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)} ({len(rows)} 标签)")


def main():
    cats = parse()
    total = sum(len(v) for v in cats.values())
    print(f"解析 {total} 题")
    write_paths(cats)
    write_tag_index(cats)
    return 0


if __name__ == "__main__":
    sys.exit(main())
