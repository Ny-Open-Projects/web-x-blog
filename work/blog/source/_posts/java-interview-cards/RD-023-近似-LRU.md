---
title: "[RD-023] 内存·近似 LRU（淘汰）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 内存 · 近似 LRU（淘汰）

- **事实**：Redis 的 LRU 是近似实现（随机采样 maxmemory-samples）
- **原理**：精确 LRU 需要全局链表开销大，Redis 在每个对象记录 lru 时间戳采样淘汰，效果接近精确 LRU
- **常见误区**：
  1. Redis 用精确 LRU 链表（错）
  2. 采样不会淘汰到真正的冷数据（错）
  3. 近似 LRU 是 4.0 才有（错）
- **工程用法**：淘汰机制深度题
- **版本锚点**：官方文档
