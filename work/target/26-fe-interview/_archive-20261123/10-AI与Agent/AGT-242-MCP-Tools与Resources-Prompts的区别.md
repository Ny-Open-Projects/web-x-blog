---
title: [AGT-242] MCP 的 Tools/Resources/Prompts 三原语——分别怎么用？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-242：MCP 的三类原语 Tools/Resources/Prompts 怎么区分与使用？

**答**:
- Tools（模型控制）：描述给 LLM，由模型决定何时调用（如"创建工单""执行查询"）——有副作用或需模型决策的动作走 Tools，定义含名称/描述/JSON Schema 参数，描述质量直接决定模型调用准确率。
- Resources（应用控制）：由应用侧决定读取的上下文数据（文件/数据库记录/API 文档），URI 寻址（`file:///a.md`、`db://orders/schema`），只读为主——应用把相关资源注入上下文，模型不直接"调用"资源。
- Prompts（用户控制）：Server 预置的提示模板，用户主动选用（斜杠命令），参数化填充——把领域最佳实践封装成模板复用。
- 判断口诀：谁发起？模型发起=Tool，应用发起=Resource，用户发起=Prompt；同一个能力的两种包装（"查订单"做成 Tool 让模型按需调，或做成 Resource 让应用预取注入）取决于调用时机是否可预测。

```javascript
// MCP Server 定义三原语
server.tool('createTicket', { title: z.string(),
  priority: z.enum(['P0','P1','P2']) },
  async ({ title, priority }) => ({
    content: [{ type: 'text',
      text: await tickets.create({ title, priority }) }],
  }));
server.resource('order-schema', 'db://orders/schema',
  async () => ({ contents: [{ uri: 'db://orders/schema',
    text: await db.getSchema('orders') }] }));   // 应用预取
server.prompt('triage', { issue: z.string() },
  ({ issue }) => ({ messages: [{ role: 'user',
    content: `按 SOP 分诊此问题：${issue}` }] }));
```
