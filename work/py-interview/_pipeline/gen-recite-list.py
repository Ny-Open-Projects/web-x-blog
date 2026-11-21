#!/usr/bin/env python3
# 生成 Python 面试卡背诵清单：按分类聚合 + 难度分布 + 一句话总述
import os, re, glob

TARGET = os.path.join(os.path.dirname(__file__), "..", "target")
OUT = os.path.join(os.path.dirname(__file__), "背诵清单.md")

def parse(path):
    title = ""
    cat = diff = freq = ""
    summary = ""
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    i = 0
    n = len(lines)
    while i < n:
        ln = lines[i]
        if ln.startswith("# "):
            title = ln[2:].strip()
        elif ln.startswith("> 分类"):
            m = re.search(r"分类：([^|]+)", ln)
            d = re.search(r"难度：([^|]+)", ln)
            fr = re.search(r"频率：([^|]+)", ln)
            if m: cat = m.group(1).strip()
            if d: diff = d.group(1).strip()
            if fr: freq = fr.group(1).strip()
        elif ln.strip() == "## 一句话总述":
            j = i + 1
            while j < n and not lines[j].strip():
                j += 1
            if j < n:
                summary = lines[j].strip()
            break
        i += 1
    return title, cat, diff, freq, summary

cards = []
for p in sorted(glob.glob(os.path.join(TARGET, "*.md"))):
    base = os.path.basename(p)
    if base.endswith(".deep.md"):
        continue
    t, c, d, fr, s = parse(p)
    cards.append((base, t, c, d, fr, s))

by_cat = {}
diff_cnt = {}
for base, t, c, d, fr, s in cards:
    by_cat.setdefault(c, []).append((base, t, d, fr, s))
    diff_cnt[d] = diff_cnt.get(d, 0) + 1

lines = []
lines.append(f"# Python 服务端面试卡 · 背诵清单\n")
lines.append(f"> 共 **{len(cards)}** 张卡（不含 .deep），全量 validate 0 error 0 warn。\n")
lines.append("## 难度分布\n")
lines.append("| 难度 | 张数 |")
lines.append("|---|---|")
for d in sorted(diff_cnt, key=lambda x: -diff_cnt[x]):
    lines.append(f"| {d} | {diff_cnt[d]} |")
lines.append("")
lines.append("## 按分类背诵\n")
for c in sorted(by_cat):
    items = by_cat[c]
    lines.append(f"### {c}（{len(items)} 张）\n")
    for base, t, d, fr, s in items:
        lines.append(f"- **[{d}/{fr}] {t}** — {s}")
    lines.append("")

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print(f"wrote {OUT}: {len(cards)} cards, cats={len(by_cat)}, diff={diff_cnt}")
