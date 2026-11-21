---
title: "[MG-084] 索引·$regex（$regex）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 索引 · $regex（$regex）

- **事实**：正则查询前缀锚定（/^abc/）可走索引，中间匹配（/abc/）全扫
- **原理**：B 树按前缀有序，锚定前缀才能定位范围，大小写敏感选项（i）使前缀优化失效，与 MySQL like 前缀同构
- **常见误区**：
  1. /abc/ 也能走索引（错）
  2. i 选项不影响索引使用（错）
  3. 正则查询总是全扫（错）
- **工程用法**：名称/编码类查询优化
- **版本锚点**：官方文档
