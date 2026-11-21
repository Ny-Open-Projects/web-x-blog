---
title: "[SP-040] AOP·@Order（排序）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## AOP · @Order（排序）

- **事实**：多个切面的执行顺序由 @Order 值决定数字越小优先级越高
- **原理**：事务切面 Order 默认 Ordered.LOWEST_PRECEDENCE，自定义切面想包在事务外需要更小值（先进入后退出）
- **常见误区**：
  1. @Order 数字越大优先级越高（错）
  2. 未标注 @Order 的切面先执行（错）
  3. @Order 可以加在方法参数上（错）
- **工程用法**：切面叠加时的执行矩阵
- **版本锚点**：Spring 文档
