---
title: "[MG-010] 副本集·oplog（复制）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 副本集 · oplog（复制）

- **事实**：副本集复制靠 oplog（固定容量循环覆盖的操作日志）从库拉取回放
- **原理**：oplog 是 capped collection，从库异步回放，回放完成度决定读一致性，oplog 窗口是从库落后容忍上限
- **常见误区**：
  1. oplog 是无限增长日志（错）
  2. 复制是同步的（错）
  3. oplog 记录文档级 diff（statement 级）（错）
- **工程用法**：副本集复制原理骨架
- **版本锚点**：官方文档
