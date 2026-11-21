---
title: "[JV-008] 对象分配·Humongous（大对象）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 对象分配 · Humongous（大对象）

- **事实**：G1 中对象大于等于 Region 一半时直接进入 Humongous 区域
- **原理**：巨型对象在新生代反复复制代价极高，G1 连续 Region 存放并视为老年代一部分，是 G1 特有概念
- **常见误区**：
  1. 大对象在任何收集器都进老年代（错）
  2. Humongous 对象会在 Minor GC 中被复制（错）
  3. Humongous 是普通老年代对象的一种（错）
- **工程用法**：巨型缓存数组导致 G1 频繁 Mixed GC 时查 Humongous
- **版本锚点**：G1 实现
