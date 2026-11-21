---
title: "[JB-072] Object·wait与notify（语法语义）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Object · wait与notify（语法语义）

- **事实**：wait/notify/notifyAll 是 Object 的 final 方法，必须在 synchronized 块内调用，否则抛 IllegalMonitorStateException。
- **原理**：wait 释放锁进入等待集，notify/notifyAll 唤醒等待线程重新竞争锁。
- **常见误区**：
  1. wait 可以在任意位置调用。（错）
  2. notify 会立即释放锁。（错）
  3. wait/notify 定义在 Thread 类中。（错）
- **工程用法**：notify 在锁释放前不生效（锁释放后等待线程才真正被唤醒）。
- **版本锚点**：JLS 17.2
