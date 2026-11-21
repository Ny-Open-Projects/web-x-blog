---
title: "[RD-019] 运维·KEYS（阻塞）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 运维 · KEYS（阻塞）

- **事实**：KEYS * 生产禁用：全库遍历阻塞主线程
- **原理**：O(N) 阻塞命令族（KEYS/HGETALL 大集合/SMEMBERS），替代方案 SCAN 渐进式遍历
- **常见误区**：
  1. KEYS * 在小库可以随便用（错）
  2. KEYS 是 O(1)（错）
  3. 阻塞只发生在数据量大时（小也会瞬时占住主线程）（错）
- **工程用法**：代码 review 静态扫描项
- **版本锚点**：实战共识
