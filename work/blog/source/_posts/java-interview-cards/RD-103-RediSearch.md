---
title: "[RD-103] 生态·RediSearch（RediSearch）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 生态 · RediSearch（RediSearch）

- **事实**：RediSearch 提供二级索引与全文检索（FT.CREATE/FT.SEARCH）
- **原理**：字段索引+分词+聚合，补足"按非 key 字段查 Redis 数据"的短板，轻量搜索场景替代 ES（重场景仍 ES），Redis 8 内置
- **常见误区**：
  1. RediSearch 自动为所有字段建索引（错）
  2. 它是 KEYS 的替代（错）
  3. 全文检索必须外置 ES（错）
- **工程用法**：轻量搜索需求评估
- **版本锚点**：Redis 8.0
