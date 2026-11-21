#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mksz824 target 卡片 → blog _posts 落位。

读取 work/target/mksz824/_CARDS_META.json，把每张卡片加 hexo front-matter
后拷到 work/blog/source/_posts/mksz824/<NNNN>-<原文件名>（4 位全局序号，与 mksz826 同范式）。

用法：python3 ai/scripts/publish_mksz824.py [--only-status polished]
"""
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "work" / "target" / "mksz824"
POSTS = ROOT / "work" / "blog" / "source" / "_posts" / "mksz824"

CATEGORIES = ["低代码商业项目"]
TAGS = ["Vue3", "低代码", "前端工程化", "Node.js", "Nuxt"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only-status", default=None)
    args = ap.parse_args()

    meta = json.loads((TARGET / "_CARDS_META.json").read_text(encoding="utf-8"))
    cards = meta["cards"]
    if args.only_status:
        cards = [c for c in cards if c.get("status") == args.only_status]

    POSTS.mkdir(parents=True, exist_ok=True)
    n = 0
    for i, c in enumerate(sorted(cards, key=lambda x: (x["chapter_no"] or 99, x["code"], x["file"])), 1):
        src = TARGET / c["file"]
        if not src.exists():
            print(f"[跳过] 缺卡片 {c['file']}")
            continue
        title = f"{c['code']} {c['title']}".strip()
        fm = (
            "---\n"
            "disableNunjucks: true\n"
            f"title: {title}\n"
            f"date: 2026-11-17 {8 + (i % 10):02d}:{i % 60:02d}:00\n"
            f"categories: [{CATEGORIES[0]}]\n"
            f"tags: [{', '.join(TAGS)}]\n"
            "---\n\n"
        )
        body = src.read_text(encoding="utf-8")
        # 卡片首行是 "# 标题"，与 front-matter title 重复，去掉
        if body.startswith("# "):
            body = body.split("\n", 1)[1].lstrip("\n")
        (POSTS / f"{i:04d}-{c['file']}").write_text(fm + body, encoding="utf-8")
        n += 1
    print(f"落位 {n} 篇 -> {POSTS}")


if __name__ == "__main__":
    raise SystemExit(main())
