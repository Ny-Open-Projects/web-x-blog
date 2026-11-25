---
title: [NODE-261] GraphQL 在 BFF 中的正确用法？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-261：GraphQL 在 BFF 中的正确用法？
**答**：
- BFF 网关模式：GraphQL server 只做 schema 拼装与 resolver 聚合，下游仍是 REST/gRPC 微服务——前端一次查询拿裁剪后的数据（NODE-049 延伸到架构层）。
- 核心收益：字段级裁剪（移动端拿小 payload）+ 聚合（N+1 由 DataLoader 解决）+ schema 即契约（NODE-254 呼应）。
- 反模式：把 GraphQL 当内部服务间协议（服务间用 REST 更简单）；resolver 里无缓存直接打下游（放大 10 倍请求）。
- 治理要点：query 深度/复杂度限制、persisted query（白名单 query hash）、schema 注册表版本管理。

```javascript
// DataLoader 防 N+1（BFF 聚合核心）
import DataLoader from 'dataloader';
const userLoader = new DataLoader(async (ids: string[]) => {
  const users = await userService.batchGet(ids);      // 一次批量
  return ids.map(id => users.find(u => u.id === id) ?? null);
});
// resolver：N 个 order 各要 user → 合并为一次 batchGet
const resolvers = {
  Order: { user: (order) => userLoader.load(order.userId) },   // DataLoader 请求内去重+合批
};
// 复杂度限制
import depthLimit from 'graphql-depth-limit';
new ApolloServer({ validationRules: [depthLimit(5), queryComplexity({ maximumComplexity: 1000 })] });
```
