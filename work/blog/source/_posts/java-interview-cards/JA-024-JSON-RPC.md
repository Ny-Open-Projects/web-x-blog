---
title: "[JA-024] MCP·JSON-RPC（协议）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## MCP · JSON-RPC（协议）

- **事实**：MCP 协议构建在 JSON-RPC 2.0 之上（initialize/tools/list/tools/call 等方法）
- **原理**：协议层标准化让任何语言的客户端服务端互通，Java SDK 只是协议的一种实现
- **常见误区**：
  1. MCP 是 Java 专有协议（错）
  2. MCP 用 REST 通信（错）
  3. 协议方法名可以随意自定义（错）
- **工程用法**：协议本质理解
- **版本锚点**：MCP 规范
