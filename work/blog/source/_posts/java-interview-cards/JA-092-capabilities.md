---
title: "[JA-092] MCP·capabilities（能力）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## MCP · capabilities（能力）

- **事实**：MCP initialize 阶段双方声明 capabilities（支持的工具/资源/采样能力）
- **原理**：能力协商决定后续可用方法集，客户端不应调用对方未声明的能力，协议稳健性来源
- **常见误区**：
  1. capabilities 是装饰信息（错）
  2. 不声明也能调用全部能力（错）
  3. 能力协商单方完成（错）
- **工程用法**：协议机制理解
- **版本锚点**：MCP 规范
