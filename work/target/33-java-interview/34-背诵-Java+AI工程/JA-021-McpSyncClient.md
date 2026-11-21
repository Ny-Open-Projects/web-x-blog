---
title: "[JA-021] MCP·McpSyncClient（客户端）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## MCP · McpSyncClient（客户端）

- **事实**：Spring AI 的 MCP 客户端：starter 引入后自动装配 McpSyncClient，可 listTools 发现工具
- **原理**：客户端连接 MCP server 后工具自动进入生态（可被 ChatClient 调用），发现与调用是两个显式动作
- **常见误区**：
  1. McpSyncClient 需要手动 new（错）
  2. listTools 直接执行工具（错）
  3. 客户端与服务端同进程（错）
- **工程用法**：接入外部工具生态
- **版本锚点**：Spring AI 1.0 GA
