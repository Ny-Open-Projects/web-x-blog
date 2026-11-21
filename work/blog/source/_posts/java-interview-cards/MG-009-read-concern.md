---
title: "[MG-009] 副本集·read concern（读关注）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 副本集 · read concern（读关注）

- **事实**：读关注 local 读本机最新（可能被回滚）、majority 读已确认数据、linearizable 线性一致
- **原理**：local 快但读到未多数派确认写，majority 一致，linearizable 最强最慢需配 w:majority
- **常见误区**：
  1. local 与 majority 相同（错）
  2. linearizable 是默认值（错）
  3. read concern 影响写入（错）
- **工程用法**：读一致性与延迟权衡
- **版本锚点**：官方文档
