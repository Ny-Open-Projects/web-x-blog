---
title: [NODE-1024] 笔试题——实现租户 SLA 报告聚合（分层→全景）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-1024：手写报告聚合

**需求与边界**：
- 需求：报告聚合（SCN-SLA-995/1024）——① 分层报告聚合（SCN-SLA-995）；② 全景看板（SCN-SLA-968）；③ 公平性（SCN-SLA-1000）；④ 报告的消费（SCN-OPS-728）。
- 边界：① 分层聚合（SCN-SLA-995）；② 公平性（SCN-SLA-1000）；③ 报告（SCN-OPS-728）。

**答**：
```javascript
async function tenantSlaAggregate(month) {
  const byTier = await Promise.all(Object.keys(TENANT_TIERS).map(t =>
    tenantSlaBoard(t, month)));                        // 分层（SCN-SLA-995）
  const fairness = await tenantFairnessCheck();        // 公平性（SCN-SLA-1000）
  const report = {
    byTier, fairness,
    overall: weightedAverage(byTier, { by: 'tier', weights: TENANT_TIERS }),   // 加权
    drill: (t) => tenantDetail(t),                     // 下钻（SCN-SLA-705）
  };
  return { report, archive: archiveSlaReport(report) };   // 消费（SCN-OPS-728/248）
}
```

**评分点**:
- 分层聚合 + 加权（SCN-SLA-995）。
- 公平性（SCN-SLA-1000）。
- 消费归档（SCN-OPS-728/248）。
