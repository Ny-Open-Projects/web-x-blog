---
title: "[JA-093] MCP·content（结果）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## MCP · content（结果）

- **事实**：MCP 工具结果以 content 列表返回（文本/图片/资源引用等内容块）
- **原理**：结果是多模态内容块而非纯字符串，客户端按类型处理，模型消费时转文本上下文
- **常见误区**：
  1. 工具结果永远是纯文本（错）
  2. content 类型不可扩展（错）
  3. 图片结果无法返回（错）
- **工程用法**：MCP 结果处理
- **版本锚点**：MCP 规范
