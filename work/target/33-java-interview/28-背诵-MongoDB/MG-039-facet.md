---
title: "[MG-039] 聚合·$facet（$facet）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 聚合 · $facet（$facet）

- **事实**：$facet 单次管道内分多路输出（同请求多聚合）
- **原理**：一次请求返回多个维度结果（列表+总数+分面统计），内存注意（每路独立），搜索页聚合场景
- **常见误区**：
  1. $facet 自动并行（错）
  2. $facet 是事务的一部分（错）
  3. $facet 结果自动排序（错）
- **工程用法**：搜索页优化技巧
- **版本锚点**：官方文档
