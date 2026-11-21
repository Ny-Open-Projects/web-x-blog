#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python 面试自测 CLI。

从 docs/*.md 解析全部题目,支持按章节/标签/难度筛选,乱序抽题自测:
先只显示「问」,回车后展开「答/代码/追问」,可自评掌握程度,结束输出统计。

用法(需 Python 3.9+,本机系统 /usr/bin/python3 可直接跑):
    python3 scripts/quiz.py                     # 全库随机 10 题
    python3 scripts/quiz.py -n 20               # 随机 20 题
    python3 scripts/quiz.py -c 6                # 只抽第 6 章(Agent)
    python3 scripts/quiz.py -t asyncio          # 按标签过滤
    python3 scripts/quiz.py -t "pandas" -n 15   # 标签 + 数量
    python3 scripts/quiz.py -d 5                # 只要 5 星难题
    python3 scripts/quiz.py --list              # 列出章节与题数
"""
import argparse
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

Q_SPLIT = re.compile(r"^### (Q\d+) · (.+)$", re.M)
META = re.compile(r"^>\s*难度:([★☆]+) \| 标签:(.+)$", re.M)
QUESTION = re.compile(r"\*\*问\*\*[:：](.+?)(?=\n\*\*答\*\*)", re.S)


def parse_docs():
    """解析全部文档(含分类子目录),返回题目列表。"""
    items = []
    for md in sorted(DOCS.rglob("*.md")):
        if md.parent.name == "paths":  # 学习路径/索引文档,非题目
            continue
        text = md.read_text(encoding="utf-8")
        category = md.parent.name if md.parent != DOCS else ""
        head = re.match(r"^# (.+)$", text, re.M)
        title = head.group(1).strip() if head else md.stem
        chapter = f"{category} · {title}" if category else title
        hits = list(Q_SPLIT.finditer(text))
        for i, hit in enumerate(hits):
            end = hits[i + 1].start() if i + 1 < len(hits) else len(text)
            block = text[hit.start():end]
            meta = META.search(block)
            stars = meta.group(1).count("★") if meta else 0
            tags = [t.strip() for t in meta.group(2).split(",")] if meta else []
            qm = QUESTION.search(block)
            question = re.sub(r"\s+", " ", qm.group(1)).strip() if qm else ""
            items.append({
                "chapter": chapter,
                "num": hit.group(1),
                "title": hit.group(2).strip(),
                "stars": stars,
                "tags": tags,
                "question": question,
                "body": block,
            })
    return items


def show(it, idx, total):
    stars = "★" * it["stars"]
    tagline = ", ".join(it["tags"])
    print(f"\n[{idx}/{total}] {it['num']} · {it['title']}")
    print(f"难度:{stars} | 标签:{tagline}")
    print(f"章节:{it['chapter']}")
    print(f"\n{it['question']}\n")


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("-n", type=int, default=10, help="抽题数量(默认 10)")
    ap.add_argument("-c", type=int, default=None, help="章节号 1-10")
    ap.add_argument("-t", default=None, help="标签过滤(模糊匹配,不区分大小写)")
    ap.add_argument("-d", type=int, default=None, help="难度星级 1-5")
    ap.add_argument("-l", type=int, choices=(1, 2, 3), default=None,
                    help="层级:1 基础(1-2星) / 2 进阶(3星) / 3 高级(4-5星)")
    ap.add_argument("--ordered", action="store_true",
                    help="按「由浅入深」顺序出题(分类->星级->题号),而非乱序")
    ap.add_argument("--list", action="store_true", help="列出分类与题数后退出")
    args = ap.parse_args()

    items = parse_docs()
    if args.list:
        chapters = {}
        for it in items:
            chapters.setdefault(it["chapter"], []).append(it)
        for ch in sorted(chapters):
            print(f"{ch:<40} {len(chapters[ch]):>3} 题")
        print(f"合计 {len(items)} 题")
        return 0

    pool = items
    if args.c:
        prefix = f"{args.c:02d}"
        pool = [x for x in pool if x["chapter"].startswith(prefix)]
    if args.t:
        t = args.t.lower()
        pool = [x for x in pool
                if any(t in tg.lower() for tg in x["tags"]) or t in x["title"].lower()]
    if args.d:
        pool = [x for x in pool if x["stars"] == args.d]
    if args.l:
        pool = [x for x in pool if (1 if x["stars"] <= 2 else 2 if x["stars"] == 3 else 3) == args.l]
    if not pool:
        print("没有匹配的题目,换条件试试(--list 查看章节)", file=sys.stderr)
        return 1
    if args.ordered:
        pool.sort(key=lambda x: (x["chapter"], x["stars"], x["num"]))
        picked = pool[: args.n]
    else:
        random.shuffle(pool)
        picked = pool[: args.n]

    print("=" * 62)
    print(f"自测开始:{len(picked)} 题(共命中 {len(pool)} 题)。回车看答案,q 退出,r 换题。")
    print("=" * 62)
    stats = {"会": 0, "模糊": 0, "不会": 0}
    grades = []
    quit_now = False
    for i, cur in enumerate(picked, 1):
        it = cur
        show(it, i, len(picked))
        cmd = input("回车看答案 / r 换一题 / q 退出 > ").strip().lower()
        if cmd == "q":
            quit_now = True
        elif cmd == "r":
            it = random.choice(pool)
            while it["num"] == cur["num"] and len(pool) > 1:
                it = random.choice(pool)
            show(it, i, len(picked))
        if quit_now:
            break
        print("-" * 62)
        print(it["body"].strip())
        print("-" * 62)
        g = input("自评:1 会 / 2 模糊 / 3 不会 > ").strip()
        grade = {"1": "会", "2": "模糊", "3": "不会"}.get(g, "模糊")
        grades.append((it, grade))
        stats[grade] += 1

    print("\n" + "=" * 62)
    print(f"自测结束:{len(grades)} 题 | 会 {stats['会']} / 模糊 {stats['模糊']} / 不会 {stats['不会']}")
    weak = [it for it, g in grades if g != "会"]
    if weak:
        print("\n建议复习:")
        for it in weak:
            print(f"  {it['num']} · {it['title']} ({it['chapter']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
