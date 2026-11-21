#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""M4 夜班滚动助手：标记单元 done 并跑 QC。用法：python3 ai/scripts/m4_mark_done.py u007 u008"""
from __future__ import annotations
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "work/target/34-java-suite/m4/_m4_state.json"
POSTS = ROOT / "work/target/34-java-suite/m4/posts"
# agent 偶发把连字符写成点号（34.java-suite），自动回收
STRAY = ROOT / "work/target/34.java-suite"

def recover_stray() -> None:
    if STRAY.exists():
        stray_posts = STRAY / "m4/posts"
        if stray_posts.exists():
            POSTS.mkdir(parents=True, exist_ok=True)
            for f in list(stray_posts.glob("*.md")) + list((STRAY / "m1").glob("*.md")) if False else list(stray_posts.glob("*.md")):
                shutil.move(str(f), POSTS / f.name)
        shutil.rmtree(STRAY, ignore_errors=True)

def main() -> None:
    recover_stray()
    st = json.loads(STATE.read_text(encoding="utf-8"))
    for uid in sys.argv[1:]:
        if uid not in st["done"]:
            st["done"].append(uid)
    json.dump(st, open(STATE, "w"), ensure_ascii=False)
    subprocess.run([sys.executable, str(ROOT / "ai/scripts/m4_qc.py")], check=False)

if __name__ == "__main__":
    main()
