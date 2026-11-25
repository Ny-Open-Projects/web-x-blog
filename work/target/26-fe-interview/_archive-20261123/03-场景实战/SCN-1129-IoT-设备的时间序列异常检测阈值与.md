---
title: [SCN-1129] IoT 设备的时间序列异常检测（阈值与基线）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1129：IoT 设备的时间序列异常检测（阈值与基线）

**答**：
- 检测：静态阈值（超限告警）+ 动态基线（同时间历史均值 ±3σ）。
- 前端：异常点标注（曲线红色标记）+ 异常事件列表联动。
- 误报：动态基线学习期（前 2 周只学习不告警）。

```javascript
// 动态基线
function dynamicBaseline(history, current, { learning = false } = {}) {
  const sameHour = history.filter(h => sameHourOfDay(h.ts, current.ts));
  const mean = avg(sameHour.map(h => h.value));
  const sd = std(sameHour.map(h => h.value));
  const anomaly = !learning && Math.abs(current.value - mean) > 3 * sd;
  return { anomaly, baseline: [mean - 3 * sd, mean + 3 * sd] };
}
function sameHourOfDay(a, b) { return new Date(a).getHours() === new Date(b).getHours(); }
function avg(a) { return a.reduce((s, v) => s + v, 0) / (a.length || 1); }
function std(a) { const m = avg(a); return Math.sqrt(avg(a.map(v => (v - m) ** 2))); }
```
