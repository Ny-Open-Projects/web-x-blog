---
title: "[JC-074] 异步·commonPool（CompletableFuture）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 异步 · commonPool（CompletableFuture）

- **事实**：supplyAsync 默认线程池是 ForkJoinPool.commonPool
- **原理**：commonPool 并行度为 CPU 核减一且全 JVM 共享，IO 任务占满会拖垮其他并行流任务，生产环境必须传自定义 Executor
- **常见误区**：
  1. commonPool 是 CF 专属线程池（错）
  2. commonPool 并行度等于 CPU 核数（错）
  3. 默认池隔离了不同业务（错）
- **工程用法**：CF 的异步任务统一换自定义池
- **版本锚点**：JDK8 文档
