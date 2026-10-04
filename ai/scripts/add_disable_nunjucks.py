#!/usr/bin/env python3
"""给所有含 Nunjucks 敏感字符（{{ 或 {% ）的博客文章 front-matter 加 disableNunjucks: true。

原因：hexo 默认用 Nunjucks 渲染 post 正文，遇到 Helm/Go-template 的 {{ }}/{% %}
会直接 FATAL 导致整个 generate 失败。加 disableNunjucks 让 hexo 跳过模板解析，
这类文章里的 {{ }} 原样输出。只改 front-matter，不动正文。

用法:
    python3 ai/scripts/add_disable_nunjucks.py [course...]
"""
import re
import sys
from pathlib import Path

ROOT = Path("/Users/Wang/Code/github/web-x-blog")
TARGET = ROOT / "work" / "target"


def needs(ftext: str) -> bool:
    return ("{{" in ftext) or ("{%" in ftext)


def add_flag(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if not needs(text):
        return False
    if not text.startswith("---\n"):
        # 没有标准 front-matter，跳过（不应发生）
        return False
    if re.search(r"(?m)^disableNunjucks\s*:", text):
        return False  # 已有
    end = text.find("\n---", 3)
    if end < 0:
        return False
    head = text[:end]  # 含开头 ---
    body = text[end:]
    new_head = head.rstrip("\n") + "\ndisableNunjucks: true\n"
    path.write_text(new_head + body, encoding="utf-8")
    return True


def main():
    courses = sys.argv[1:]
    dirs = [TARGET / c for c in courses] if courses else [TARGET]
    changed = 0
    scanned = 0
    for d in dirs:
        if not d.is_dir():
            continue
        for f in sorted(d.rglob("*.md")):
            if f.name.startswith("_"):
                continue
            scanned += 1
            if add_flag(f):
                changed += 1
                print(f"[+disableNunjucks] {f.relative_to(ROOT)}")
    print(f"\nscanned={scanned} changed={changed}")


if __name__ == "__main__":
    main()
