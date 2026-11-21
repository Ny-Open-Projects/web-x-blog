---
title: "[MG-083] 调优·executionStats（explain）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 调优 · executionStats（explain）

- **事实**：explain executionStats 三层：queryPlanner（计划）→executionStats（实际执行）→allPlansExecution（计划对比）
- **原理**：executionStats 给出 totalKeysExamined/totalDocsExamined/nReturned 三比值与执行时间，是判断索引效率的硬数据，普通 explain 只做预估
- **常见误区**：
  1. explain 默认执行查询（错）
  2. nReturned 等于 docsExamined 是正常（1:1 才理想）（错）
  3. explain 无性能开销（错）
- **工程用法**：慢查询定位标准动作
- **版本锚点**：官方文档
