---
title: [NODE-038] 如何封装一个 RBAC（基于角色的访问控制）鉴权中间件？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-038：如何封装一个 RBAC（基于角色的访问控制）鉴权中间件？
**答**：
- 模型：**user → roles → permissions**（permission 形如 `order:read`/`order:write`）。中间件声明式标注所需权限：`router.get('/orders', requirePermission('order:read'), handler)`。
- 实现要点：JWT claims 中只放 roles（体积小），permission 由服务端从角色映射表解析（支持热更新无需重签 token）；层级继承（admin ⊃ editor ⊃ viewer）用 Set 归并；无权限统一 403 并打审计日志。
- 对比 ACL（资源级）与 ABAC（属性级）：RBAC 覆盖 80% 后台场景，资源级校验（"你只能改自己的订单"）另在 service 层做 ownership 判断。

```javascript
// 权限映射：角色 → 权限集合（可放配置中心/DB 热更新）
const ROLE_PERMISSIONS = {
  admin: ['order:read', 'order:write', 'user:manage'],
  editor: ['order:read', 'order:write'],
  viewer: ['order:read'],
};
// 层级归并
const flatten = (roles) => [...new Set(roles.flatMap((r) => ROLE_PERMISSIONS[r] || []))];

const requirePermission = (need) => async (ctx, next) => {
  const claims = ctx.state.user; // 前置 auth 中间件已验签
  if (!claims) ctx.throw(401, '未登录');
  const owned = flatten(claims.roles || []);
  if (!owned.includes(need)) {
    // 审计日志：谁在何时越权访问了什么
    console.warn(JSON.stringify({ level: 'warn', event: 'rbac_denied',
      uid: claims.uid, roles: claims.roles, need, path: ctx.path }));
    ctx.throw(403, `需要权限 ${need}`);
  }
  await next();
};

// 路由挂载
router.get('/orders', requirePermission('order:read'), listOrders);
router.post('/orders', requirePermission('order:write'), createOrder);
router.delete('/users/:id', requirePermission('user:manage'), deleteUser);

// service 层的资源级 ownership 校验（RBAC 之外的第二道门）
async function updateOrder(uid, orderId, patch) {
  const order = await db.orders.find(orderId);
  if (order.ownerId !== uid && !flatten(user.roles).includes('order:write:all')) {
    throw new BizError('ORDER_FORBIDDEN', '只能修改自己的订单', 403);
  }
  return db.orders.update(orderId, patch);
}
```

---

## 六、数据层
