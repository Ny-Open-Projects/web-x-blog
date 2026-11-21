---
title: "[JC-031] 线程池·AbortPolicy（拒绝策略）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 线程池 · AbortPolicy（拒绝策略）

- **事实**：ThreadPoolExecutor 默认拒绝策略是 AbortPolicy 即抛 RejectedExecutionException
- **原理**：四种策略：Abort 抛异常、CallerRuns 由提交线程执行、Discard 静默丢弃、DiscardOldest 丢队首再提交，默认抛异常逼迫调用方处理
- **常见误区**：
  1. 默认策略是静默丢弃（错）
  2. 默认策略是调用者执行（错）
  3. 拒绝策略可以自动重试任务（错）
- **工程用法**：重要任务用 CallerRuns 降速反压
- **版本锚点**：JDK 源码
