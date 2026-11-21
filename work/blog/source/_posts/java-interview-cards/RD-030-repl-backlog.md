---
title: "[RD-030] 复制·repl_backlog（增量）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 复制 · repl_backlog（增量）

- **事实**：增量复制靠 repl_backlog 环形缓冲区（replication backlog）
- **原理**：从库断线重连时 offset 还在 backlog 内则增量补发，backlog 太小（默认 1MB）会被覆盖触发全量，调大 backlog 是主从抖动的第一优化
- **常见误区**：
  1. 断线重连总是全量（错）
  2. backlog 默认足够大（错）
  3. backlog 在从库（错）
- **工程用法**：主从网络抖动治理
- **版本锚点**：官方文档
