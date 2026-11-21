---
title: [AGT-243] MCP 传输层——stdio 与 Streamable HTTP 怎么选？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-243：MCP 的两种传输方式怎么选——本地 stdio 与远程 HTTP？

**答**:
- stdio（本地）：Host 以子进程方式启动 Server，通过标准输入输出通信——零网络开销、天然同机权限、简单可靠；适合个人工具（本地文件/终端/IDE 集成）；缺点是无法共享（每用户一份进程）。
- Streamable HTTP（远程）：Server 独立部署为 HTTP 服务，支持流式响应（SSE）与会话管理，可多用户共享、可水平扩展、可统一鉴权审计；适合团队级/企业级工具（内部 API 网关型 Server）。
- 选型判据：单机个人用 → stdio；多人共享/需要集中管控（鉴权/审计/限流）→ 远程 HTTP；从 stdio 起步的工具成熟后"上云"是常见演进路径（协议层不变，只换传输）。
- 远程部署的额外工程：会话粘性（有状态会话路由到同实例或状态外置）、断线重连与 Last-Event-ID 续传、鉴权（OAuth/OIDC）——stdio 时不存在的问题在远程都要补。

```text
MCP 传输选型：
stdio：本地子进程 / 个人工具 / 同机权限
  / 零部署，但每用户一份、不可共享
Streamable HTTP：独立部署 / 多用户共享
  / 集中鉴权审计限流 / 可扩展
  附加工程：会话粘性 / SSE 重连续传 /
  OAuth 鉴权
演进：stdio 起步 → 成熟后上远程，
  协议层不变只换传输。
```
