---
title: [SCN-1159] SCADA 大屏的权限与操作审计（双人复核）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1159：SCADA 大屏的权限与操作审计（双人复核）

**答**：
- 权限：查看/操作/组态分级；关键操作（阀门开关/参数修改）双人复核（第二人授权）。
- 审计：所有操作留痕（who/when/what/before/after），不可篡改日志。
- 应急：单人夜班场景的应急操作流程（特殊授权记录）。

```javascript
// 双人复核
async function criticalOperation(op, operator, reviewer) {
  const request = await api('/op/request', { op, operator });
  const approved = await api('/op/approve',
    { requestId: request.id, reviewer });              // 第二人授权
  if (!approved.ok) return { ok: false, reason: '复核未通过' };
  auditLog({ type: 'critical-op', op, operator, reviewer,
    before: op.beforeValue, after: op.afterValue });
  return execute(op);
}
async function execute(op) { return { ok: true }; }
```
