---
title: "[AL-032] 设计·LRU（LRU）"
date: 2026-11-18
categories: [Java面试, 算法]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 设计 · LRU（LRU）

- **事实**：LRU 实现：哈希表+双向链表 O(1) get/put（本项目手写并实测）
- **原理**：哈希定位节点+链表维护顺序（头最新尾最旧），Java 可用 LinkedHashMap(accessOrder=true) 快速版，容量淘汰与 Redis 近似 LRU（RD-023）对比
- **常见误区**：
  1. LRU 用数组实现 O(1)（错）
  2. LinkedHashMap 默认就是 LRU（需 accessOrder+removeEldest）（错）
  3. put 与 get 复杂度不同（错）
- **工程用法**：手写题第一名（本项目 ExamSolutions 实测）
- **版本锚点**：本项目实测
