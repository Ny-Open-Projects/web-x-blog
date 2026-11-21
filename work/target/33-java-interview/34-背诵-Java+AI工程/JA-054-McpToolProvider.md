---
title: "[JA-054] Agent·McpToolProvider（MCP 工具）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Agent · McpToolProvider（MCP 工具）

- **事实**：LangChain4j 的 McpToolProvider 把 MCP server 的工具包装为框架工具挂给 AiServices
- **原理**：MCP 工具与本地 @Tool 工具混用（同一 Agent 双来源），生态工具免重写接入，与 JA-040 联动
- **常见误区**：
  1. MCP 工具必须转成本地方法（错）
  2. McpToolProvider 是 Spring AI 类（错）
  3. MCP 工具与本地工具互斥（错）
- **工程用法**：MCP 工具接入 LC4j
- **版本锚点**：LangChain4j 1.0
