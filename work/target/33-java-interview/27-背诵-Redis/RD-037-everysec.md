---
title: "[RD-037] 持久化·everysec（AOF）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 持久化 · everysec（AOF）

- **事实**：AOF 刷盘三策略：always/everysec（默认）/no
- **原理**：everysec 每秒 fsync 最多丢 1 秒数据（平衡点），always 最安全最慢，no 交给 OS，官方文档核对（默认 everysec）
- **常见误区**：
  1. AOF 默认 always（错）
  2. everysec 不会丢数据（错）
  3. no 策略最安全（错）
- **工程用法**：持久化参数标准
- **版本锚点**：官方文档核对
