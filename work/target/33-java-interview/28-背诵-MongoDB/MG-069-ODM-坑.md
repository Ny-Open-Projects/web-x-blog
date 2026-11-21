---
title: "[MG-069] Java·ODM 坑（ODM）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Java · ODM 坑（ODM）

- **事实**：ODM（Spring Data/Mongoose）掩盖文档模型本质，P10 应能脱离 ODM 直谈文档设计
- **原理**：ODM 的 @Document/@Field 映射隐藏 BSON 结构，复杂聚合仍要原生管道，建模评审用原生文档视角
- **常见误区**：
  1. ODM 是必需的（错）
  2. ODM 自动优化查询（错）
  3. 脱离 ODM 无法开发（错）
- **工程用法**：技术深度分水岭
- **版本锚点**：实战共识
