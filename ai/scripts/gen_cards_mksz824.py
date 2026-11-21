#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mksz824（24.真实高质量低代码商业项目）基础卡片生成器。

从 work/source/24.../ 的 .md 讲稿确定性生成 work/target/mksz824/ 基础卡片：
  - 文件名：<编号>-<清洗标题>.md（编号取章节号-讲号，如 1-1、15-3）
  - 正文：口播稿按句分段落（不做 LLM 改写，status: raw，待精修）
  - front-matter：仅存 _META 字段于 _CARDS_META.json，blog 落位时再加 hexo front-matter

用法：python3 ai/scripts/gen_cards_mksz824.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "work" / "source" / "24.真实高质量低代码商业项目-前端后端运维管理系统"
OUT = ROOT / "work" / "target" / "mksz824"

COURSE_TITLE = "真实高质量低代码商业项目，前端/后端/运维/管理系统"

ZW = re.compile(r"[\u200b\u200c\u200d\ufeff]")


def clean_title(stem: str) -> str:
    t = ZW.sub("", stem)
    t = re.sub(r"[_\s]+$", "", t)  # 尾部 _. 与空格
    t = re.sub(r"\s+", " ", t).strip(" -_—·、")
    t = t.replace("第二布", "第二步")  # ASR 错别字（文件名实测 6 处）
    return t


def lesson_code(stem: str) -> str:
    m = re.match(r"^\s*(\d+(?:[-.]\d+)*)", ZW.sub("", stem))
    return m.group(1).replace(".", "-") if m else ""


def chapter_no(dirname: str) -> str:
    m = re.match(r"^第(\d+)章", dirname)
    return m.group(1) if m else ""


def to_paragraphs(text: str) -> str:
    """口播稿按句号/问号/叹号分段落：每 3-5 句合一段。"""
    text = ZW.sub("", text)
    text = re.sub(r"[ \t]+", " ", text)
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    body = "".join(lines)
    sents = re.split(r"(?<=[。！？!?])", body)
    sents = [s.strip() for s in sents if s.strip()]
    paras, buf = [], []
    for s in sents:
        buf.append(s)
        if len("".join(buf)) >= 160:
            paras.append("".join(buf))
            buf = []
    if buf:
        paras.append("".join(buf))
    return "\n\n".join(paras)


def main() -> int:
    meta = []
    used = set()
    for d in sorted(SRC.iterdir()):
        if not d.is_dir() or d.name.startswith(("_", ".")):
            continue
        ch = chapter_no(d.name)
        # 第 7 章 Done/ 子目录为重复副本（第 2 遍扫描逐篇核对），剔除
        mds = [p for p in sorted(d.rglob("*.md")) if "Done" not in p.parts]
        for p in mds:
            lc = lesson_code(p.stem)
            title = clean_title(p.stem)
            # 章内讲号重启（各章都从 1-1 开始），全局编号 = 章号 + 章内讲号
            if ch and lc and not lc.startswith(ch + "-"):
                code = f"{ch}-{lc}"
            else:
                code = lc
            # 标题去掉开头序号
            title = re.sub(r"^\d+(?:[-.]\d+)*\s*", "", title).strip() or title
            words = len(p.read_text(encoding="utf-8", errors="ignore").strip())
            body = to_paragraphs(p.read_text(encoding="utf-8", errors="ignore"))
            slug = f"{code}-{title}" if code else title
            slug = re.sub(r"[\\/:*?\"<>|]", "，", slug).strip()
            fname = slug + ".md"
            n = 2
            while fname in used:
                fname = f"{slug}-{n}.md"
                n += 1
            used.add(fname)
            (OUT / fname).write_text(f"# {slug}\n\n{body}\n", encoding="utf-8")
            meta.append({
                "file": fname,
                "chapter": d.name,
                "chapter_no": int(ch) if ch else None,
                "code": code,
                "title": title,
                "words": words,
                "src": str(p.relative_to(ROOT)),
                "status": "raw",
            })
    (OUT / "_CARDS_META.json").write_text(
        json.dumps({"course": "mksz824", "course_title": COURSE_TITLE, "cards": meta},
                   ensure_ascii=False, indent=1),
        encoding="utf-8")
    print(f"生成卡片 {len(meta)} 篇 -> {OUT}")
    print(f"总字数 {sum(m['words'] for m in meta)}")


if __name__ == "__main__":
    raise SystemExit(main())
