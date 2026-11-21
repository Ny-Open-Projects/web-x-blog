#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 mksz824 润色进度面板（visualize fragment HTML）。

用法：python3 -I ai/scripts/render_mksz824_progress.py
输出：会话可视化目录 mksz824-polish-progress.html
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "work" / "target" / "mksz824"
VIZ = Path("/Users/Wang/zcode-multi/3/.zcode/v2/visualizations/a29d53a79c2dfa3173ec26624c01bfd346921def46d84f608082b3252f58d66b")

meta = json.loads((TARGET / "_CARDS_META.json").read_text(encoding="utf-8"))
cards = meta["cards"]
stat = Counter(c["status"] for c in cards)
polished = stat.get("polished", 0)
total = len(cards)

# 按章统计
by_ch = {}
for c in cards:
    ch = c["chapter_no"] or 0
    d = by_ch.setdefault(ch, {"raw": 0, "polished": 0})
    d[c["status"]] += 1

# 波次
waves = json.loads((TARGET / "_SCANS" / "WAVES.json").read_text(encoding="utf-8"))
done_set = {c["file"] for c in cards if c["status"] == "polished"}
wave_rows = []
for i, w in enumerate(waves):
    done = sum(1 for f in w["files"] if f in done_set)
    wave_rows.append((i + 1, w["tier"], len(w["files"]), done))

import datetime
now = datetime.datetime.now().strftime("%m-%d %H:%M")

ch_bars = ""
for ch in sorted(by_ch):
    d = by_ch[ch]
    pct = d["polished"] * 100 // max(d["polished"] + d["raw"], 1)
    ch_bars += f"""
    <div style="display:flex;align-items:center;gap:8px;margin:3px 0;">
      <span class="text-muted" style="width:42px;text-align:right;flex:none;">第{ch}章</span>
      <div class="progress" style="flex:1;" role="progressbar" aria-label="第{ch}章进度"
           aria-valuenow="{pct}" aria-valuemin="0" aria-valuemax="100">
        <div class="progress-bar" style="width:{pct}%"></div>
      </div>
      <span class="tabular-nums text-small" style="width:70px;flex:none;">{d["polished"]}/{d["polished"]+d["raw"]}</span>
    </div>"""

wave_tags = ""
for n, tier, nfiles, done in wave_rows:
    if done == nfiles:
        color = "var(--green)"
    elif done > 0:
        color = "var(--yellow)"
    else:
        color = "var(--border)"
    wave_tags += (f'<span style="display:inline-block;flex:none;width:26px;height:18px;border-radius:4px;'
                  f'background:{color};opacity:.85;" data-tooltip="波次{wave_rows[n-1][0]}（{tier}）{done}/{nfiles}"></span>')

html = f"""<div id="mksz824-progress">
  <div class="viz-grid" style="margin-bottom:8px;">
    <div class="card viz-stat"><div class="text-muted">已润色 / 总卡片</div>
      <div class="viz-stat-value tabular-nums">{polished}<span style="font-size:16px;"> / {total}</span></div>
      <div class="text-small text-muted">更新 {now}</div></div>
    <div class="card viz-stat"><div class="text-muted">总体进度</div>
      <div class="viz-stat-value tabular-nums">{polished * 100 // total}%</div>
      <div class="text-small text-muted">波次流水线 · 每波约 30 篇</div></div>
    <div class="card viz-stat"><div class="text-muted">剩余</div>
      <div class="viz-stat-value tabular-nums">{total - polished}<span style="font-size:16px;"> 篇</span></div>
      <div class="text-small text-muted">约 {(total - polished) // 30 + 1} 个波次</div></div>
  </div>
  <div class="card" style="padding:12px;">
    <div class="text-small text-muted" style="margin-bottom:6px;">波次状态（绿=完成 黄=进行中 灰=待派发）</div>
    <div style="display:flex;gap:4px;flex-wrap:wrap;">{wave_tags}</div>
  </div>
  <div style="margin-top:10px;">{ch_bars}</div>
</div>
"""

VIZ.mkdir(parents=True, exist_ok=True)
out = VIZ / "mksz824-polish-progress.html"
out.write_text(html, encoding="utf-8")
print(out)
