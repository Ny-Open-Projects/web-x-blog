---
title: "[JA-196] MCP·cursor（分页）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## MCP · cursor（分页）

- **事实**：MCP 列表类操作支持游标分页（tools/list 等，cursor 翻页）
- **原理**：大工具/资源清单一次性返回浪费，游标分页协议化，客户端要处理翻页
- **常见误区**：
  1. 列表操作必须一次全量（错）
  2. 游标是自定义字符串随意（错）
  3. 分页只在资源存在（错）
- **工程用法**：列表协议细节
- **版本锚点**：MCP 规范
