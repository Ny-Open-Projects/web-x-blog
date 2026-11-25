---
title: [ARC-229] RBAC 的角色互斥与 SoD 如何落地？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-229：RBAC 的角色互斥与 SoD 如何落地？
**答**：
- SoD（职责分离）：出账与审批不能是同一人、创建者不能审核自己的单据。模型上分两类：**角色互斥**（不能同时持有 A、B 角色）与**动态职责分离**（同一流程节点不能由同一人先后执行）。
- 互斥落在授权侧：角色编辑器保存时校验互斥矩阵，用户被授予互斥角色时后端拒绝；前端做的是即时反馈（保存前预检）。
- 动态 SoD 落在流程侧：审批流引擎校验"当前审批人 ≠ 单据创建人/上一节点处理人"，前端在指派 UI 里直接过滤掉不合法候选人。
- 审计配套：互斥矩阵本身要版本化，调整走审批。

```typescript
// 静态互斥矩阵
const mutex: [string, string][] = [['finance:pay', 'finance:audit'], ['proc:create', 'proc:approve']];
function assertGrant(user, newRole) {
  const clash = mutex.find(([a, b]) =>
    (user.roles.includes(a) && newRole === b) || (user.roles.includes(b) && newRole === a));
  if (clash) throw new PermError(`角色互斥：${newRole} 与 ${user.roles.find(r => clash.includes(r))} 冲突`);
}
// 动态 SoD：审批人候选过滤
const candidates = deptUsers.filter(u =>
  u.id !== order.createdBy && u.id !== flow.prevNodeId);   // 创建者与上节点处理人不可审
// 前端预检只是体验，后端流程引擎同样校验（防绕过）
```
