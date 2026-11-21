---
title: "[MG-035] 存储引擎·checkpoint（checkpoint）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 存储引擎 · checkpoint（checkpoint）

- **事实**：WiredTiger 定期 checkpoint（默认 60 秒）落盘一致状态
- **原理**：journal（WAL）保证 checkpoint 间崩溃恢复，恢复时长与 journal 量相关，60 秒检查点+journal 是恢复模型
- **常见误区**：
  1. checkpoint 每 10 秒（错）
  2. journal 可关闭（生产不可关）（错）
  3. checkpoint 期间停写（错）
- **工程用法**：崩溃恢复机制
- **版本锚点**：官方文档
