---
title: "[MG-038] 聚合·allowDiskUse（限制）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 聚合 · allowDiskUse（限制）

- **事实**：聚合 $sort/$group 超内存默认报错需 allowDiskUse=true 落盘
- **原理**：100MB 限制防止拖垮节点，落盘性能下降明显，优先优化管道（前置 match/拆分阶段）
- **常见误区**：
  1. allowDiskUse 默认开启（错）
  2. 超内存自动降级不报错（错）
  3. 落盘对性能无影响（错）
- **工程用法**：聚合错误排查
- **版本锚点**：官方文档
