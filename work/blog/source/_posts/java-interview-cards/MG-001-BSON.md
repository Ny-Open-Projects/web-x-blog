---
title: "[MG-001] 文档模型·BSON（基础）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 文档模型 · BSON（基础）

- **事实**：MongoDB 数据单位是 BSON 文档（二进制 JSON）单文档上限 16MB
- **原理**：BSON 支持嵌套文档与数组字段，无固定 schema，字段按需存在，与关系模型的行最大差异
- **常见误区**：
  1. BSON 就是 JSON 没有区别（错）
  2. 单文档无上限（错）
  3. 文档必须有相同字段（错）
- **工程用法**：建模思维的转换起点
- **版本锚点**：官方文档
