---
title: "[RD-056] Bitmap·bitmap（统计）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Bitmap · bitmap（统计）

- **事实**：bitmap 用 1 位表示一个状态：签到/活跃/布尔集合，1 亿用户活跃约 12MB
- **原理**：SETBIT/BITCOUNT/BITOP，位偏移即用户 ID，月度签到卡（31 bit）与连续签到计算（BITPOS）标准方案
- **常见误区**：
  1. bitmap 每个用户固定 1 字节（错）
  2. BITCOUNT 是 O(N) 无优化（有 popcount 优化）（错）
  3. bitmap 不能求交集（错）
- **工程用法**：海量布尔统计方案
- **版本锚点**：实战共识
