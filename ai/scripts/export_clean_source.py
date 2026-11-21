#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""导出指定周/节的清洗后源文，供人工/LLM 写作时精读（只读，不改 source）。

用法:
    /usr/local/bin/python3 ai/scripts/export_clean_source.py 1 2
    /usr/local/bin/python3 ai/scripts/export_clean_source.py 1
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "work/source/20.体系课_人人都能学会数据分析[完结]"
WEEK_DIR = re.compile(r"^第(\d+)周")
NUM_PREFIX = re.compile(r"^\s*(\d+)\s*[-.]\s*(\d+)\s*")
# 只删「整行都是推广/工具痕迹」的行；正文里偶尔提到的词保留，避免误伤语义
NOISE_LINE = re.compile(r"更多IT资源|微信号|微信\s*\d+|迅捷文字转语音|www\.|https?://|ruike|2268731")


def clean_text(path: Path) -> str:
    """去掉推广行、工具痕迹与空行，保留完整讲述内容。"""
    kept = []
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        s = line.strip()
        if not s or NOISE_LINE.search(s):
            continue
        kept.append(s)
    return "\n".join(kept)


def main() -> None:
    week = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    section = int(sys.argv[2]) if len(sys.argv) > 2 else None
    week_dirs = [d for d in SRC.iterdir() if d.is_dir()
                 and (m := WEEK_DIR.match(d.name)) and int(m.group(1)) == week]
    if not week_dirs:
        raise SystemExit(f"找不到第 {week} 周目录")
    wd = week_dirs[0]
    out = [f"# 第 {week} 周 {wd.name} · 清洗后源文", ""]
    for f in sorted(wd.rglob("*.txt")):
        m = NUM_PREFIX.match(f.name)
        if not m:
            continue
        sec, les = int(m.group(1)), int(m.group(2))
        if section is not None and sec != section:
            continue
        title = NUM_PREFIX.sub("", f.name[:-4])
        title = re.sub(r"_\s*更多IT.*|-\s*迅捷.*|~?\d*\[\d+\]", "", title).strip(" -_")
        text = clean_text(f)
        out.append(f"\n## {sec}-{les} {title}\n")
        out.append(text if text else "[空文件]")
    target = Path(f"/tmp/w{week}" + (f"_s{section}" if section else "") + "_clean.md")
    target.write_text("\n".join(out), encoding="utf-8")
    print(f"已导出 {target} ({target.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
