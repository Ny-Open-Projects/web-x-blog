---
title: "[JC-030] 线程池·newCachedThreadPool（误用）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 线程池 · newCachedThreadPool（误用）

- **事实**：Executors.newCachedThreadPool 最大线程数是 Integer.MAX_VALUE 可无限创建线程
- **原理**：SynchronousQueue 无容量不排队，来一个任务必建一个新线程，高并发瞬间创建数万线程耗尽内存与线程句柄
- **常见误区**：
  1. newCachedThreadPool 有默认 10 个线程上限（错）
  2. 它内部队列是 LinkedBlockingQueue（错）
  3. 线程数上限是 CPU 核数（错）
- **工程用法**：突发可容忍时可用但要压测线程峰值
- **版本锚点**：阿里手册
