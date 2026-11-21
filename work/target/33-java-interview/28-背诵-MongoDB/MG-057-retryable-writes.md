---
title: "[MG-057] 驱动·retryable writes（重试）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 驱动 · retryable writes（重试）

- **事实**：可重试写（retryable writes，3.6+ 默认开启）网络闪断自动重试
- **原理**：驱动记录写操作（含 _id）重试一次，防网络抖动报错，但重试+失败组合仍需业务幂等（重试可能部分成功后报错）
- **常见误区**：
  1. retryable writes 保证写一定成功（错）
  2. 重试无限次（错）
  3. 默认关闭（错）
- **工程用法**：驱动层容错机制
- **版本锚点**：官方文档
