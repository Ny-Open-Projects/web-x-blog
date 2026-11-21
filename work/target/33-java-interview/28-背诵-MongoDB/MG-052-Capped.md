---
title: "[MG-052] 集合·Capped（Capped）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 集合 · Capped（Capped）

- **事实**：Capped collection 固定大小循环覆盖（日志/最新消息场景）
- **原理**：写入顺序保留自动淘汰旧文档，无索引开销（除 _id），oplog 就是 capped 的实现，size 满后新写覆盖旧数据
- **常见误区**：
  1. Capped 自动扩容（错）
  2. Capped 支持任意更新（错）
  3. Capped 是 4.2 新特性（错）
- **工程用法**：固定容量日志场景
- **版本锚点**：官方文档
