---
title: "[JC-027] 线程池·ThreadPoolExecutor（参数）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 线程池 · ThreadPoolExecutor（参数）

- **事实**：线程池标准构造有 7 个参数：corePoolSize、maximumPoolSize、keepAliveTime、unit、workQueue、threadFactory、handler
- **原理**：这是任务调度策略的全部输入，任何 Executors 快捷方法都是对它的包装且各有陷阱
- **常见误区**：
  1. 线程池只有核心与非核心线程两个参数（错）
  2. keepAliveTime 对核心线程默认也生效（错）
  3. threadFactory 参数可有可无（错）
- **工程用法**：生产环境一律手动 new ThreadPoolExecutor
- **版本锚点**：JDK 文档
