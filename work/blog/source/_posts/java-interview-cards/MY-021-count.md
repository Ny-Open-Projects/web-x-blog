---
title: "[MY-021] SQL·count(*)（count）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## SQL · count(*)（count）

- **事实**：count(*) 与 count(1) 等价且官方推荐，count(col) 会跳过 null
- **原理**：count(*) 由优化器专门优化（任选最小索引数行），count(col) 需逐行判空，count(distinct col) 去重且忽略 null
- **常见误区**：
  1. count(1) 比 count(*) 快（错）
  2. count(col) 与 count(*) 结果一定相同（错）
  3. count(*) 必须扫全表（错）
- **工程用法**：统计行数规范写 count(*)
- **版本锚点**：官方文档核对
