---
title: "[JA-191] LangChain4j·McpToolProvider（MCP）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · McpToolProvider（MCP）

- **事实**：LC4j 的 McpToolProvider.builder().mcpClients(...) 把 MCP 工具包装为 Provider 挂给 AiServices
- **原理**：与 JA-054 联动，MCP 工具与 @Tool 工具同池，双框架均把 MCP 当一等公民
- **常见误区**：
  1. MCP 工具要先翻译成注解（错）
  2. McpToolProvider 不存在（错）
  3. 只能挂一个 MCP 客户端（错）
- **工程用法**：MCP 工具接入 LC4j
- **版本锚点**：LangChain4j 1.0
