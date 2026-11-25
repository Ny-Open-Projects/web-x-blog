---
title: [ARC-222] 多租户 SaaS 的 RBAC 权限模型如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-222：多租户 SaaS 的 RBAC 权限模型如何设计？
**答**：
- 核心隔离：权限体系按租户分域——用户-角色绑定关系、角色定义都是 tenant 内资源；同一个用户在不同租户可以是完全不同的角色。
- 三层角色：系统角色（平台管理员）、租户预置角色（租户开通自带的 Owner/Admin/Member）、租户自定义角色（基于权限码自由组装）。权限码全平台统一注册，角色只是租户内的"权限码组合"。
- 前端架构：路由/菜单/按钮按"当前租户上下文"渲染，切换租户 = 重新拉取权限快照（不做本地缓存复用）；权限快照版本随租户 token 走。
- 升级路径：套餐（Plan）限定权限码可用上限——自定义角色不能包含未购买套餐的权限码，前端在角色编辑器里把不可用码置灰。

```typescript
// 权限快照（切租户即换快照）
interface PermSnapshot {
  tenantId: string;
  role: string;
  perms: string[];            // 生效权限码，已按套餐过滤
  planLimits: { maxRoles: number };
}
function buildSnapshot(userId: string, tenantId: string): PermSnapshot {
  const binding = getBinding(userId, tenantId);            // tenant 内绑定
  const perms = resolvePerms(binding.role)                 // 角色 → 权限码
    .filter(p => planHasPerm(tenantPlan(tenantId), p));    // 套餐上限过滤
  return { tenantId, role: binding.role, perms, planLimits: plan(tenantId).limits };
}
// 切换租户：switchTenant(id) → 重新换取快照 → 重载路由表，绝不清缓存复用上一个租户的 perms
```
