---
title: "[JA-148] MCP·OAuth（鉴权）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## MCP · OAuth（鉴权）

- **事实**：MCP 2025 规范为 HTTP 传输引入 OAuth 鉴权框架（客户端授权访问远程 server）
- **原理**：远程 server 的访问控制协议化（不再靠网络隔离），企业接入必备认知，与 SP-088 安全链知识互补
- **常见误区**：
  1. 远程 server 无需鉴权（错）
  2. 鉴权只在网络层做（错）
  3. OAuth 与 MCP 无关（错）
- **工程用法**：远程安全接入
- **版本锚点**：MCP 2025 规范
