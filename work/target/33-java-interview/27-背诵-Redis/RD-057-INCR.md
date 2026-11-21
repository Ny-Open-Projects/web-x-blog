---
title: "[RD-057] 分布式·INCR（限流）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 分布式 · INCR（限流）

- **事实**：分布式限流：INCR+EXPIRE 固定窗口，或 ZSet 滑动窗口，或 Lua 令牌桶
- **原理**：固定窗口有临界双倍问题，滑动窗口（本项目实测过滑动窗口语义：窗口内时间戳计数）更平滑，集群限流 Redis 是天然中心
- **常见误区**：
  1. INCR+EXPIRE 分两步没有竞态（有）（错）
  2. 滑动窗口 Redis 无法实现（错）
  3. 限流粒度只能到全局（可按 user/key 维度）（错）
- **工程用法**：接口防刷/配额控制
- **版本锚点**：本项目实测
