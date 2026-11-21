---
title: [NODE-361] Node 服务的鉴权中间件与权限模型如何统一实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-361：鉴权中间件与权限模型统一实现
**答**:
- 三步分离：认证（是谁：JWT/session 校验，中间件产出 ctx.user）→ 授权（能做什么：RBAC/ABAC 判定）→ 审计（做了什么：敏感操作记录）。鉴权中间件只做认证+注入，授权声明在路由级。
- 授权声明式：路由元数据（require: 'order:read'，scope: 'own'）+ 统一判定函数 can(user, perm, resource)；行级权限（只能看自己的单）通过 resource.ownerId 比较或 scope 注入查询条件（service 层强制 where userId）。
- 数据权限强制点：权限判定必须"查询条件注入"而非"查出来再过滤"（后过滤会漏分页/聚合）；服务端永远最终裁决（前端显隐只是 UI，ARC-420）。
- 批量接口的权限：批量查询按用户可见集过滤，防"越权枚举 ID"（IDOR）；响应中不暴露无权字段。
- 缓存注意：权限快照缓存 TTL 短或变更失效（ARC-230）；越权尝试进风控埋点。
```javascript
// 路由级声明 + 查询注入
const requirePerm = (perm) => async (ctx, next) => {
  if (!await can(ctx.user, perm)) throw new Forbidden(perm);
  await next();
};
router.get('/orders', requirePerm('order:read'), async (ctx) => {
  ctx.body = await svc.listOrders({ ...ctx.query, ownerId: ctx.user.id }); // 行级条件强制注入
});
```
