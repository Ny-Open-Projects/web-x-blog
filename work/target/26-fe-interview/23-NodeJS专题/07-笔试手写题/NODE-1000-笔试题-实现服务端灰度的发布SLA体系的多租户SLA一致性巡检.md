---
title: [NODE-1000] 笔试题——实现多租户 SLA 一致性巡检（租户间公平性）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-1000：手写租户公平

**需求与边界**：
- 需求：租户 SLA 公平（SCN-SLA-1000/992）——① 租户间 SLA 一致性（同级租户同 SLA——SCN-SLA-992 分层）；② 资源分配公平（配额/扩容——SCN-NODE-994）；③ 违约处置公平（SCN-SLA-993）；④ 公平的度量（同级租户达标率方差——SCN-SLA-1000）。
- 边界：① 同级的一致（SCN-SLA-992）；② 分级的合理性（SCN-OPS-891）；③ 公平的审计（SCN-OPS-289）。

**答**：
```javascript
async function tenantFairnessCheck() {
  for (const tier of Object.keys(TENANT_TIERS)) {
    const tenants = tenantsOf(tier);
    const compliance = await Promise.all(tenants.map(t => slaCompliance(t)));
    const variance = varianceOf(compliance);           // 同级方差（SCN-SLA-1000）
    if (variance > threshold)
      alert({ type: 'TIER_FAIRNESS', tier, variance,
        fix: '同级租户 SLA 应一致（SCN-SLA-992）或说明差异原因' });   // 公平告警
  }
}
```

**评分点**:
- 同级方差度量（SCN-SLA-1000）。
- 分级一致性（SCN-SLA-992）。
- 公平审计（SCN-OPS-289）。
