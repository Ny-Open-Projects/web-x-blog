---
title: "[JA-008] Spring AI·MessageWindowChatMemory（记忆）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · MessageWindowChatMemory（记忆）

- **事实**：ChatMemory 默认实现 MessageWindowChatMemory 按窗口保留最近 N 条消息
- **原理**：窗口截断防 token 爆炸，持久化经 ChatMemoryRepository（内存或 JDBC 实现）
- **常见误区**：
  1. ChatMemory 无限保留全部历史（错）
  2. MessageWindowChatMemory 是持久化数据库（错）
  3. 窗口参数不可调（错）
- **工程用法**：多轮上下文成本控制
- **版本锚点**：Spring AI 1.0 GA
