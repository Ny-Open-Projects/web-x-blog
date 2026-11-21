---
title: [SCN-501] 笔试题——实现场景 SLA 看板（多级聚合/达标率/P95 热力）？
date: 2026-11-20
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-501：手写 SLA 看板：多级聚合（业务→功能→接口）、达标率、P95 热力

**需求与边界**：
- 输入：链路耗时流水；输出：SLA 达标看板。
- 边界要求：① 多级聚合（业务线→功能→接口钻取）；② 达标率（P95 ≤ SLA 的比例）+超限明细；③ P95 热力图（时段×接口——定位慢时段）；④ 预算对照（SCN-401 预算 vs 实测）。

**答**：
```javascript
function slaBoard(rows, { slas }) {            // rows: [{biz, feature, api, ms, ts}]
  const agg = (group) => ({
    p50: quantile(group.map(r => r.ms), 0.5),
    p95: quantile(group.map(r => r.ms), 0.95),
    sla: slas[group.key],
    ok: quantile(group.map(r => r.ms), 0.95) <= slas[group.key],
    count: group.length,
  });
  const byBiz = groupBy(rows, 'biz').map(agg);       // 业务级
  const byFeature = groupBy(rows, 'feature').map(agg);   // 功能级（钻取）
  // P95 热力：时段(hour) × api 矩阵
  const heat = groupBy(rows, r =>
    `${hour(r.ts)}:${r.api}`).map(agg);
  return {
    biz: sortBy(byBiz, 'p95').reverse(),      // 最慢置顶
    feature: byFeature, heat,
    breaches: rows.filter(r => r.ms > slas[r.api]).slice(0, 20),
  };                                           // 超限明细（可下钻）
}
// 钻取：biz → feature → 超限明细行（trace 定位）；
// 预算对照：sla vs 实测 p95（偏差标红）。
```

**评分点**:
- 多级聚合钻取（业务→功能→明细 trace）。
- 达标率判定（P95 ≤ SLA）+ 超限明细可定位。
- P95 热力矩阵（时段×接口——定位慢时段）。
- 预算对照（偏差标红——SCN-401 闭环）。
