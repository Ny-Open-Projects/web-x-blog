---
title: "[JC-018] 线程基础·interrupt（中断）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 线程基础 · interrupt（中断）

- **事实**：对运行中的线程调用 interrupt 只是设置中断标志不会真正停止
- **原理**：Java 的协作式中断：线程需要自行检查 isInterrupted 或在阻塞点抛 InterruptedException 响应
- **常见误区**：
  1. interrupt 会立刻杀死线程（错）
  2. interrupt 只对阻塞中的线程有效（错）
  3. 循环中检查中断会降低性能（错）
- **工程用法**：任务循环内定期检查 Thread.currentThread().isInterrupted()
- **版本锚点**：Thread.interrupt javadoc
