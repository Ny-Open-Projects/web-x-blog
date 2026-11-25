---
title: [SCN-1199] SCADA 大屏的权限与岗位矩阵（最小权限矩阵化）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1199：SCADA 大屏的权限与岗位矩阵（最小权限矩阵化）

**答**：
- 矩阵：岗位 × 操作权限矩阵（配置化管理），新岗位按矩阵赋权。
- 临时：临时授权（承包商限时权限，到期自动收回）。
- 回收：离职/转岗权限即时回收。

```javascript
// 权限矩阵
const PERM_MATRIX = {
  operator: ['view', 'ack', 'basic-cmd'],
  engineer: ['view', 'ack', 'basic-cmd', 'param'],
  manager: ['view', 'report'],
};
function grantByRole(user, role, { ttlMs } = {}) {
  const perms = PERM_MATRIX[role] ?? [];
  const grant = { user: user.id, perms,
    expireAt: ttlMs ? Date.now() + ttlMs : null };     // 临时授权
  return api('/auth/grant', grant);
}
```
