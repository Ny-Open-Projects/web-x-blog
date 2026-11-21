---
title: [ARC-070] ABAC 与数据权限是什么概念？前端有何体现？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-070：ABAC 与数据权限是什么概念？前端有何体现？
**答**：
- RBAC 回答"什么角色能做什么操作"，ABAC 回答"满足什么属性条件才能操作"（属主、部门、金额阈值、时间窗），即数据级权限。
- 前端体现：列表按数据可见范围过滤的提示、行内按钮的可用性（不是所有行都能编辑）、表单字段按上下文禁用。
- 架构要求：条件计算规则收敛为策略表达式，前端渲染策略下发结果，不硬编码 if。

```typescript
// 服务端下发的策略（属性条件），前端只消费结果与解释
interface Policy {
  resource: 'order';
  action: 'edit';
  condition: {                       // ABAC 条件：属主或同部门 + 金额上限
    anyOf: [
      { field: 'order.ownerId', op: 'eq', valueFrom: 'session.userId' },
      { field: 'order.deptId', op: 'eq', valueFrom: 'session.deptId' },
    ],
    allOf: [{ field: 'order.amount', op: 'lte', value: 100000 }],
  };
}

// 前端把策略结果渲染为行级 UI，而不是自己写 if
function rowActions(order: Order, check: (p: Policy, ctx: Ctx) => boolean, session: Session) {
  const editable = check(policies.orderEdit, { order, session });
  return editable ? [<EditButton key="e" />] : [<ReadonlyTag key="r" text="仅查看（超限或非本部门）" />];
}
// 要点：check 逻辑与后端共享同一份策略求值器（同构），避免两端规则漂移
```
