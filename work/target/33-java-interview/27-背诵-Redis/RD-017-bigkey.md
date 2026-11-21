---
title: "[RD-017] 运维·bigkey（bigkey）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 运维 · bigkey（bigkey）

- **事实**：bigkey（大 key）危害：阻塞主线程、网络拥塞、删除卡顿、倾斜
- **原理**：排查 redis-cli --bigkeys 与 MEMORY USAGE，治理拆分（hash 分桶）与异步删除（UNLINK）
- **常见误区**：
  1. bigkey 只是占内存无性能影响（错）
  2. 大 key 删除自动安全（错）
  3. bigkey 只在 cluster 有影响（错）
- **工程用法**：生产隐患排查项
- **版本锚点**：实战共识
