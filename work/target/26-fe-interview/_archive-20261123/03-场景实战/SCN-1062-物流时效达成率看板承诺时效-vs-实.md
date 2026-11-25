---
title: [SCN-1062] 物流时效达成率看板（承诺时效 vs 实际）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1062：物流时效达成率看板（承诺时效 vs 实际）

**答**：
- 指标：承诺时效达成率（分线路/网点）、超时件分布（哪段延误）。
- 归因：超时归因（干线/分拨/派送），责任方定位。
- 看板：趋势 + Top 超时线路列表 + 改进任务联动。

```javascript
// 时效看板
function slaBoard(waybills, promises) {
  const rows = waybills.map(w => ({
    ...w, promise: promises[w.line],
    actualH: (w.deliveredAt - w.createdAt) / 3600_000,
  }));
  const hit = rows.filter(r => r.actualH <= r.promise);
  return { rate: +(hit.length / rows.length * 100).toFixed(1) + '%',
    topLate: rows.filter(r => r.actualH > r.promise)
      .sort((a, b) => b.actualH - r.promise - (a.actualH - a.promise))
      .slice(0, 5) };
}
```
