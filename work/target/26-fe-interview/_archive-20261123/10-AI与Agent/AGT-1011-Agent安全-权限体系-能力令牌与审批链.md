---
title: [1011] Agent 的权限体系怎么设计成「能力令牌」模式
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 安全, 权限]
type: 面试题
---

## 1011：Agent 的权限体系怎么设计成「能力令牌」模式

**答**：
- 能力令牌（capability token）模式：权限不是「Agent 是谁」而是「Agent 被授予什么能力」——每个能力是签名令牌（工具、参数范围、资源范围、TTL），调用工具时验签。
- 三级审批链：低危自动放行、中危编排器规则审批（预算内自动批）、高危人工；审批记录进审计日志可回溯。
- 令牌不可转移：A Agent 的令牌 B 用不了（绑定 agentId），防止横向越权；令牌泄露影响面被 TTL 限制。
- 追问钩子：能力令牌和 OAuth scope 的区别？——scope 描述「用户授权应用什么」，能力令牌描述「编排器授权 Agent 什么」，粒度到参数级（如「只能读 /data/x 目录」）。

```ts
const cap = signJWT({ agent: 'coder-1', tool: 'fs.write',
  path_prefix: '/workspace/coder-1/', maxBytes: 100000, ttl: 600 }, K);
async function callTool(agent, tool, args) {
  const ok = verify(cap, { agentId: agent.id, tool, ...scopeCheck(args, cap) });
  if (!ok) throw new Forbidden('capability mismatch');
  if (riskOf(tool, args) === 'high') return humanApproval(args);
  return tools[tool].run(args);
}
```
