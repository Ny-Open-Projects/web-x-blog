---
title: "[MY-068] 参数·buffer pool（buffer pool）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 参数 · buffer pool（buffer pool）

- **事实**：innodb_buffer_pool_size 是最关键参数：专用数据库服务器设物理内存 50%-75%
- **原理**：缓存数据页与索引页，命中率（InnoDB buffer pool hit rate）99%+ 为健康，改大小需重启（8.0 支持在线动态调整）
- **常见误区**：
  1. buffer pool 越大越好可以占 95%（错）
  2. 8.0 不能在线调整（错）
  3. 命中率与业务无关（错）
- **工程用法**：MySQL 调参第一项
- **版本锚点**：InnoDB 文档
