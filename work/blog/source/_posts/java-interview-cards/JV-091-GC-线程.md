---
title: "[JV-091] GC·GC 线程（并发）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## GC · GC 线程（并发）

- **事实**：GC 线程数由 -XX:ConcGCThreads 与 ParallelGCThreads 控制
- **原理**：ParallelGCThreads 是 STW 阶段并行线程数（默认约 CPU 核数），ConcGCThreads 是并发阶段线程数（默认按比例），容器 CPU 限额影响默认值
- **常见误区**：
  1. GC 线程越多吞吐越高无上限（错）
  2. GC 与业务线程永不并行（错）
  3. GC 线程数无法配置（错）
- **工程用法**：容器化 JVM 调参注意 CPU 限额影响默认值
- **版本锚点**：HotSpot
