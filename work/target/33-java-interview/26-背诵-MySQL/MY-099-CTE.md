---
title: "[MY-099] SQL·CTE（CTE）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## SQL · CTE（CTE）

- **事实**：CTE（with 子句）与递归 CTE 处理树形/图遍历查询
- **原理**：递归 CTE（with recursive）查组织架构/评论树替代应用层递归，深度控制防死循环，是 8.0 复杂查询利器
- **常见误区**：
  1. 递归 CTE 无法终止（错）
  2. CTE 是临时表别名（是命名查询可递归）（错）
  3. 树查询只能应用层实现（错）
- **工程用法**：层级数据查询方案
- **版本锚点**：MySQL 8.0
