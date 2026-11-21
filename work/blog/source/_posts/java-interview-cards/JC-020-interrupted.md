---
title: "[JC-020] 线程基础·interrupted（中断）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 线程基础 · interrupted（中断）

- **事实**：静态 Thread.interrupted 会清除中断标志而实例方法 isInterrupted 不会
- **原理**：interrupted 设计给线程自查并消费信号，误用会丢失他人设置的中断状态
- **常见误区**：
  1. interrupted 与 isInterrupted 完全等价（错）
  2. isInterrupted 也会清除标志（错）
  3. 静态方法操作的是当前线程以外的线程（错）
- **工程用法**：自查循环里用 interrupted 消费信号
- **版本锚点**：Thread 源码
