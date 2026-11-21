---
title: "[JV-011] GC·Minor GC（触发）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## GC · Minor GC（触发）

- **事实**：Minor GC 由 Eden 区空间不足触发与老年代无关
- **原理**：新生代 Eden 满即触发，回收整个新生代（Eden+两个 Survivor），采用复制算法把存活对象在 Survivor 间拷贝
- **常见误区**：
  1. Minor GC 由老年代满触发（错）
  2. Minor GC 只回收 Eden 不回收 Survivor（错）
  3. Minor GC 是 Full GC 的一种（错）
- **工程用法**：频繁 Minor GC 查分配速率
- **版本锚点**：分代收集
