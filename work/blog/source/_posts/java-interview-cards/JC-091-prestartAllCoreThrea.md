---
title: "[JC-091] 线程池·prestartAllCoreThreads（预热线程）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 线程池 · prestartAllCoreThreads（预热线程）

- **事实**：prestartAllCoreThreads 可提前创建所有核心线程避免冷启动抖动
- **原理**：默认核心线程懒创建（来任务才建），突发流量首请求建线程有延迟，网关类服务可预热
- **常见误区**：
  1. 核心线程在提交前就已全部创建（错）
  2. 该方法是 Executors 快捷方法自带的（错）
  3. 预热会降低内存使用（错）
- **工程用法**：低延迟网关线程池预热
- **版本锚点**：JDK 文档
