---
title: "[MY-020] explain·explain analyze（analyze）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## explain · explain analyze（analyze）

- **事实**：explain analyze（8.0.18+）真实执行并报告每算子实际耗时与行数
- **原理**：普通 explain 是优化器预估可能骗人，analyze 给出实际执行计划与耗时分布，是 SQL 优化利器
- **常见误区**：
  1. explain analyze 只做预估不执行（错）
  2. 它比普通 explain 更快（错）
  3. 8.0 之前就有该功能（错）
- **工程用法**：疑难 SQL 优化第一步
- **版本锚点**：MySQL 8.0.18
