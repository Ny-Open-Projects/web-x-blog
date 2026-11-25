---
title: [AGT-801] 一个企业级 Agent 平台（多租户）由哪些层组成，租户隔离在哪几层做？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-801：一个企业级 Agent 平台（多租户）由哪些层组成，租户隔离在哪几层做

**答**：
- 六层：接入层（SSO/网关/限流）、编排层（Agent 运行时/会话/任务队列）、模型网关（统一多模型接入/路由/配额）、工具层（工具注册/沙箱执行/权限）、记忆与知识层（RAG/记忆，按租户分域）、治理层（审计/计费/策略/可观测）。
- 隔离必须贯穿：请求隔离（租户标签全程透传）、数据隔离（存储分租户索引）、计算隔离（沙箱按租户限额）、模型隔离（配额独立+日志隔离）。任何一层漏隔离都是事故源。
- 前端视角的核心诉求：租户配置驱动 UI（哪些 Agent/工具可见）、身份贯通（on-behalf-of 代用户执行）、审计可视。

```javascript
const PLATFORM = {
  access: ['sso', 'gateway', 'ratelimit'],
  runtime: ['agent-runtime', 'sessions', 'task-queue'],
  model: ['model-gateway', 'routing', 'quota'],
  tools: ['registry', 'sandbox', 'rbac'],
  memory: ['rag', 'profile', 'tenant-domain'],
  govern: ['audit', 'billing', 'policy', 'observability'],
};
function tenantContext(req) {
  const ctx = { tenantId: req.tenant, userId: req.user, traceId: genId() };
  if (!ctx.tenantId) throw new Error('TENANT_REQUIRED');
  return ctx;                                     // 全程透传
}
```

