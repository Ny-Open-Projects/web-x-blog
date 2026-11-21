---
title: "[MG-061] 查询·projection（投影）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 查询 · projection（投影）

- **事实**：projection 只取需要的字段减少网络与反序列化开销
- **原理**：配合覆盖索引免 FETCH，大文档（嵌套深）查询必须投影，与 SQL select 列同理
- **常见误区**：
  1. projection 影响索引选择不大（影响覆盖判定）（错）
  2. projection 会加载全文档再过滤（错）
  3. 默认返回全部字段是合理默认（错）
- **工程用法**：查询性能基础优化
- **版本锚点**：官方文档
