---
title: "[JC-098] 协作·Condition（条件队列）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 协作 · Condition（条件队列）

- **事实**：Condition 将等待队列从锁对象解耦支持一个锁多个条件队列
- **原理**：synchronized 只有一套 wait/notify，多条件必须 notifyAll 全员唤醒，ReentrantLock 多个 Condition 精准唤醒对应等待者，有界队列 ArrayBlockingQueue 即 notFull/notEmpty 双条件
- **常见误区**：
  1. 一个 ReentrantLock 只能有一个 Condition（错）
  2. Condition 的 signal 不需要持有锁（错）
  3. Condition 与 Object.wait 可以混用（错）
- **工程用法**：生产者消费者分开唤醒用双 Condition
- **版本锚点**：JDK 源码
