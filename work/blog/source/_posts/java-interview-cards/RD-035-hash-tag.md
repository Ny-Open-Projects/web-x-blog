---
title: "[RD-035] Cluster·hash tag（限制）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Cluster · hash tag（限制）

- **事实**：Cluster 下 mget/mset/事务/Lua 多 key 必须同 slot，hash tag {} 强制同槽
- **原理**：key 含 {} 内相同串则按串计算槽（user:{1001}:a 与 user:{1001}:b 同槽），跨槽命令报 CROSSSLOT 错误
- **常见误区**：
  1. Cluster 完全支持 mget（自动聚合，客户端可聚合但底层仍拆分）（错）
  2. hash tag 会影响数据均匀（错）
  3. Lua 在 Cluster 不可用（同槽 Lua 可用）（错）
- **工程用法**：业务 key 设计规范
- **版本锚点**：官方文档
