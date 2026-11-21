---
title: "[JC-087] 协作·park（LockSupport）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 协作 · park（LockSupport）

- **事实**：LockSupport.park 与 unpark 是 JUC 阻塞的底层原语
- **原理**：unpark 可先于 park 调用（许可制，最多持有 1 个许可），不抛 InterruptedException 但响应中断返回，AQS 队列挂起全靠它
- **常见误区**：
  1. unpark 必须在 park 之后调用才有效（错）
  2. park 会抛 InterruptedException（错）
  3. LockSupport 与线程池强绑定（错）
- **工程用法**：自定义同步器时使用
- **版本锚点**：JDK 源码
