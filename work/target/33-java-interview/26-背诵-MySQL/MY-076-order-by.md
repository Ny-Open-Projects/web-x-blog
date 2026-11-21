---
title: "[MY-076] SQL·order by（排序）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## SQL · order by（排序）

- **事实**：order by 走索引免排序（联合索引含排序列），否则 filesort（sort_buffer 内存不足落盘临时文件）
- **原理**：filesort 单行太大或行数多时用"分批+归并"，max_length_for_sort_data 控制单路/双路策略，覆盖索引免回表是 order by 优化核心
- **常见误区**：
  1. filesort 一定落盘（错）
  2. order by 必须加索引列（错）
  3. sort_buffer 大小决定内存排序上限（有影响但不是全部）（错）
- **工程用法**：排序慢查询分析
- **版本锚点**：实战共识
