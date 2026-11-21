---
title: "[JC-054] 协作工具·countDown（CountDownLatch）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 协作工具 · countDown（CountDownLatch）

- **事实**：CountDownLatch 计数不可重置用完即弃
- **原理**：await 等计数到零，countDown 递减，构造时固定 count，重复使用需重建对象或改用 CyclicBarrier
- **常见误区**：
  1. CountDownLatch 可 reset 复用（错）
  2. countDown 可以把计数加回来（错）
  3. 计数到零后 countDown 抛异常（错）
- **工程用法**：并行任务汇合点（多服务预加载后继续）
- **版本锚点**：JDK 文档
