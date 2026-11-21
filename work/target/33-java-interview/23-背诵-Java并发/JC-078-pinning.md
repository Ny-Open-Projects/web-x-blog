---
title: "[JC-078] 虚拟线程·pinning（误用）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 虚拟线程 · pinning（误用）

- **事实**：JDK21-23 中虚拟线程在 synchronized 块内阻塞会 pin 载体线程
- **原理**：被 pin 的载体无法释放导致吞吐退化，JDK24 JEP 491 已修复（synchronized 不再 pin）；过渡期热点路径可换 ReentrantLock
- **常见误区**：
  1. pinning 问题在 JDK21 已修复（错）
  2. pinning 只影响性能不影响正确性所以无需关注（错）
  3. ReentrantLock 也会 pin 载体线程（错）
- **工程用法**：JDK21 服务排查吞吐退化先查 pin
- **版本锚点**：JEP 491
