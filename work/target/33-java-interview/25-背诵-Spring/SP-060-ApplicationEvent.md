---
title: "[SP-060] 事件·ApplicationEvent（机制）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 事件 · ApplicationEvent（机制）

- **事实**：Spring 事件机制：ApplicationEventPublisher 发布、@EventListener 监听默认同步执行
- **原理**：监听器在发布线程内执行（同调用方法一样），异常会传播回发布者，解耦发布方与消费方
- **常见误区**：
  1. 事件默认异步执行（错）
  2. 事件监听异常不影响发布方（错）
  3. 事件是跨进程通信（错）
- **工程用法**：进程内解耦（业务完成后的扩展动作）
- **版本锚点**：Spring 文档
