---
title: "[JA-040] 选型·langchain4j-mcp（MCP 共存）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 选型 · langchain4j-mcp（MCP 共存）

- **事实**：两个框架都能接 MCP：Spring AI 有 mcp starter，LangChain4j 有 langchain4j-mcp 模块（McpToolProvider）
- **原理**：MCP 是传输与生态协议层（AI-018），框架只是客户端实现方，工具生态跨框架复用
- **常见误区**：
  1. MCP 只支持一个框架（错）
  2. 两框架接 MCP 要重写工具（错）
  3. McpToolProvider 是 Spring AI 的类（错）
- **工程用法**：MCP 生态复用
- **版本锚点**：LangChain4j 1.0
