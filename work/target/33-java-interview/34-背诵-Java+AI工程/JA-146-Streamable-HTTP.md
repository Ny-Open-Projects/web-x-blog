---
title: "[JA-146] MCP·Streamable HTTP（传输）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## MCP · Streamable HTTP（传输）

- **事实**：MCP 2025 规范引入 Streamable HTTP 传输（演进替代旧 SSE 双通道方案）
- **原理**：单端点流式 HTTP 简化部署与鉴权，新项目按新传输选型，旧 SSE 仍在过渡支持
- **常见误区**：
  1. Streamable HTTP 不存在（错）
  2. 必须用 SSE（错）
  3. 传输与鉴权无关（错）
- **工程用法**：传输选型
- **版本锚点**：MCP 2025 规范
