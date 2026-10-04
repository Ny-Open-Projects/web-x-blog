#!/usr/bin/env python3
"""扫描待处理组的源文件健康度：字节数 / 字符数 / 有效行数 / 估算内容行数。

用法:
    python3 ai/scripts/scan_pending_sources.py 4.k8s4-cka
    python3 ai/scripts/scan_pending_sources.py 3.k8s3-top
输出按编号排序，空文件与可疑残缺（有效行 < 10）单独标出来。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # /Users/Wang/Code/github/web-x-blog
SRC = ROOT / "work" / "source"

NOISE = re.compile(r'^\s*([-—=~*#\s])\1{3,}\s*$')


def probe(path: Path):
    raw = path.read_bytes()
    if not raw:
        return 0, 0, 0
    text = raw.decode("utf-8", errors="replace")
    chars = len(text.strip())
    lines = [l for l in text.splitlines() if l.strip() and not NOISE.match(l)]
    return len(raw), chars, len(lines)


def main():
    course = sys.argv[1]
    d = SRC / course
    if not d.exists():
        sys.exit(f"不存在: {d}")

    rows = []
    for p in d.glob("*.txt"):
        # 编号 = 文件名开头第一个空格/分隔符之前的 token
        stem = p.stem
        num = stem.split(" ")[0].strip()
        tail = stem[len(num):].strip().lstrip("-").strip()
        raw, chars, lines = probe(p)
        rows.append((num, tail[:40], raw, chars, lines, p.name))

    rows.sort(key=lambda r: r[0])

    print(f"{'编号':<12}{'字节':>8}{'字符':>8}{'有效行':>8}  标题")
    bad = []
    for num, tail, raw, chars, lines, name in rows:
        flag = ""
        if raw == 0 or chars == 0:
            flag = "  <<< 空文件"
            bad.append(num)
        elif lines < 10:
            flag = f"  <<< 残缺(仅{lines}行)"
            bad.append(num)
        print(f"{num:<12}{raw:>8}{chars:>8}{lines:>8}  {tail}{flag}")

    print(f"\n共 {len(rows)} 个源文件；疑似空/残缺 {len(bad)} 个：{bad}")


if __name__ == "__main__":
    main()
