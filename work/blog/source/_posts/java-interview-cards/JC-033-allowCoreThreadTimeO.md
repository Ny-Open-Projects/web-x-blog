---
title: "[JC-033] 线程池·allowCoreThreadTimeOut（参数）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 线程池 · allowCoreThreadTimeOut（参数）

- **事实**：allowCoreThreadTimeOut(true) 可让核心线程在空闲超过 keepAliveTime 后被回收
- **原理**：默认核心线程不回收常驻内存，流量低谷期可用该参数释放资源，回收后新任务重新建线程
- **常见误区**：
  1. 核心线程在任何配置下都不会回收（错）
  2. 该参数只对非核心线程生效（错）
  3. 开启后线程池最少保留 1 个线程（错）
- **工程用法**：突发流量型服务低谷缩容
- **版本锚点**：JDK 文档
