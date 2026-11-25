---
title: [VIZ-276] 手写日历热力图（GitHub 风格）：格子布局与色阶
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-276：手写日历热力图（GitHub 风格）：格子布局与色阶

**答**：
- 题目：日历热力图——按周列布局（53 列×7 行），每日活跃度→色阶（5 档），月标签定位。复用 ALG-543 色阶思想。
- 思路：日期对齐（weekStart 偏移）；每日值 → 分位数分档（四分位）；月首格标月名。
- 评分点：周列对齐；分位数分档（数据驱动阈值）；月标签定位。

```javascript
function calendarHeatmap(dailyCounts, { year = new Date().getFullYear() } = {}) {
  const start = new Date(year, 0, 1);
  const cells = [];
  const values = Object.values(dailyCounts).filter(v => v > 0).sort((a, b) => a - b);
  const quantile = (p) => values[Math.floor(values.length * p)] ?? 0;
  const thresholds = [quantile(0.25), quantile(0.5), quantile(0.75), quantile(1)];   // 四分位分档
  const level = v => v === 0 ? 0 : 1 + thresholds.findIndex(t => v <= t);
  for (let week = 0; week < 53; week++)
    for (let day = 0; day < 7; day++) {
      const date = new Date(start);
      date.setDate(start.getDate() + week * 7 + day - start.getDay() + 1);
      if (date.getFullYear() !== year) continue;
      const key = date.toISOString().slice(0, 10);
      cells.push({ date: key, col: week, row: (date.getDay() + 6) % 7,
        level: level(dailyCounts[key] ?? 0),
        monthLabel: date.getDate() === 1 ? date.toLocaleString('zh', { month: 'short' }) : null });
    }
  return { cells, legend: [0, 1, 2, 3, 4] };
}
```
