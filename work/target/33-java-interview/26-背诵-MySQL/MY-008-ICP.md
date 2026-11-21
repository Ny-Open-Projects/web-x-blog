---
title: "[MY-008] 索引·ICP（下推）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 索引 · ICP（下推）

- **事实**：索引下推（ICP，5.6+）把 where 条件下推到存储引擎层先过滤再回表
- **原理**：联合索引非前缀列的条件在引擎层用索引值过滤，减少回表次数，explain Extra 出现 Using index condition
- **常见误区**：
  1. ICP 会减少索引扫描（错）
  2. ICP 在 Server 层过滤（错）
  3. ICP 只对主键查询生效（错）
- **工程用法**：5.6+ 默认开启知道其原理即可
- **版本锚点**：MySQL 5.6
