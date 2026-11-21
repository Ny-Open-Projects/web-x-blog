---
title: [AGT-113] Agent 平台化怎么设计（多 Agent 托管 / 监控 / 计费），MCP 服务市场如何做（发现 / 安装 / 权限）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-113：Agent 平台化怎么设计（多 Agent 托管 / 监控 / 计费），MCP 服务市场如何做（发现 / 安装 / 权限）？
**答**：
- 平台三要素：托管（Agent 用 manifest 声明模型/工具权限/触发方式/预算，运行时按 manifest 装配）、监控（每次执行的 trace 与成本落库）、计费（按 token 与调用次数计量）。
- MCP 市场核心流程：注册中心提供搜索/评分/版本管理；安装 = 拉取 manifest → 安装前明示所需权限 → 用户授权 → 注册进运行时。
- 权限沙箱：市场工具默认最小权限（只读），写权限单独勾选；运行时按 manifest 校验调用，越权直接拒绝（复用 AGT-115）。
- 多 Agent 隔离：每个 Agent 独立会话存储与工具注册表，共享网关的限流、审计与计费。

```yaml
# agent manifest —— 平台托管的最小声明
name: weekly-report-agent
version: 1.2.0
model: gpt-4o-mini
triggers:
  - type: schedule
    cron: "0 9 * * 1"          # 每周一 9 点
  - type: chat
tools:
  - ref: mcp:github@2.1/search_issues
    permission: read
  - ref: builtin/send_email
    permission: write           # 写权限需在市场安装页明示并由用户勾选
budget:
  maxCostPerRunCents: 50
```

```typescript
// 平台运行时：按 manifest 校验权限并计量
class AgentRuntime {
  async invoke(agent: AgentManifest, input: unknown) {
    const trace = startTrace(agent.name);
    const runtime = new ToolRegistry();
    for (const t of agent.tools) {
      runtime.register(...resolveTool(t.ref, t.permission)); // 按 manifest 装配工具，未授权不进注册表
    }
    try {
      const result = await runAgentLoop({
        messages: [toUserMessage(input)],
        tools: runtime,
        budget: agent.budget,          // 预算控制（AGT-069）
      });
      metering.bill(agent.name, trace.usage); // 计费：按 token 与调用次数
      return result;
    } finally {
      trace.end();                   // trace 与成本落库，接入监控看板
    }
  }
}
```
