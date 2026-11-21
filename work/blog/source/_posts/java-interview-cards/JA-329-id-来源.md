---
title: "[JA-329] Spring AI·id 来源（会话）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · id 来源（会话）

- **事实**：conversationId 来源三选：前端显式传（会话模型）→后端解析（用户+会话）→默认值（无状态单轮）
- **原理**：会话标识决定记忆隔离粒度（JA-064），来源不清是串号（JA-097）的根源，接口设计先定 id 语义
- **常见误区**：
  1. conversationId 框架自动生成（错）
  2. 来源不需要设计（错）
  3. 默认值适合多用户（错）
- **工程用法**：会话标识设计
- **版本锚点**：实战共识
