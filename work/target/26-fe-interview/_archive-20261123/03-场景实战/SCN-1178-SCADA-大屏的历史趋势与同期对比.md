---
title: [SCN-1178] SCADA 大屏的历史趋势与同期对比（同比环比）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1178：SCADA 大屏的历史趋势与同期对比（同比环比）

**答**：
- 对比：产量/能耗同比（去年同期）/环比（上月），季节因素标注（旺季）。
- 归因：产量下降归因（停机天数/速度/良率分解，1160 模型）。
- 展示：同比曲线叠加（对齐横轴）。

```javascript
// 同期对比
function yoyCompare(cur, lastYear) {
  const align = cur.map((v, i) => ({ cur: v, last: lastYear[i] ?? null }));
  return {
    yoy: +(cur.reduce((s, v) => s + v, 0) / Math.max(1, lastYear.reduce((s, v) => s + v, 0)) * 100 - 100).toFixed(1) + '%',
    aligned: align,                                    // 对齐叠加曲线
    seasonNote: isPeakSeason() ? '旺季因素需剔除' : null,
  };
}
function isPeakSeason() { return false; }
```
