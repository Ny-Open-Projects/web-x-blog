---
title: "[JA-091] MCP·initialize（客户端）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## MCP · initialize（客户端）

- **事实**：MCP 客户端使用前必须 initialize（协议握手：版本与能力协商），Java SDK 的 McpSyncClient 显式调用
- **原理**：握手失败即后续不可用，initialize 是协议强制步骤不是可选配置，排障先查握手
- **常见误区**：
  1. 客户端开箱即用无需握手（错）
  2. initialize 可跳过（错）
  3. 握手只发生在服务端（错）
- **工程用法**：MCP 连接排障
- **版本锚点**：MCP 规范
