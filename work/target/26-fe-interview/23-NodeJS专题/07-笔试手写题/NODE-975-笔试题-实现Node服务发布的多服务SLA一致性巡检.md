---
title: [NODE-975] 笔试题——实现多服务 SLA 一致性巡检（SLA 与容量对齐）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-975：手写 SLA 巡检

**需求与边界**：
- 需求：SLA 一致性（SCN-SLA-975/699）——① SLA 与容量对齐（SLA 承诺的容量 ≥ 实际——SCN-NODE-699）；② SLA 与降级矩阵对齐（降级预案支撑 SLA——SCN-OPS-329）；③ 巡检的告警（不对齐——SCN-SLA-975）；④ 巡检的修复建议（SCN-SLA-975）。
- 边界：① 容量数据源（SCN-NODE-765 预估）；② 降级矩阵数据源（SCN-OPS-329）；③ 巡检的周期（月度——SCN-SLA-975）。

**答**：
```javascript
async function slaCapacityAlignment() {
  for (const sla of allSlas()) {
    const cap = await capacityFor(sla.service);        // 容量（SCN-NODE-765）
    const required = slaQps(sla);                      // SLA 承诺
    if (cap < required) alert({ type: 'SLA_CAP_MISMATCH', service: sla.service,
      fix: `扩容至 ${required} QPS 或降级 SLA（SCN-NODE-699）` });   // 修复建议
    if (!degradeMatrixCovers(sla)) alert({ type: 'SLA_DEGRADE_GAP', service: sla.service,
      fix: '补降级矩阵（SCN-OPS-329）' });             // 降级对齐（SCN-OPS-329）
  }
}
```

**评分点**:
- SLA 与容量对齐（SCN-NODE-699/765）。
- SLA 与降级矩阵对齐（SCN-OPS-329）。
- 修复建议（SCN-SLA-975）。
