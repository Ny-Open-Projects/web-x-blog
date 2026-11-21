---
title: "[JA-035] LangChain4j·ChatMemory（记忆）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · ChatMemory（记忆）

- **事实**：LangChain4j 的记忆：MessageWindowChatMemory 窗口记忆，AiServices.chatMemoryProvider(id→memory) 支持多会话
- **原理**：多用户场景按 memoryId 隔离各自窗口，持久化由 ChatMemoryStore 接口实现（内存/数据库）
- **常见误区**：
  1. 记忆自动全局共享（错）
  2. 多会话不需要 memoryId（错）
  3. 窗口截断会丢系统提示（错）
- **工程用法**：多会话记忆装配
- **版本锚点**：LangChain4j 1.0
