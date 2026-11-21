---
title: "[JA-195] MCP·prompts（模板）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## MCP · prompts（模板）

- **事实**：MCP prompts 原语提供服务端预置提示模板（带参数）供客户端取用
- **原理**：把"优质提示词"生态化复用（客户端无需内置），与 resources/tools 并列（JA-143 三原语）
- **常见误区**：
  1. prompts 是客户端历史记录（错）
  2. 模板不能带参数（错）
  3. 该原语很少实现（错）
- **工程用法**：提示词生态复用
- **版本锚点**：MCP 规范
