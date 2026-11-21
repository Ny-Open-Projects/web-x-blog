---
title: "[AL-033] 设计·LFU（LFU）"
date: 2026-11-18
categories: [Java面试, 算法]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 设计 · LFU（LFU）

- **事实**：LFU：频次桶+双向链表（同频按时间），O(1) get/put，比 LRU 多频次维度
- **原理**：频次桶数组+桶内 LRU 链，淘汰最小频次最久未用，与 Redis LFU（RD-024）概念联动，实现复杂度高于 LRU
- **常见误区**：
  1. LFU 与 LRU 相同（错）
  2. LFU 实现 O(logN)（错）
  3. 频次不衰减（Redis 有衰减）（错）
- **工程用法**：手写进阶题
- **版本锚点**：理论共识
