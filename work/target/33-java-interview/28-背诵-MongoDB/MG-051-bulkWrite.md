---
title: "[MG-051] 写入·bulkWrite（批量）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 写入 · bulkWrite（批量）

- **事实**：批量写入 bulkWrite（ordered/unordered）与 insertMany
- **原理**：unordered 并行执行更快（失败集合适用），ordered 顺序执行遇错停止，大批量导入必用
- **常见误区**：
  1. bulkWrite 自动并行（错）
  2. ordered 更快（错）
  3. 批量写入无事务性（错）
- **工程用法**：数据导入性能
- **版本锚点**：官方文档
