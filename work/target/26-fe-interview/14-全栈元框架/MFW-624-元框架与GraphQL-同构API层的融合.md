---
title: [MFW-624] 元框架与 GraphQL：同构 API 层的融合
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-624：元框架与 GraphQL 融合

**答**:
- GraphQL 在 RSC 架构的三个落点：1) **server 组件直接调 GraphQL**（fetch GraphQL API——RSC 是 BFF 的 GraphQL client RBL-550）；2) **/graphql route handler**（暴露自己的 GraphQL 端点—— Yoga/helix 集成——RSC 页面也可直调（同进程）；3) client 组件的 GraphQL（urli/apollo client——client 状态层）。
- RSC + GraphQL 的组合语义：RSC 内 GraphQL 查询（server 端去重/缓存 tag——Data Cache 包 GraphQL 响应 RBL-526）；「GraphQL 的 N+1」在 RSC 下的形态：组件各自查 = N 次请求——batching（dataloader/批量端点 RBL-930）。
- 融合的边界：GraphQL server（route handler）与 RSC 数据层重叠——「同进程直调 vs GraphQL 查询」：内部数据 RSC 直调 repo（类型安全 RBL-946）；外部 GraphQL API（第三方）→ RSC 调——「自建数据的直调 × 外部 API 的 GraphQL」混合。
- 追问钩子：为什么「RSC 时代 GraphQL 作为内部 API」的价值下降？——GraphQL 的核心价值：client 自由组合数据（聚合/裁剪/单请求）——RSC server 直调 DB/repo（同进程无网络开销 + 类型直推——不需要 GraphQL 的聚合层）；GraphQL 剩余价值 = 外部多端（RN/第三方——跨网络消费）；「同进程直调 × 跨网络 GraphQL」的混合：内部直调、外部保留 GraphQL——API 层的选择由「消费端与数据的位置关系」决定（RBL-516 tRPC 同理）。

```typescript
// RSC 内 GraphQL（外部 API）
export async function Page({ params }) {
  const data = await fetch(GRAPHQL_URL, {
    method: 'POST', body: JSON.stringify({ query: PRODUCT_QUERY, variables: { id } }),
    next: { tags: [`product:${id}`], revalidate: 60 },   // Data Cache 包 GraphQL RBL-526
  }).then(r => r.json());
  return <Product data={data.product} />;
}
// 自建 GraphQL 端点（route handler）
// app/api/graphql/route.ts
import { createYoga } from 'graphql-yoga';
const yoga = createYoga({ schema, batchingLimit: 10 });
export { POST, GET } = yoga;                             // Next route handler 集成
// N+1 缓解：RSC 组件级查询 → 批量
const batch = new Map();
function batchedQuery(query, vars) {
  batch.set(query + JSON.stringify(vars), null);         // 收集后一次发送（microtask flush）
}
```
