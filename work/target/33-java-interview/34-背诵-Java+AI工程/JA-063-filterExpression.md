---
title: "[JA-063] Spring AI·filterExpression（向量）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · filterExpression（向量）

- **事实**：SearchRequest.filterExpression 支持元数据过滤（如 type == 'news'）缩小检索范围
- **原理**：向量库层过滤（先过滤后近邻）比检索后业务过滤高效，元数据随 Document 入库即过滤字段
- **常见误区**：
  1. 过滤只能在业务代码做（错）
  2. filterExpression 是 SQL 语句（错）
  3. 元数据过滤不影响性能（错）
- **工程用法**：多租户类目检索隔离
- **版本锚点**：Spring AI 1.0 GA
