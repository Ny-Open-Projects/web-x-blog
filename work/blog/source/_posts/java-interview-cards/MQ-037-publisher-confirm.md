---
title: "[MQ-037] 可靠·publisher confirm（confirm）"
date: 2026-11-18
categories: [Java面试, 消息队列]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 可靠 · publisher confirm（confirm）

- **事实**：RabbitMQ 可靠投递：publisher confirm（broker 确认）+mandatory（路由失败退回）+持久化
- **原理**：confirm 异步回调确认到达 broker，配合本地消息表/事务消息实现不丢投递，消费端 manual ack
- **常见误区**：
  1. confirm 默认开启（错）
  2. 持久化消息 confirm 就不丢（confirm 只到内存/日志）（错）
  3. mandatory 与 confirm 重复（错）
- **工程用法**：投递可靠性配置
- **版本锚点**：官方文档
