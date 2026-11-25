---
title: [NODE-1020] 笔试题——实现 SLA 影响分析（SLA 变更的下游影响）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-1020：手写影响分析

**需求与边界**：
- 需求：SLA 影响分析（SCN-SLA-965/954）——① SLA 变更的下游影响（依赖矩阵——SCN-NODE-915）；② 影响面的门禁（SCN-OPS-229）；③ 影响面的通知（SCN-OPS-864）；④ 影响的报告（SCN-OPS-261）。
- 边界：① 依赖矩阵（SCN-NODE-915）；② 门禁（SCN-OPS-229）；③ 通知（SCN-OPS-864）。

**答**：
```javascript
async function slaChangeImpact(consumer, newSla) {
  const dependents = await slaDependents(consumer);    // 依赖矩阵（SCN-NODE-915）
  const impacts = dependents.map(d => ({
    consumer: d, affected: !canSupport(d.sla, newSla),   // 下游 SLA 支撑校验（SCN-SLA-1004）
  }));
  const impacted = impacts.filter(i => i.affected);
  if (impacted.length) await notify({ to: impacted.map(i => i.consumer.ownerRole),
    ackRequired: true });                              // 通知（SCN-OPS-864）
  return { impacts, gate: impacted.length ? 'BLOCK' : 'PASS' };   // 门禁（SCN-OPS-229）
}
```

**评分点**:
- 依赖矩阵（SCN-NODE-915）。
- 下游支撑校验（SCN-SLA-1004）。
- 通知 ack 门（SCN-OPS-864/229）。
