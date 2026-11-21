---
title: [ARC-068] RBAC 模型在前端如何落地（表设计 + 路由生成）？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-068：RBAC 模型在前端如何落地（表设计 + 路由生成）？
**答**：
- 模型：用户 → 角色 → 权限（permission = 资源 + 操作），前端只持有"权限码集合"，路由表按权限码过滤生成。
- 铁律：前端权限只是体验优化（隐藏不可用入口），授权判断必须在服务端复核。
- 动态路由：登录后拉权限码，用 meta.code 匹配生成可访问路由，未授权路由 404/403。

```typescript
// 服务端返回的权限码（前端不存角色关系表，只拿结果）
type Permission = string; // 'order:list' | 'order:refund' | 'stock:write'
const permissions: Permission[] = await api.get('/me/permissions'); // ['order:list','order:refund']

// 路由表：声明式挂权限码
const routes: AppRoute[] = [
  { path: '/orders', component: OrderList, meta: { code: 'order:list', title: '订单管理' } },
  { path: '/orders/:id/refund', component: Refund, meta: { code: 'order:refund' } },
  { path: '/stock', component: Stock, meta: { code: 'stock:write' } },
];

// 按权限生成可访问路由
function buildAccessibleRoutes(all: AppRoute[], perms: Permission[]): AppRoute[] {
  return all.filter(r => !r.meta.code || perms.includes(r.meta.code));
}

// 服务端模型参考（前端要懂的结构）：
// users(id) ── user_roles ── roles(id) ── role_permissions ── permissions(resource, action)
// permissions: { resource: 'order', action: 'refund' } → code = 'order:refund'
```
