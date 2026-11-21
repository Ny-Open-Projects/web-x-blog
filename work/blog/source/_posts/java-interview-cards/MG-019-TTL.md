---
title: "[MG-019] 索引·TTL（TTL）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 索引 · TTL（TTL）

- **事实**：TTL 索引（expireAfterSeconds）后台约 60 秒一轮删除过期文档
- **原理**：删除有延迟（非精确到秒），适合日志/会话类清理，官方文档核对（60 秒巡检周期），删除操作本身有性能开销
- **常见误区**：
  1. TTL 精确到秒删除（错）
  2. TTL 删除是免费的（错）
  3. TTL 可用于所有场景（错）
- **工程用法**：过期数据清理方案
- **版本锚点**：官方文档核对
