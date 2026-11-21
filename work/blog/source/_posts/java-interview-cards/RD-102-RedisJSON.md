---
title: "[RD-102] 生态·RedisJSON（RedisJSON）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 生态 · RedisJSON（RedisJSON）

- **事实**：RedisJSON 提供文档级 JSON 存取（JSON.SET/JSON.GET 路径语法）
- **原理**：支持 JSONPath 局部更新与原子操作，对比 String 存 JSON：免全量序列化（局部读写字段），与 MongoDB 文档思想对齐但更轻
- **常见误区**：
  1. RedisJSON 就是 String 存 JSON（错）
  2. 局部更新需自己读改写（错）
  3. JSON.GET 无路径过滤（错）
- **工程用法**：对象局部字段高频更新场景
- **版本锚点**：Redis 8.0
