---
title: "[RD-024] 内存·LFU（淘汰）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 内存 · LFU（淘汰）

- **事实**：LFU（4.0+）按访问频率淘汰用 Morris 计数器+衰减
- **原理**：计数对数增长省 4bit 存储，lru-decay-time 定期衰减防历史热点永驻，适合访问频率差异大的场景
- **常见误区**：
  1. LFU 精确统计频次（错）
  2. LFU 不会淘汰新 key（错）
  3. LFU 是 Redis 原生就有（4.0 引入）（错）
- **工程用法**：热点稳定型缓存选 lfu
- **版本锚点**：Redis 4.0
