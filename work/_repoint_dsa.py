#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""统一重指向 21.dsa 工具链：基路径 / 博客路径(blog_v2->根) / 语言路径(->code/)。"""
import os

ROOT = "/Users/Wang/Code/github/web-x-blog/work/target/21.dsa"
OLD_BASE = "/Users/Wang/Code/webfault-ai/dsa"
NEW_BASE = "/Users/Wang/Code/github/web-x-blog/work/target/21.dsa"
LANGS = ["ts", "go", "python", "java", "rust", "lua", "c", "cpp", "r", "zig", "dart"]

SH_LANG_FIXES = {
    "verify_all.sh": ["$DSA/go", "$DSA/ts", "$DSA/python", "$DSA/java"],
    "verify_new.sh": ["$DSA/$lang"],
}


def is_binary(path):
    try:
        with open(path, "rb") as f:
            return b"\x00" in f.read(8192)
    except Exception:
        return True


changed = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    for fn in filenames:
        fp = os.path.join(dirpath, fn)
        if is_binary(fp):
            continue
        try:
            text = open(fp, "r", encoding="utf-8").read()
        except Exception:
            try:
                text = open(fp, "r", encoding="latin-1").read()
            except Exception:
                continue
        orig = text
        rel = os.path.relpath(fp, ROOT)
        in_tools = rel.startswith("_tools/")

        # (A) 基路径
        if OLD_BASE in text:
            text = text.replace(OLD_BASE, NEW_BASE)

        # (B/C) 工具链 .py
        if in_tools and fn.endswith(".py"):
            text = text.replace("blog_v2", "")                      # 博客路径 -> 根
            for L in LANGS:                                        # 语言 f-string -> code/
                text = text.replace("{DSA}/%s/" % L, "{DSA}/code/%s/" % L)
            text = text.replace("DSA_DIR / lang", 'DSA_DIR / "code" / lang')  # pathlib
            text = text.replace(                                   # gen_blog base 特殊
                "{DSA}/{'ts' if lang == 'typescript' else lang}",
                "{DSA}/code/{'ts' if lang == 'typescript' else lang}")
            text = text.replace("{DSA}/{lang}/", "{DSA}/code/{lang}/")  # gen_bs 变量 lang

        # (C) 两个 verify 脚本的语言路径
        if in_tools and fn in SH_LANG_FIXES:
            for token in SH_LANG_FIXES[fn]:
                text = text.replace(token, token.replace("$DSA/", "$DSA/code/"))

        if text != orig:
            open(fp, "w", encoding="utf-8").write(text)
            changed.append(rel)

print("变更文件数:", len(changed))
for c in changed:
    print("  ", c)
