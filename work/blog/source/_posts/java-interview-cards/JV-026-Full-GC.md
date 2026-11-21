---
title: "[JV-026] 收集器·Full GC（G1）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 收集器 · Full GC（G1）

- **事实**：G1 的 Full GC 在 JDK10 起为多线程并行（JEP 307）
- **原理**：JDK8 的 G1 Full GC 是单线程 Serial，退化时停顿巨大，JDK10 改并行大幅缩短，升级 JDK 版本对 G1 退化场景收益明显
- **常见误区**：
  1. G1 的 Full GC 一直是并行的（错）
  2. G1 Full GC 也是并发的无停顿（错）
  3. G1 永远不会退化到 Full GC（错）
- **工程用法**：升级 JDK 修复 G1 退化停顿
- **版本锚点**：JEP 307
