---
title: [AIC-086] Agent 的权限审计怎么做？「它到底能干什么」这个问题怎么回答清楚？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-086：Agent 的权限审计怎么做？「它到底能干什么」这个问题怎么回答清楚？
**答**：
- 权限建模：把 agent 能力拆成「工具 × 资源 × 动作」三元组清单（如 filesystem×src×rw、terminal×白名单命令×exec、mcp×schema.read×r），每个 agent 实例的权限集显式配置，不靠默认。
- 审计三件事：静态（配置里声明的权限集 vs 实际需要，最小化）、动态（运行时每次越权尝试都记录并告警）、定期（权限集与团队现状对齐，删掉没人用的）。
- 「能干什么」的可视化：生成权限说明书（人类可读）放在 agent 配置旁边，接入新工具时 PR 必须更新该文档——审计从「考古」变「读文档」。
- 与 AIC-009 的关系：命令白名单是权限审计的一个特例；完整审计还包括文件写入范围、网络访问域、数据读取级别。
- 追问钩子：高危动作（删库、发布、改生产配置）无论多麻烦都走「人工二次确认」，这条没有商量余地。

```javascript
// 权限三元组模型 + 动态审计
const perms = [
  { tool: 'filesystem', resource: 'src/**', action: 'rw' },
  { tool: 'terminal', resource: /npm (test|lint|run build)/, action: 'exec' },
  { tool: 'terminal', resource: /.*/, action: 'exec', denied: true },
];
function audit(toolCall, traceId) {
  const allowed = perms.some(p => !p.denied && p.tool === toolCall.tool &&
    matches(p.resource, toolCall.resource) && p.action === toolCall.action);
  if (!allowed) auditLog.warn({ traceId, ...toolCall, verdict: 'DENIED' }); // 越权尝试留痕
  return allowed;
}
```
