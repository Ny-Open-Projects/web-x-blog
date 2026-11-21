---
title: "[JV-110] 排查·ThreadMXBean（编程）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 排查 · ThreadMXBean（编程）

- **事实**：ThreadMXBean 提供编程式诊断：findDeadlockedThreads/线程 CPU 时间/锁持有统计
- **原理**：无需外部工具在应用内自检（健康检查集成死锁探测），getThreadCpuTime 区分忙与闲（比 wall time 准），是自研监控平台的编程接口
- **常见误区**：
  1. ThreadMXBean 只能读不能监控（错）
  2. findDeadlockedThreads 只查 monitor 死锁（也查 JUC 属主环）（错）
  3. CPU 时间与墙钟时间相同（错）
- **工程用法**：自研健康检查的 API 基础
- **版本锚点**：JDK 文档
