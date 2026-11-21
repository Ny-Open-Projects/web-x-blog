---
title: "[JB-097] 集合通用·ArrayDeque（性能）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 集合通用 · ArrayDeque（性能）

- **事实**：ArrayDeque 作为队列/栈的性能全面优于 LinkedList（无节点创建开销、内存连续）。
- **原理**：JDK 官方文档明确建议优先使用 ArrayDeque。
- **常见误区**：
  1. LinkedList 作为栈比 ArrayDeque 快。（错）
  2. ArrayDeque 有固定的容量上限。（错）
  3. ArrayDeque 允许插入 null 元素。（错）
- **工程用法**：Deque 不允许 null（队列语义需要 null 哨兵判断 poll 失败）。
- **版本锚点**：JDK 官方推荐（替代 Stack）
