---
title: "[JA-026] MCP·tools/call（工具）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## MCP · tools/call（工具）

- **事实**：MCP 工具调用链路：client.listTools() 发现工具描述，client.callTool(...) 执行并取结果
- **原理**：工具描述含名称/说明/inputSchema（JSON Schema），schema 描述决定模型能否正确填参
- **常见误区**：
  1. callTool 会自动发现工具（错）
  2. 工具描述不影响模型填参（错）
  3. schema 是可选装饰（错）
- **工程用法**：MCP 工具排障
- **版本锚点**：MCP Java SDK
