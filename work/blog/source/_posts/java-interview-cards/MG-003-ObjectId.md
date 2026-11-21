---
title: "[MG-003] 文档模型·ObjectId（主键）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 文档模型 · ObjectId（主键）

- **事实**：默认主键 ObjectId=4 字节秒级时间戳+5 字节进程级随机+3 字节递增计数
- **原理**：时间戳前缀使 ObjectId 天然趋势递增，写入分布式友好（类似雪花效果），官方文档核对零差异
- **常见误区**：
  1. ObjectId 是完全随机的（错）
  2. 3 字节计数是全局递增（是进程内递增）（错）
  3. ObjectId 不含时间信息（错）
- **工程用法**：_id 设计与写入性能
- **版本锚点**：官方文档核对
