---
title: [NODE-992] 笔试题——实现 SLA 多租户分层管理（租户级 SLA 分层）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-992：手写租户分层

**需求与边界**：
- 需求：租户 SLA 分层（SCN-NODE-678/992）——① 租户级 SLA 定义（金/银/铜——SCN-OPS-714 权限联动）；② 分层容量分配（金租户高配额——SCN-NODE-678）；③ 分层的巡检（SCN-SLA-975）；④ 分层的变更（SCN-SLA-965）。
- 边界：① 分层的容量校验（SCN-NODE-699）；② 分级的权限（SCN-OPS-714）；③ 分层的通知（SCN-OPS-612）。

**答**：
```javascript
const TENANT_TIERS = {
  gold: { sla: { availability: 0.9995 }, quota: { qps: 1000 } },
  silver: { sla: { availability: 0.999 }, quota: { qps: 300 } },
  bronze: { sla: { availability: 0.995 }, quota: { qps: 50 } },
};
async function tenantTierCheck() {
  for (const [tier, cfg] of Object.entries(TENANT_TIERS)) {
    const tenants = tenantsOf(tier);
    const cap = capacityFor(tier);                     // SCN-NODE-678 分层容量
    if (tenants.length * cfg.quota.qps > cap)
      alert({ type: 'TIER_CAP_MISMATCH', tier, fix: '扩容或升配（SCN-NODE-699）' });   // SCN-SLA-975
  }
}
```

**评分点**:
- 租户分层 SLA（金/银/铜——SCN-OPS-714）。
- 分层容量校验（SCN-NODE-678/699）。
- 巡检告警（SCN-SLA-975）。
