---
title: "[JA-067] Spring AI·Jdbc 仓储（记忆）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · Jdbc 仓储（记忆）

- **事实**：ChatMemory 持久化用 JdbcChatMemoryRepository（chat-memory-repository-jdbc starter）
- **原理**：记忆跨实例共享与重启保留需仓储化，JDBC 实现配表结构自动管理，其他存储可自行实现仓储接口
- **常见误区**：
  1. 记忆只能存内存（错）
  2. JDBC 仓储需要手工维护所有表（错）
  3. 持久化改变记忆窗口语义（错）
- **工程用法**：多实例会话记忆
- **版本锚点**：Spring AI 1.0 GA
