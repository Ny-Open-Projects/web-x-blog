---
title: "[JC-032] 线程池·CallerRunsPolicy（拒绝策略）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 线程池 · CallerRunsPolicy（拒绝策略）

- **事实**：CallerRunsPolicy 让提交任务的线程自己执行以实现反压
- **原理**：执行期间提交线程被占用，上游生产速度被迫降速，是简洁的背压手段但会阻塞调用方
- **常见误区**：
  1. CallerRunsPolicy 把任务转给空闲线程执行（错）
  2. 它把任务放回队列头部（错）
  3. 它不会阻塞提交线程（错）
- **工程用法**：非核心链路可接受，支付链路慎用
- **版本锚点**：实战经验
