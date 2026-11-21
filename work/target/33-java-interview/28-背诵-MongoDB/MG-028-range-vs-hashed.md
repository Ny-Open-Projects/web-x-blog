---
title: "[MG-028] 分片·range vs hashed（类型）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 分片 · range vs hashed（类型）

- **事实**：range 分片（范围查询友好）vs hashed 分片（写均匀、范围查询废）
- **原理**：range 支持范围扫描但单调写倾斜，hashed 写分散但点查与范围查询代价不同，按读写模式选
- **常见误区**：
  1. hashed 支持范围查询（错）
  2. range 写永远均匀（错）
  3. 两者性能相同（错）
- **工程用法**：分片策略选型
- **版本锚点**：官方文档
