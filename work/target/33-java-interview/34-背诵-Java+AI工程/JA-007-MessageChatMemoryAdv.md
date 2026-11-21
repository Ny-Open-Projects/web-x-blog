---
title: "[JA-007] Spring AI·MessageChatMemoryAdvisor（记忆）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · MessageChatMemoryAdvisor（记忆）

- **事实**：MessageChatMemoryAdvisor 把 ChatMemory 中的历史注入对话
- **原理**：记忆与 advisor 解耦：换记忆实现只换 ChatMemory bean，注入逻辑不变，多会话按 conversationId 隔离
- **常见误区**：
  1. 记忆必须在 prompt 里手动拼接（错）
  2. MessageChatMemoryAdvisor 与 ChatMemory 无关（错）
  3. conversationId 是可选项（多会话必须传）（错）
- **工程用法**：多轮对话记忆装配
- **版本锚点**：Spring AI 1.0 GA
