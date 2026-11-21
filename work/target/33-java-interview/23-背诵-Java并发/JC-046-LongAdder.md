---
title: "[JC-046] 原子类·LongAdder（性能）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 原子类 · LongAdder（性能）

- **事实**：高竞争计数用 LongAdder 而非 AtomicLong
- **原理**：AtomicLong 所有线程 CAS 同一个值自旋严重，LongAdder 分散到 Cell 数组各自累加，sum 时汇总，竞争下吞吐可高一个数量级
- **常见误区**：
  1. LongAdder 在任何场景都快于 AtomicLong（错）
  2. LongAdder 的 sum 是精确强一致快照（错）
  3. LongAdder 也能 replace 原子读改写（错）
- **工程用法**：纯计数（QPS 统计）用 LongAdder
- **版本锚点**：JDK 文档
