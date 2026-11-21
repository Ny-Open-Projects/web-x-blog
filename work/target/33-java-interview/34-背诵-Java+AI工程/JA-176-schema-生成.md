---
title: "[JA-176] MCP·schema 生成（工具）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## MCP · schema 生成（工具）

- **事实**：MCP Java SDK 从 POJO/方法签名自动生成 inputSchema（JSON Schema）
- **原理**：手写 schema 易错，SDK 反射生成保证与实现同步，描述字段仍需人工写清（JA-108）
- **常见误区**：
  1. schema 必须手写（错）
  2. 自动生成的 schema 无描述（错）
  3. 生成与实现会脱节（错）
- **工程用法**：MCP 工具注册
- **版本锚点**：官方文档核对
