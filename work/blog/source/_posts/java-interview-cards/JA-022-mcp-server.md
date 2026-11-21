---
title: "[JA-022] MCP·mcp-server（服务端）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## MCP · mcp-server（服务端）

- **事实**：Spring AI 的 MCP 服务端 starter：spring-ai-starter-mcp-server（stdio）与 webmvc/webflux（SSE）变体
- **原理**：把本应用的 @Tool 能力暴露为 MCP 服务给其他 Agent 复用，transport 决定通信方式（本地子进程 vs 远程 HTTP）
- **常见误区**：
  1. MCP server starter 只能走 stdio（错）
  2. 暴露后其他进程无法调用（错）
  3. 服务端与客户端是同一个 starter（错）
- **工程用法**：MCP 服务提供方搭建
- **版本锚点**：Spring AI 1.0 GA
