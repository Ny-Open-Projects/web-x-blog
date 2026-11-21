---
title: "[JC-082] 死锁·jstack（排查）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 死锁 · jstack（排查）

- **事实**：jstack 输出末尾直接报告 Java-level deadlock 及涉及的锁
- **原理**：JVM 自动检测 monitor 与 JUC 锁的死锁，Arthas thread -b 一条命令定位死锁源头，ThreadMXBean.findDeadlockedThreads 可编程检测
- **常见误区**：
  1. 死锁需要人工分析才能发现（错）
  2. jstack 无法检测 ReentrantLock 死锁（错）
  3. 发现死锁必须重启才能解除（错）
- **工程用法**：生产 dump 排查第一入口
- **版本锚点**：工具文档
