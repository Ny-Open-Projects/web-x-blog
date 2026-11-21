---
title: "[AL-015] 堆·TopK（TopK）"
date: 2026-11-18
categories: [Java面试, 算法]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 堆 · TopK（TopK）

- **事实**：TopK：海量数据取最大 K 个用小顶堆（O(N logK) 空间 O(K)），K 小于 N/2 时堆优于全排序
- **原理**：堆只维护 K 个候选（内存友好），更大规模用分桶+外排（海量题），与 Kafka 消费（堆调度）/Redis ZSet 排行榜知识联动
- **常见误区**：
  1. TopK 用大顶堆（错）
  2. TopK 必须 O(NlogN)（错）
  3. 堆解法需要全部数据在内存（错）
- **工程用法**：海量数据题标配
- **版本锚点**：理论共识
