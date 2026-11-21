---
title: "[RD-053] 队列·BRPOP（List）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 队列 · BRPOP（List）

- **事实**：轻量队列：LPUSH+BRPOP（阻塞弹出）
- **原理**：简单异步任务场景可用，缺点：无 ACK（取出即丢）、无重试、无持久化保障，要求高的场景用 Stream 或专业 MQ
- **常见误区**：
  1. List 队列支持 ACK（错）
  2. BRPOP 不阻塞（错）
  3. List 队列可以替代 Kafka（错）
- **工程用法**：消息队列选型降级方案
- **版本锚点**：实战共识
