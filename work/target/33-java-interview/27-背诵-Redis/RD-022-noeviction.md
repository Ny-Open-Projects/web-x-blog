---
title: "[RD-022] 内存·noeviction（淘汰）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 内存 · noeviction（淘汰）

- **事实**：内存淘汰 8 种策略默认 noeviction（写报错）
- **原理**：volatile 系列（有过期时间）与 allkeys 系列（全库）×lru/lfu/random + noeviction/ttl，缓存场景应设 allkeys-lru
- **常见误区**：
  1. 默认会自动淘汰冷数据（错）
  2. 淘汰策略默认 allkeys-lru（错）
  3. noeviction 表示删除所有数据（错）
- **工程用法**：缓存实例必配淘汰策略
- **版本锚点**：官方文档
