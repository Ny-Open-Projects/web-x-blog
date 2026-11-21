---
title: "[JA-025] MCP·stdio（传输）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## MCP · stdio（传输）

- **事实**：MCP 传输层决定通信方式：stdio 常用于本地子进程，SSE/HTTP 用于远程服务
- **原理**：Claude Desktop 等客户端以 stdio 子进程方式拉起本地 MCP server，远程共享则用 SSE transport，选型按部署形态
- **常见误区**：
  1. MCP 只有一种传输方式（错）
  2. stdio 用于远程调用（错）
  3. transport 是可选项（错）
- **工程用法**：本地 vs 远程服务部署
- **版本锚点**：MCP 规范
