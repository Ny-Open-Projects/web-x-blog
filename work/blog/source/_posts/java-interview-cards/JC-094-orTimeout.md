---
title: "[JC-094] 异步·orTimeout（CompletableFuture）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 异步 · orTimeout（CompletableFuture）

- **事实**：JDK9 引入 orTimeout 与 completeOnTimeout 给 CF 加超时
- **原理**：超时不取消底层任务只是让 CF 以异常或默认值完成，任务线程仍可能在跑，彻底取消需要 cancel 配合任务自身响应中断
- **常见误区**：
  1. orTimeout 会中断正在执行的任务（错）
  2. JDK8 就有 orTimeout（错）
  3. 超时后底层任务立即停止（错）
- **工程用法**：CF 链统一超时兜底
- **版本锚点**：JDK9
