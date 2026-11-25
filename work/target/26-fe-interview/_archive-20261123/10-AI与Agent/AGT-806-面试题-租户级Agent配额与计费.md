---
title: [AGT-806] 平台对租户的配额（调用数/token/工具次数）与计费模型怎么设计？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-806：平台对租户的配额（调用数/token/工具次数）与计费模型怎么设计

**答**：
- 配额三层：月度包（合同量）、突发上限（防单租户打爆共享资源）、单任务上限（防死循环）。配额扣减实时（Redis 原子操作），日终对账。
- 计费模型：按实际用量（token+工具调用+存储）分项计价，套餐折扣在出账层算；成本明细按任务/Agent/工具维度可查（租户自助账单）。
- 超额策略可配：硬停（合同约定）/软限（降速+通知）/超量计费；策略执行在网关（拒绝)与运行时（任务暂停）两层。

```javascript
async function checkQuota(tenant, est) {
  const q = await redis.hgetall(`quota:${tenant}`);
  if (q.month + est.tokens > q.monthLimit)
    return policy.onExceed(tenant);               // 硬停/软限/超量
  if (q.burst + est.tokens > q.burstLimit)
    return throttle(tenant);
  await redis.hincrby(`quota:${tenant}`, 'month', est.tokens); // 原子扣减
  return { ok: true };
}
```

