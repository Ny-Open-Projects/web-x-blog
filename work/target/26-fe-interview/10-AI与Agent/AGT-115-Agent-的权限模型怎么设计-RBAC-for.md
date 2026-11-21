---
title: [AGT-115] Agent 的权限模型怎么设计（RBAC for tools）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-115：Agent 的权限模型怎么设计（RBAC for tools）？
**答**：
- RBAC 三件套：角色（role）→ 权限（工具 × 动作级别 read/write/admin）→ 主体（用户/Agent）；Agent 继承发起用户的权限，不高于人。
- 权限粒度三层：工具级（能否调用）、动作级（read/write/admin）、数据级（只能查自己部门的工单，行级校验）。
- 执行层强制：未授权工具根本不进注册表——LLM 的 tools 列表里看不到、调用也无路由；提示词约束可被注入绕过，代码约束不能。
- 权限变更即时生效：每次 Agent 循环用最新角色构建注册表；降权后进行中会话的下一次调用即被拒，并留审计。

```typescript
import { z } from 'zod';

// RBAC for tools：注册表层强制校验
type Action = 'read' | 'write' | 'admin';
interface ToolPerm { tool: string; action: Action }

const ROLES: Record<string, ToolPerm[]> = {
  viewer: [
    { tool: 'search_docs', action: 'read' },
    { tool: 'get_order', action: 'read' },
  ],
  operator: [
    { tool: 'search_docs', action: 'read' },
    { tool: 'get_order', action: 'read' },
    { tool: 'create_ticket', action: 'write' },
  ],
  admin: [{ tool: '*', action: 'admin' }],          // 通配：完整权限
};

// 关键：权限不足的工具根本不进注册表 —— LLM 的 tools 列表里看不到，调用也无路由
function createScopedRegistry(roleName: string, toolImpls: Map<string, unknown>): ToolRegistry {
  const perms = ROLES[roleName] ?? [];
  const reg = new ToolRegistry();
  for (const [name, impl] of toolImpls) {
    if (perms.some((p) => p.tool === '*' || p.tool === name)) reg.register('builtin', name, impl as any);
  }
  return reg;
}

// 数据级权限：工具实现内部按主体二次校验（行级）
const get_order = defineTool({
  name: 'get_order',
  description: '查询订单，仅限本部门',
  schema: z.object({ orderId: z.string() }),
  run: async ({ orderId }) => {
    const order = await db.getOrder(orderId);
    const ctx = currentExecContext();               // 发起用户与角色由运行时注入
    if (order.deptId !== ctx.user.deptId && ctx.role !== 'admin') throw new Error('无权访问该订单');
    return order;
  },
});
// 底线：Agent 权限不高于发起用户；权限变更即时生效并留审计
```
