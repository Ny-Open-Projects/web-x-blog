---
title: "[JA-145] MCP·roots（安全）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## MCP · roots（安全）

- **事实**：MCP 客户端可声明 roots（文件系统等作用域边界）约束 server 可访问范围
- **原理**：最小权限原则在协议层落地（AI-076 沙箱思想联动），server 越界访问被协议约束
- **常见误区**：
  1. roots 是可选装饰（错）
  2. server 可以访问任意路径（错）
  3. 边界由 server 自己声明（错）
- **工程用法**：最小权限落地
- **版本锚点**：MCP 规范
