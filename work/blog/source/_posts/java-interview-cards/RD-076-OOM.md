---
title: "[RD-076] 运维·OOM（故障）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 运维 · OOM（故障）

- **事实**：Redis 写入报 OOM command not allowed：内存到 maxmemory 且策略是 noeviction
- **原理**：先看淘汰策略是否误配 noeviction，再查大 key/碎片/持久化缓冲，扩容（加内存/分片）与治理并行
- **常见误区**：
  1. 报错说明 Redis 坏了（错）
  2. 删数据是唯一解（错）
  3. 该错误只影响读（错）
- **工程用法**：线上故障应急
- **版本锚点**：实战共识
