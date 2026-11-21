---
title: "[RD-084] 场景·INCR（计数）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 场景 · INCR（计数）

- **事实**：计数器场景：INCR 原子自增（文章阅读量/库存预占/接口调用统计）
- **原理**：INCR 原子且 O(1)，计数语义与过期组合（INCR+EXPIRE 限流），需要持久化的计数定期落库
- **常见误区**：
  1. INCR 有并发问题（错）
  2. 计数必须每次写库（错）
  3. INCR 返回值是 void（错）
- **工程用法**：高频原子操作
- **版本锚点**：实战共识
