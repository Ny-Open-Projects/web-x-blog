---
title: "[MQ-015] 性能·sendfile（零拷贝）"
date: 2026-11-18
categories: [Java面试, 消息队列]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 性能 · sendfile（零拷贝）

- **事实**：Kafka 用零拷贝（sendfile）从页缓存直达网卡免用户态拷贝
- **原理**：消费路径数据不进用户态（2 次拷贝→0 次），配合页缓存命中率，是 Kafka 吞吐高的关键之一
- **常见误区**：
  1. 零拷贝是 Kafka 独有（NIO 有）（错）
  2. sendfile 有多次内核拷贝（错）
  3. 零拷贝与吞吐无关（错）
- **工程用法**：性能原理八股
- **版本锚点**：Linux 机制
