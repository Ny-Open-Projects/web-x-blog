---
title: [SCN-1117] IoT 设备数据大屏（园区能耗监控）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1117：IoT 设备数据大屏（园区能耗监控）

**答**：
- 指标：分回路能耗（电/水/气）实时功率 + 日/月累计，能耗排名（区域对比）。
- 图表：功率实时曲线 + 能耗柱状对比 + 异常能耗（基线偏差）标注。
- 刷新：功率 5s（边缘聚合上报），累计 1 分钟。

```javascript
// 能耗大屏
function energyBoard(meters) {
  const byZone = groupBy(meters, m => m.zone);
  return Object.entries(byZone).map(([zone, ms]) => ({
    zone,
    power: ms.reduce((s, m) => s + m.powerKW, 0),
    todayKWh: ms.reduce((s, m) => s + m.todayKWh, 0),
    anomaly: baselineDeviation(ms),                    // 基线偏差
  })).sort((a, b) => b.power - a.power);
}
function baselineDeviation(ms) { return null; }
function groupBy(arr, fn) { const m = {}; arr.forEach(x => { const k = fn(x); (m[k] ??= []).push(x); }); return m; }
```
