---
title: "[MY-023] SQL·NLJ（join）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## SQL · NLJ（join）

- **事实**：join 实现：Nested-Loop Join 逐行驱动被驱动表（有索引走 Index NLJ）
- **原理**：驱动表每行到被驱动表查一次（走索引则很快），无可用索引时 Block NLJ 用 join buffer 缓存驱动表批量匹配，8.0.18 起无索引等值 join 可用 Hash Join
- **常见误区**：
  1. join 一定是笛卡尔积（错）
  2. BNL 比 NLJ 更快（错）
  3. 8.0 没有 hash join（错）
- **工程用法**：join 性能分析基础
- **版本锚点**：MySQL 8.0.18
