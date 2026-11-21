---
title: "[JC-086] 并发容器·ConcurrentSkipListMap（选型）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 并发容器 · ConcurrentSkipListMap（选型）

- **事实**：需要排序的并发 Map 用 ConcurrentSkipListMap（跳表）
- **原理**：TreeMap 线程不安全，加锁 TreeMap 退化为全局锁，跳表天然支持无锁读与范围查询，Redis ZSet 同款结构
- **常见误区**：
  1. ConcurrentSkipListMap 是 TreeMap 的线程安全版（错）
  2. 跳表比红黑树内存更省（错）
  3. 跳表不支持范围查询（错）
- **工程用法**：并发+有序+范围查询场景
- **版本锚点**：JDK 文档
