---
title: "[RD-040] 持久化·RDB vs AOF（选型）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 持久化 · RDB vs AOF（选型）

- **事实**：RDB 恢复快体积小（可能丢分钟级），AOF 丢数据少（最多 1 秒）体积大恢复慢
- **原理**：4.0 起混合持久化（aof-use-rdb-preamble）：重写时 RDB 头+增量 AOF 尾，兼得两者，是生产默认推荐
- **常见误区**：
  1. 混合持久化是 RDB 独有（错）
  2. AOF 一定优于 RDB（错）
  3. 混合持久化 2.0 就有（错）
- **工程用法**：持久化选型标准答案
- **版本锚点**：Redis 4.0
