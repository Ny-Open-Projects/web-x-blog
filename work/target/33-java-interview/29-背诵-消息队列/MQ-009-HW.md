---
title: "[MQ-009] 复制·HW（HW）"
date: 2026-11-18
categories: [Java面试, 消息队列]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 复制 · HW（HW）

- **事实**：HW（high watermark）是消费者可见的最高位移，LEO 是日志末端
- **原理**：消费者只能读到 HW 之前的消息（ISR 确认的），LEO-HW 差值即未同步消息，防读到可能被截断的数据
- **常见误区**：
  1. 消费者能读到所有消息（错）
  2. HW 是硬件配置（错）
  3. LEO 与 HW 无关（错）
- **工程用法**：复制一致性的关键概念
- **版本锚点**：官方文档
