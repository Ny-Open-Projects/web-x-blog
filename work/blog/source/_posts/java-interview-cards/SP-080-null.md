---
title: "[SP-080] 缓存·null（陷阱）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 缓存 · null（陷阱）

- **事实**：@Cacheable 默认不缓存 null 返回值（可配 allowNullValues）
- **原理**：穿透防护要么允许 null 加短 TTL，要么代码层缓存空对象，配合缓存穿透治理
- **常见误区**：
  1. @Cacheable 默认缓存 null（错）
  2. null 缓存与穿透无关（错）
  3. allowNullValues 是默认 true（错）
- **工程用法**：缓存穿透方案选型
- **版本锚点**：Spring 文档
