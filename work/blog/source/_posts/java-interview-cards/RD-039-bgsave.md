---
title: "[RD-039] 持久化·bgsave（RDB）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 持久化 · bgsave（RDB）

- **事实**：RDB 快照 save（阻塞）/bgsave（fork 子进程）
- **原理**：fork 利用写时复制（COW）主线程继续服务，期间写操作复制页导致内存可能翻倍，大实例 fork 是秒级停顿源
- **常见误区**：
  1. bgsave 期间写入丢失（错）
  2. fork 是零成本操作（错）
  3. RDB 恢复比 AOF 慢（错）
- **工程用法**：持久化停顿排查知识
- **版本锚点**：官方文档
