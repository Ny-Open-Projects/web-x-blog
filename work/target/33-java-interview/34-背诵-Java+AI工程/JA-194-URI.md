---
title: "[JA-194] MCP·URI（资源）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## MCP · URI（资源）

- **事实**：MCP resources 以 URI 标识（文件/数据库行/自定义 scheme），readResource 读取内容
- **原理**：资源与工具分离：工具是动作、资源是可读数据，URI 命名空间由 server 设计
- **常见误区**：
  1. 资源与工具是同一回事（错）
  2. URI 可随意重复（错）
  3. 资源只能读文件（错）
- **工程用法**：MCP 资源设计
- **版本锚点**：MCP 规范
