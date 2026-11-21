---
title: "[JA-141] MCP·McpAsyncServer（异步）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## MCP · McpAsyncServer（异步）

- **事实**：MCP Java SDK 提供同步与异步两套 API：McpAsyncServer/McpAsyncClient（CompletableFuture 风格）
- **原理**：同步版易用阻塞线程池，异步版高吞吐低占用，按并发规模选型，与并发工程知识联动
- **常见误区**：
  1. SDK 只有同步 API（错）
  2. 异步版返回阻塞结果（错）
  3. 两套 API 不能共存（错）
- **工程用法**：并发模型选型
- **版本锚点**：MCP Java SDK
