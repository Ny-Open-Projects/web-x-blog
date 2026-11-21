---
title: "[JC-104] 虚拟线程·carrier（调度）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 虚拟线程 · carrier（调度）

- **事实**：虚拟线程默认调度器是专用 ForkJoinPool（FIFO 模式）并行度默认 CPU 核数
- **原理**：可用 jdk.virtualThreadScheduler.parallelism 调整，载体线程数少于虚拟线程数百万级，阻塞 IO 时载体立即被复用
- **常见误区**：
  1. 载体线程数等于虚拟线程数（错）
  2. 调度器是平台线程池需手动创建（错）
  3. 并行度默认是 1（错）
- **工程用法**：调优虚拟线程吞吐先调载体数
- **版本锚点**：JDK21 文档
