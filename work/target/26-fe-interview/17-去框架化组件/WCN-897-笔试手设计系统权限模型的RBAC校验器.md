---
title: [WCN-897] 笔试：手写设计系统「权限模型」的 RBAC 校验器（含四眼原则）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-897：笔试：手写设计系统「权限模型」的 RBAC 校验器（含四眼原则）

**题目**：实现 `createRBAC(config)` 权限校验器。config 形如 `{ roles: { role: ['perm1', ...] }, ownerOf: { component: [owners] }, emergencyDisabled: string[] }`。返回 `{ assign(user, roles), can(user, perm, resource?), requireReviewer(user, author, action), setEmergency(bool) }`。要求：① `assign` 给用户分配角色（数组）；② `can(user, perm, resource)` —— 用户任一角色含该 perm 或含 `*` 则允许；若 perm 是 `publish`/`deprecate` 且 resource 是某组件，则用户还必须是该组件 owner（`ownerOf`）——即「发布者还需是 owner」的双重条件；③ `requireReviewer(user, author, action)` 实现四眼原则——用户有 `review` 权限且 user !== author 才允许审核；④ `emergencyDisabled` 中的权限在紧急模式下被禁用；⑤ `setEmergency(bool)` 切换。边界：未知用户/角色返回 false；`*` 通配；紧急模式只禁用配置列表中的权限。

**答**：

```javascript
function createRBAC(config) {
  const { roles = {}, ownerOf = {}, emergencyDisabled = [] } = config;
  const users = new Map(); let emergency = false;
  return {
    assign(user, rs) { users.set(user, Array.isArray(rs) ? rs : [rs]); },
    can(user, perm, resource) {
      const rs = users.get(user) || [];
      const perms = rs.flatMap(r => roles[r] || []);
      if (!perms.includes('*') && !perms.includes(perm)) return false;
      if (emergency && emergencyDisabled.includes(perm)) return false; // 紧急禁用
      if ((perm === 'publish' || perm === 'deprecate') && resource) {
        return (ownerOf[resource] || []).includes(user);              // 双重条件：还需是 owner
      }
      return true;
    },
    requireReviewer(user, author, action) {
      if (user === author) return false;                              // 四眼原则
      return this.can(user, 'review');
    },
    setEmergency(v) { emergency = !!v; },
  };
}
const rbac = createRBAC({
  roles: { dev: ['submit'], lead: ['submit', 'review', 'publish', 'deprecate'], admin: ['*'] },
  ownerOf: { 'ds-button': ['alice'] },
  emergencyDisabled: ['deprecate'],
});
rbac.assign('alice', ['lead']); rbac.assign('bob', ['dev']);
console.log(rbac.can('alice', 'publish', 'ds-button')); // true（lead + owner）
console.log(rbac.can('bob', 'publish', 'ds-button'));   // false（无 publish 权限）
console.log(rbac.requireReviewer('alice', 'alice', 'review')); // false（不能审自己）
rbac.setEmergency(true);
console.log(rbac.can('alice', 'deprecate', 'ds-button')); // false（紧急禁用）
```

**评分点**：
- 角色并集 + `*` 通配的权限判定正确（RBAC 基础）。
- 敏感操作（publish/deprecate）叠加 owner 双重校验（细粒度授权）。
- 四眼原则（不能审自己）+ 紧急模式禁用配置（治理与安全）。
- 未知用户/角色返回 false（`this.can` 在 requireReviewer 中正确调用），边界安全。
