---
title: "[JC-009] wait/notify·IllegalMonitorStateException（协作机制）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## wait/notify · IllegalMonitorStateException（协作机制）

- **事实**：wait 与 notify 必须在持有对象 monitor 时调用否则抛 IllegalMonitorStateException
- **原理**：wait 的语义是释放锁并挂起，不持锁调用则语义不成立，JVM 直接抛异常
- **常见误区**：
  1. 任何线程都可以对任意对象调用 wait（错）
  2. 在 synchronized 块外调用 wait 只是无效不报错（错）
  3. notify 与 wait 可以不加锁配对使用（错）
- **工程用法**：永远在 synchronized(obj) 内配对使用 wait 与 notify
- **版本锚点**：JLS 17.2
