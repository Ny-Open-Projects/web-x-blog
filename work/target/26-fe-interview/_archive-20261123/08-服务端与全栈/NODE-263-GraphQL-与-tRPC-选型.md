---
title: [NODE-263] GraphQL 与 tRPC 的选型？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-263：GraphQL 与 tRPC 的选型？
**答**:
- 决策维度一：客户端形态——多语言/多端（iOS/Android/小程序）→ GraphQL（schema 是中立契约）；纯 TS 全栈 monorepo → tRPC（类型零成本）。
- 维度二：查询灵活性——前端动态拼查询（字段裁剪）→ GraphQL；调用模式固定（RPC 风格）→ tRPC。
- 维度三：生态与治理——GraphQL 有网关生态（federation/缓存策略）与学习成本；tRPC 简单但绑定 Node+TS。
- 组合：对外 GraphQL 联邦、内部 TS 服务间 tRPC/gRPC——两层协议各管一段（NODE-260 阶段 3）。

```javascript
// 选型矩阵
const m = [
  { factor: '多端契约', weight: 3, gql: 5, trpc: 2 },
  { factor: 'TS 全栈类型安全', weight: 3, gql: 3, trpc: 5 },
  { factor: '动态查询/裁剪', weight: 2, gql: 5, trpc: 1 },
  { factor: '学习与治理成本', weight: 2, gql: 2, trpc: 5 },
];
// 结论：BFF 面向多端 → GraphQL；纯 Web monorepo → tRPC
```
