---
title: "[JC-017] 线程基础·BLOCKED（线程状态）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 线程基础 · BLOCKED（线程状态）

- **事实**：Java 线程有 6 种状态 BLOCKED 与 WAITING 语义不同
- **原理**：BLOCKED 是等 monitor 锁，WAITING 是等 notify、join 或 LockSupport.park，TIMED_WAITING 是限时版
- **常见误区**：
  1. RUNNABLE 的线程一定在 CPU 上执行（错）
  2. BLOCKED 包括等 Condition（错）
  3. 线程状态共 5 种（错）
- **工程用法**：dump 分析时区分 BLOCKED 与 WAITING 定位问题
- **版本锚点**：Thread.State
