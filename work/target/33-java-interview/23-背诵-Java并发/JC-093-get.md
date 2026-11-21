---
title: "[JC-093] 异步·get（Future）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 异步 · get（Future）

- **事实**：Future.get 不传超时参数会无限阻塞
- **原理**：下游挂死则调用线程永久卡住，必须 get(timeout) 并处理 TimeoutException，或整体改 CF 加 orTimeout（JDK9+）
- **常见误区**：
  1. Future.get 默认有 30 秒超时（错）
  2. get 阻塞时会自动释放线程池线程（错）
  3. 超时后任务自动取消（错）
- **工程用法**：所有远程调用 Future 必须带超时
- **版本锚点**：JDK 文档
