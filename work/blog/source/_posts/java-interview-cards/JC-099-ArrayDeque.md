---
title: "[JC-099] 并发容器·ArrayDeque（Deque）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 并发容器 · ArrayDeque（Deque）

- **事实**：ArrayDeque 是循环数组双端队列性能优于 Stack 与 LinkedList
- **原理**：官方明确推荐替代 Stack（Stack 继承 Vector 带锁开销），做队列也优于 LinkedList（缓存友好）
- **常见误区**：
  1. Stack 是推荐的栈实现（错）
  2. ArrayDeque 有容量上限不可扩容（错）
  3. LinkedList 做队列性能最优（错）
- **工程用法**：栈一律 ArrayDeque
- **版本锚点**：JDK 文档
