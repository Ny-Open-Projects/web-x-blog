---
title: "[JA-023] MCP·io.modelcontextprotocol（SDK）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## MCP · io.modelcontextprotocol（SDK）

- **事实**：MCP Java SDK 的 Maven 坐标是 io.modelcontextprotocol.sdk:mcp，Spring AI 的 MCP starter 是其封装
- **原理**：理解层次：SDK 提供 McpServer/McpClient 核心，Spring AI starter 负责自动装配，SDK 可脱离 Spring 使用
- **常见误区**：
  1. MCP Java SDK 是 Spring 自研私有协议（错）
  2. SDK 不能脱离 Spring 使用（错）
  3. 坐标是 org.springframework.ai:mcp-core（错）
- **工程用法**：非 Spring 应用接 MCP
- **版本锚点**：MCP Java SDK
