---
title: "[JV-012] GC·Full GC（触发）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## GC · Full GC（触发）

- **事实**：Full GC 触发场景：老年代空间不足、元空间不足、System.gc、晋升失败等
- **原理**：Full GC 涉及整堆 stop-the-world（G1/ZGC 的 Full GC 也是 STW），是延迟毛刺的主要来源
- **常见误区**：
  1. Full GC 只回收老年代（错）
  2. G1 的 Full GC 是并发的（错）
  3. 频繁 Full GC 是正常现象（错）
- **工程用法**：Full GC 频率是 JVM 健康第一指标
- **版本锚点**：JVM 实践
