#!/usr/bin/env python3
"""按「编号列」把 _PROGRESS.md 的 pending 行批量拨成 done（只动自己认领的编号段）。

用法:
    python3 ai/scripts/mark_progress_done.py k8stop 67-95 --map map.json
    python3 ai/scripts/mark_progress_done.py k8stop 48-66      # 无 map 时按源序号自动猜

映射表格式（map.json）：
    {"67": "5-34_xxx.md", "68": "5-35_yyy.md", "85": null}   # null = 保持 skip
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "work" / "target"

ROW = re.compile(r"^\| *([a-z]+) *\| *(\d+) \|")


def rows(text):
    for i, line in enumerate(text.splitlines(), 1):
        m = ROW.match(line)
        if m:
            yield i, m.group(1), m.group(2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("course")
    ap.add_argument("numrange", help="例如 67-95")
    ap.add_argument("--map", help="json 文件：编号 -> 文件名 或 null")
    args = ap.parse_args()

    lo, hi = (int(x) for x in args.numrange.split("-"))
    mapping = json.loads(Path(args.map).read_text(encoding="utf-8")) if args.map else {}

    path = TARGET / args.course / "_PROGRESS.md"
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    changed, missing, skipped = [], [], []
    for lineno, status, num in list(rows(text)):
        if not (lo <= int(num) <= hi):
            continue
        if status != "pending":
            continue
        idx = lineno - 1
        cells = [c.strip() for c in lines[idx].strip().strip("|").split("|")]
        if len(cells) < 6:
            missing.append((num, "行格式异常"))
            continue
        fn = mapping.get(num, "__AUTO__")
        if fn == "__AUTO__":
            fn = None
        if fn is None:
            continue  # skip 段：由调用方自行保证状态列已是 skip
        old = lines[idx]
        cells[0] = "done"
        cells[5] = fn
        lines[idx] = "| " + " | ".join(cells) + " |\n"
        changed.append((num, fn))
        if old == lines[idx]:
            missing.append((num, "无变化"))

    path.write_text("".join(lines), encoding="utf-8")
    print(f"[done] {len(changed)} 行 -> done")
    for n, f in changed:
        print(f"  #{n} -> {f}")
    if missing:
        print(f"[!] {len(missing)} 行未改动:", missing)
    if not changed:
        sys.exit(1)


if __name__ == "__main__":
    main()
