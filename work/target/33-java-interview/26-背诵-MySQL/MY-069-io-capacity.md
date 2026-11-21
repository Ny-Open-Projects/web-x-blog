---
title: "[MY-069] 参数·io capacity（刷脏）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 参数 · io capacity（刷脏）

- **事实**：innodb_io_capacity 告诉 InnoDB 磁盘能力（SSD 建议 2000+）
- **原理**：刷脏速率匹配磁盘吞吐，设置过低脏页堆积触发"连击"刷脏引发性能抖动（ wal 快满时激进刷盘）
- **常见误区**：
  1. 该参数与磁盘无关（错）
  2. 设置越高越好（错）
  3. 刷脏只发生在空闲时（错）
- **工程用法**：性能抖动排查知识点
- **版本锚点**：InnoDB 文档
