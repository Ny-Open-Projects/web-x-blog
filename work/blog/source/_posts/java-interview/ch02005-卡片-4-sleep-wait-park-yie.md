---
title: "卡片 4：sleep / wait / park / yield 区别"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 概念卡, 33]
type: 概念卡
disableNunjucks: true
---

### 卡片 4：sleep / wait / park / yield 区别
- sleep：Thread 静态方法，**不释放锁**，超时自动醒。
- wait：Object 方法，**必须在 synchronized 内**，释放锁，notify 唤醒。
- park/unpark：JUC 底层（LockSupport），以"许可"为单位，unpark 可先于 park 发放（不像 wait/notify 必须先等后通知），这就是 AQS 用它的原因。
- yield：提示调度器让出 CPU，不可靠，别用。
