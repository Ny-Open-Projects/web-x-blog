---
title: "[JC-051] 显式锁·lockInterruptibly（能力）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 显式锁 · lockInterruptibly（能力）

- **事实**：ReentrantLock 相比 synchronized 增加可中断、超时与公平能力
- **原理**：lockInterruptibly 等锁时响应中断、tryLock(time) 限时获取、多 Condition 条件队列，synchronized 全都不支持
- **常见误区**：
  1. synchronized 也支持中断等待（错）
  2. tryLock 获取不到会一直重试（错）
  3. Condition 与 wait 必须配对在同一把锁上（错）
- **工程用法**：需要中断响应与限时获取的场景选 ReentrantLock
- **版本锚点**：JDK 文档
