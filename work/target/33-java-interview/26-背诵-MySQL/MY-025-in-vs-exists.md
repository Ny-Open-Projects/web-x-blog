---
title: "[MY-025] SQL·in vs exists（join）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## SQL · in vs exists（join）

- **事实**：in 与 exists 的选择本质是谁做驱动表：in 外表驱动适合外表小，exists 子表驱动适合外表大
- **原理**：8.0 优化器会自动改写半连接（semi-join），两写法性能差异缩小，重点还是索引是否可用
- **常见误区**：
  1. in 永远比 exists 快（错）
  2. exists 永远比 in 快（错）
  3. 优化器不会改写子查询（错）
- **工程用法**：子查询优化知识
- **版本锚点**：实战共识
