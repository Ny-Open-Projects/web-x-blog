---
title: "[MY-084] 架构·query cache（缓存）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 架构 · query cache（缓存）

- **事实**：query cache 在 MySQL 8.0 被移除（命中失效代价大于收益）
- **原理**：任何表更新使相关缓存全部失效，高更新场景得不偿失，8.0 删除该功能改由应用层 Redis 承担缓存职责
- **常见误区**：
  1. 8.0 还有 query cache（错）
  2. query cache 提升写性能（错）
  3. 移除是因为性能 bug（错）
- **工程用法**：版本演进知识点
- **版本锚点**：MySQL 8.0
