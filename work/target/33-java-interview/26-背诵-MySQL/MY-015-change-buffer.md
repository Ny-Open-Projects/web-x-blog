---
title: "[MY-015] 索引·change buffer（change buffer）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 索引 · change buffer（change buffer）

- **事实**：唯一索引不能使用 change buffer 而普通二级索引可以
- **原理**：change buffer 把非唯一二级索引的写缓存起来合并减少随机读页，唯一索引必须立即判重无法缓存，写多读少场景普通索引更优
- **常见误区**：
  1. 唯一索引写入更快（错）
  2. change buffer 对所有索引生效（错）
  3. change buffer 缓存的是数据页（错）
- **工程用法**：写密集场景索引选型考量
- **版本锚点**：InnoDB 文档
