---
title: [NODE-994] 笔试题——实现租户容量弹性联动（金租户优先扩容）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-994：手写弹性联动

**需求与边界**：
- 需求：租户弹性（SCN-NODE-994/678）——① 租户等级驱动的扩容优先级（金租户优先——SCN-OPS-891）；② 扩容的配额分配（SCN-NODE-678 分层）；③ 扩容的全局校验（SCN-NODE-699）；④ 弹性的审计（SCN-OPS-273）。
- 边界：① 优先级的公平（SCN-OPS-891）；② 扩容的下游（SCN-NODE-699）；③ 弹性的监控（SCN-NODE-834）。

**答**：
```javascript
async function tenantElasticScale(event) {
  const tenants = affectedTenants(event).sort(byTier);   // 金租户优先（SCN-OPS-891）
  for (const t of tenants) {
    const cap = downstreamSafeMax();                   // 全局校验（SCN-NODE-699）
    if (!cap) { alert({ type: 'SCALE_CAP' }); break; }
    await scaleFor(t, { by: TENANT_TIERS[t.tier].quota.qps * 0.2 });   // 分层配额（SCN-NODE-678）
    audit({ scaled: t.id, tier: t.tier });             // 审计（SCN-OPS-273）
  }
}
```

**评分点**:
- 金租户优先（SCN-OPS-891）。
- 分层配额 + 全局校验（SCN-NODE-678/699）。
- 审计（SCN-OPS-273）。
