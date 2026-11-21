---
title: [AGT-248] MCP Resources 与 Prompts 的实战用法——不只是工具？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-248：MCP 的 Resources 和 Prompts 在生产里怎么用出价值？

**答**:
- Resources 的典型用法一：文档即资源——内部系统把 API 文档/数据字典/Runbook 暴露为 Resources（`doc://api/orders`），Host 按需读取注入上下文，替代"把文档贴进 prompt"的手工操作；配合资源模板（`db://orders/schema/{table}`）支持参数化读取。
- Resources 用法二：动态上下文订阅——资源支持变更通知（subscribe），文件/数据变化时 Host 自动刷新注入，保证上下文新鲜（AGT-215 新鲜度问题的协议层解法）。
- Prompts 的典型用法：领域 SOP 模板化——"故障排查""代码审查""周报生成"封装成参数化 Prompt，用户 `/triage INC-123` 一键调起；组织级 prompt 资产通过 MCP 分发，比复制粘贴规范文档可靠得多。
- 组合拳：Prompt 模板内引导模型使用同 Server 的 Tools 与 Resources——一个领域 Server（工具+文档+模板）构成完整的能力包，这是 MCP Server 产品化的形态。

```javascript
// 资源模板 + 订阅
server.resource('table-schema', 'db://schema/{table}',
  async ({ table }) => ({ contents: [{ uri: `db://schema/${table}`,
    text: await db.describe(table) }] }));
server.onResourceChanged('db://schema/orders',
  () => host.refreshContext());            // 变更推送
// Prompt：领域 SOP 一键调起
server.prompt('triage', { incident: z.string() },
  ({ incident }) => ({ messages: [{ role: 'user',
    content: `用 searchRunbook 工具查询相关预案，
      按 SOP-7 分诊：${incident}` }] }));    // Prompt 引导用 Tool
```
