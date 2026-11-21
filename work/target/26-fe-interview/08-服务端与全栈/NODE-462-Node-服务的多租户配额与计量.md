---
title: [NODE-462] Node 服务多租户的配额与计量（租户级限制）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-462：多租户配额与计量
**答**:
- 双层配额：租户级（套餐决定：请求数/存储/成员数/功能开通）+ 用户级（租户内个人配额）；计费维度按租户聚合（NODE-401）。
- 配额执行：请求配额在网关/BFF 层（租户 ID 维度令牌桶，NODE-360）、存储配额在写入层（上传前预检 + 后核——超配额拒绝并提示）、功能配额（开通校验中间件：feature + plan 矩阵）。
- 超配额体验：明确引导（升级页面/联系销售）而非生硬报错；接近配额预警（80% 通知管理员 ARC-439）；临时扩容（大客户活动期手动提额，有时限）。
- 公平性：大租户高负载不影响小租户（租户级限流天然隔离 NODE-395 + 资源池隔离：重租户迁移独立部署）。
- 计量口径：配额消耗计量与计费计量同源（同一事件流两消费方——防"配额算的"与"账单算的"不一致对账灾难）。
```javascript
// 租户配额中间件
function tenantQuota(kind, cost = 1) {
  return async (ctx, next) => {
    const t = ctx.state.tenant;
    const plan = await plans.of(t);                              // 套餐配额
    if (!(await luaDecr(`tq:${t.id}:${kind}:${period()}`, cost)))
      return ctx.throw(429, { code: 'QUOTA_EXCEEDED',
        detail: { used: plan[kind], upgrade: `/billing/${t.id}` } });  // 引导升级
    return next();
  };
}
```
