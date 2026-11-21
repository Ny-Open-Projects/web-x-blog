---
title: "[JV-024] 收集器·Mixed GC（G1）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 收集器 · Mixed GC（G1）

- **事实**：G1 的常规回收是 Mixed GC：新生代加上部分老年代 Region
- **原理**：按停顿预测模型选择回收收益最高的 Region 集合，不必然整堆回收，这是 G1 停顿可控的关键
- **常见误区**：
  1. G1 只做 Full GC（错）
  2. Mixed GC 必须回收全部老年代（错）
  3. Mixed GC 是并发的全程无停顿（错）
- **工程用法**：调 G1 必懂 Mixed GC 与停顿目标的关系
- **版本锚点**：G1 论文
