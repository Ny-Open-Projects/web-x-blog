---
title: "[MG-085] 驱动·retryable reads（重试）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 驱动 · retryable reads（重试）

- **事实**：可重试读（retryReads，3.6+ 默认开启）网络抖动自动重试读操作
- **原理**：读操作天然幂等可安全重试，与 retryable writes 组成驱动层容错，网络闪断不再报错（代价是掩盖网络问题需监控）
- **常见误区**：
  1. retryReads 默认关闭（错）
  2. 重试读可能读到脏数据（错）
  3. 读重试需要业务幂等（读天然幂等无需）（错）
- **工程用法**：驱动容错配置
- **版本锚点**：官方文档
