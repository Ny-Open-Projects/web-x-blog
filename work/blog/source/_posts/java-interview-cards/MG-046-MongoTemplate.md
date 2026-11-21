---
title: "[MG-046] Java·MongoTemplate（集成）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Java · MongoTemplate（集成）

- **事实**：Spring Data MongoDB：MongoRepository 简单 CRUD，复杂聚合用 MongoTemplate
- **原理**：Repository 方法名解析有限（聚合/动态投影不够用），MongoTemplate 显式可控，团队规范通常两者并存
- **常见误区**：
  1. MongoRepository 能做所有事（错）
  2. MongoTemplate 是过时 API（错）
  3. 两者必须二选一（错）
- **工程用法**：Java 集成规范
- **版本锚点**：Spring Data 文档
