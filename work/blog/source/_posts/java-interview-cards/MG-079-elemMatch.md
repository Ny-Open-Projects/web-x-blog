---
title: "[MG-079] 查询·$elemMatch（数组）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 查询 · $elemMatch（数组）

- **事实**：$elemMatch 要求数组元素的多个条件同时满足于同一元素
- **原理**：{scores:{$gte:80,$lte:90}} 是字段级条件（可匹配不同元素），$elemMatch 才是元素级组合条件，数组查询的经典语义陷阱
- **常见误区**：
  1. $gte 与 $lte 组合天然作用于同一元素（错）
  2. elemMatch 与普通条件等价（错）
  3. elemMatch 只能用于数字数组（错）
- **工程用法**：成绩区间/标签组合查询
- **版本锚点**：官方文档
