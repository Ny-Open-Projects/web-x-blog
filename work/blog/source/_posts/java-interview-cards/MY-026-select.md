---
title: "[MY-026] SQL·select *（优化）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## SQL · select *（优化）

- **事实**：select * 的危害：无法覆盖索引、传输无效列、buffer pool 污染
- **原理**：按需 select 列表配合覆盖索引，宽表大字段（TEXT/BLOB）必须拆分按需读
- **常见误区**：
  1. select * 有查询缓存优化抵消（错）
  2. select * 对性能无影响（错）
  3. 只影响网络传输（错）
- **工程用法**：SQL 规范第一条
- **版本锚点**：实战共识
