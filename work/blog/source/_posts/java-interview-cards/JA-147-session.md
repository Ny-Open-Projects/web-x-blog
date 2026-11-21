---
title: "[JA-147] MCP·session（会话）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## MCP · session（会话）

- **事实**：MCP 的 HTTP 传输带会话管理（会话 id 维持多轮通信状态）
- **原理**：有状态会话支持断线重连与上下文保持，负载均衡需会话亲和或无状态化设计，与网关知识联动
- **常见误区**：
  1. MCP 全部无状态（错）
  2. 会话 id 是随机装饰（错）
  3. 负载均衡无影响（错）
- **工程用法**：MCP 部署要点
- **版本锚点**：MCP 2025 规范
