---
title: "[MY-019] explain·Extra（Extra）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## explain · Extra（Extra）

- **事实**：关键 Extra：Using index（覆盖）、Using index condition（ICP）、Using filesort（额外排序）、Using temporary（临时表）
- **原理**：filesort 与 temporary 是性能红灯：order by 未走索引、group by/distinct 建 tmp，优化方向是补索引或改写
- **常见误区**：
  1. Using index 表示回表（错）
  2. Using filesort 是文件排序一定落盘（错）
  3. Extra 只显示 type 信息（错）
- **工程用法**：explain 解读第二指标
- **版本锚点**：MySQL 文档
