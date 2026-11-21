---
title: "[MG-037] 聚合·$lookup（性能）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 聚合 · $lookup（性能）

- **事实**：$lookup（关联查询）是性能黑洞能冗余就冗余
- **原理**：跨集合关联相当于 SQL JOIN 但无索引优化时全扫，建模时冗余热点字段（如类目名进商品文档）避免 lookup
- **常见误区**：
  1. lookup 性能与 join 相同（错）
  2. lookup 自动建索引（错）
  3. 冗余数据不需要同步（错）
- **工程用法**：建模与查询的权衡
- **版本锚点**：实战共识
