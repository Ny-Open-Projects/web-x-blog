---
title: [NODE-312] GraphQL 深水区：N+1 之外的性能问题？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-312：GraphQL 深水区：N+1 之外的性能问题？
**答**:
- N+1 之外四大坑：深层嵌套扇出（depth limit NODE-261）、大对象序列化（字段白名单+分页强制）、resolver 同步阻塞（resolver 里跑重计算）、缓存穿透（无 APQ 任意 query 打爆）。
- 复杂度分析：queryComplexity 按字段成本加权（列表字段成本 ×预计条数）——比 depth 更精确。
- 强制分页：list 字段 schema 层强制 first/limit 上限——防"一次拉全表"。
- 监控：按 operation name 统计耗时/复杂度分布——复杂度高的 op 进治理清单。

```javascript
import { queryComplexity } from 'graphql-query-complexity';
validationRules: [
  queryComplexity({ maximumComplexity: 300,
    estimators: [fieldExtensionsEstimator(), simpleCostEstimator({ scalarCost: 1, objectCost: 2, listFactor: 20 })] }),
],
// list 字段成本放大：posts(cost×20) —— 嵌套两层列表直接超限拒绝
// 强制分页：schema 层
posts(first: Int = 20, after: String): PostConnection!    // first 上限由 resolver clamp 到 100
```
