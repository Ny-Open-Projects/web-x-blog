---
title: "[JA-197] MCP·log（日志）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## MCP · log（日志）

- **事实**：MCP 带 logging 能力（server 按级别推送日志消息给 client）
- **原理**：server 侧运行日志协议化输出（client 面板可见），排查 MCP 工具问题时开日志能力
- **常见误区**：
  1. server 日志只能写本地文件（错）
  2. MCP 无日志能力（错）
  3. 日志级别不可控（错）
- **工程用法**：MCP 排障
- **版本锚点**：MCP 规范
