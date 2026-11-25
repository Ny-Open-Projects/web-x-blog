---
title: [1180] MCP（工具协议）和 A2A（Agent 间协议）各解决什么问题
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 协议]
type: 面试题
---

## 1180：MCP（工具协议）和 A2A（Agent 间协议）各解决什么问题

**答**：
- MCP 解决「Agent ↔ 工具/资源」：统一工具发现、调用、资源读取的协议——Agent 不为每个工具写集成；解决的是 N×M 集成问题。
- A2A 解决「Agent ↔ Agent」：跨 Agent 的任务委托、状态查询、产物交换——Agent 之间是「对等协作」而非「主从调用工具」；解决的是协作语义（任务书、进度、产物）标准化。
- 分层关系：Agent 用 MCP 接工具、用 A2A 找同伴——两层互补不替代；自研编排时对应的就是「工具层协议」与「协作层协议」的分离。
- 落地建议：MCP 生态成熟可优先采用（工具接入标准化收益立现）；A2A 在跨团队场景有价值，单团队内部先用简单内部协议，避免过早标准化。
- 追问钩子：什么信号说明该引入标准协议了？——工具集成代码占总代码比例失控（>30%）、跨团队 Agent 调用开始出现（协议各自发明对不上）。

```ts
// 分层架构示意
const stack = {
  toolLayer: mcpClient({ servers: ['fs', 'search', 'db'] }),     // Agent->工具
  collabLayer: a2aClient({ directory, auth: 'capability' }),     // Agent->Agent
};
// 编排器按层调用，不直连任何具体工具/Agent
```
