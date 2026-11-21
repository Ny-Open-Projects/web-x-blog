---
title: "[JA-076] Spring AI·Message 类型（消息）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · Message 类型（消息）

- **事实**：底层消息抽象：UserMessage/AssistantMessage/SystemMessage 三类聚合为 Prompt
- **原理**：ChatClient 门面之下消息有角色类型区分，需要精细控制消息序列时下沉到 Message 层构造 Prompt
- **常见误区**：
  1. 所有消息是同一种类型（错）
  2. AssistantMessage 不能人工构造（错）
  3. 消息类型只在日志区分（错）
- **工程用法**：精细 prompt 组装
- **版本锚点**：Spring AI 1.0 GA
