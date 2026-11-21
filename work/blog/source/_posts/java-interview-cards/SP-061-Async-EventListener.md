---
title: "[SP-061] 事件·@Async+@EventListener（异步）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 事件 · @Async+@EventListener（异步）

- **事实**：事件异步化：监听器加 @Async 且启用 @EnableAsync
- **原理**：发布线程立即返回监听在线程池执行，异步监听异常由 AsyncUncaughtExceptionHandler 处理
- **常见误区**：
  1. @EventListener 天然异步（错）
  2. 异步监听异常会传回发布者（错）
  3. 不需要线程池配置（错）
- **工程用法**：发布方不被下游拖慢
- **版本锚点**：Spring 文档
