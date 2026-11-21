---
title: "[MG-025] explain·COLLSCAN（解读）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## explain · COLLSCAN（解读）

- **事实**：explain 关键计划：COLLSCAN 全集合扫（红灯）、IXSCAN 索引扫、FETCH 回表
- **原理**：与 MySQL explain 思路同构，totalDocsExamined 与 nReturned 比值是效率指标，1:1 为理想
- **常见误区**：
  1. COLLSCAN 表示用集合扫描优化（错）
  2. IXSCAN 一定快（错）
  3. FETCH 就是磁盘读（错）
- **工程用法**：查询调优入口
- **版本锚点**：官方文档
