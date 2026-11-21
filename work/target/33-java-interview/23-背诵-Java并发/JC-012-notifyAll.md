---
title: "[JC-012] wait/notify·notifyAll（协作机制）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## wait/notify · notifyAll（协作机制）

- **事实**：notify 只随机唤醒一个等待线程无法指定目标
- **原理**：多个线程等待不同条件时可能唤醒错误的线程导致所有线程永久等待，多条件场景必须 notifyAll
- **常见误区**：
  1. notify 会唤醒所有等待线程（错）
  2. notify 保证唤醒的是等待最久的线程（错）
  3. notify 比 notifyAll 在任何场景都更快（错）
- **工程用法**：多条件共用一个锁对象时用 notifyAll 或拆分锁
- **版本锚点**：实战经验
