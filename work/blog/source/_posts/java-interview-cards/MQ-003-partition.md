---
title: "[MQ-003] 架构·partition（分区）"
date: 2026-11-18
categories: [Java面试, 消息队列]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 架构 · partition（分区）

- **事实**：Kafka 主题分多个 partition（并行单元）分区内有序
- **原理**：分区是并行度与顺序性的单位，生产按 key 哈希路由保证同 key 同分区，扩分区会破坏 key 路由（同 key 可能换分区）
- **常见误区**：
  1. partition 内无序（错）
  2. 分区数越少越好（错）
  3. 扩分区不影响顺序（错）
- **工程用法**：分区设计的顺序性代价
- **版本锚点**：官方文档
