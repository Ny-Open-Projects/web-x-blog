---
title: [SCN-1164] SCADA 大屏的生产计划与实际进度对比（甘特）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1164：SCADA 大屏的生产计划与实际进度对比（甘特）

**答**：
- 对比：生产计划甘特（计划开始/结束 vs 实际），延误订单标红。
- 进度：订单进度百分比（产量/计划量）实时更新。
- 预测：当前速度外推完成时间（预计延期预警）。

```javascript
// 生产甘特
function productionGantt(orders) {
  return orders.map(o => ({
    order: o.no, plan: [o.planStart, o.planEnd],
    actual: o.actualStart ? [o.actualStart, o.actualEnd ?? Date.now()] : null,
    progress: +(o.output / o.planQty * 100).toFixed(1) + '%',
    forecastEnd: o.actualStart
      ? o.actualStart + (Date.now() - o.actualStart) / (o.output / o.planQty)
      : null,
    late: Date.now() > o.planEnd && o.output < o.planQty,
  }));
}
```
