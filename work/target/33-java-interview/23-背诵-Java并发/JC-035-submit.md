---
title: "[JC-035] 线程池·submit（误用）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 线程池 · submit（误用）

- **事实**：submit 提交的任务抛出的异常被 Future 吞掉不打印
- **原理**：execute 直接走线程的 uncaughtExceptionHandler，submit 把异常包进 Future 只有 get 时才拿到，漏 get 则异常静默
- **常见误区**：
  1. submit 与 execute 异常行为一致（错）
  2. submit 会自动打印堆栈（错）
  3. 异常会传播到线程池（错）
- **工程用法**：有 get 才用 submit，否则 execute 加 UEH 打日志
- **版本锚点**：JDK 源码实测
