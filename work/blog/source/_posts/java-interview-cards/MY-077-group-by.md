---
title: "[MY-077] SQL·group by（分组）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## SQL · group by（分组）

- **事实**：group by 无索引时走临时表+排序（8.0 默认不排序了），group by 结果需要 order by 显式声明
- **原理**：8.0 起 group by 不再隐式排序（5.7 隐式按分组列排序），依赖旧行为的 SQL 升级后出 Bug
- **常见误区**：
  1. group by 结果总是有序（错）
  2. 8.0 group by 隐式排序（错）
  3. 临时表与排序不能同时出现（错）
- **工程用法**：版本升级兼容性知识点
- **版本锚点**：MySQL 8.0
