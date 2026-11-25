---
title: [NODE-662] GraphQL 网关（聚合/N+1/Dataloader）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-662：GraphQL 网关怎么做？
**答**：
- 网关模式：schema 聚合（各服务 schema 合并）+ 解析器路由（字段级路由到下游）；查询复杂度限制（depth/complexity 分析——恶意深查询防御，SCN-NODE-641 限流升级）。
- N+1 的解法：Dataloader（批量+缓存——同请求内相同 key 合并为一次 IN）；per-request 实例（Dataloader 必须每请求新建——跨请求缓存会泄露用户数据）。
- 持久查询与安全：APQ（持久查询——客户端只发 hash，防任意查询注入）、禁 introspection（生产）、错误脱敏（不泄露内部堆栈——SCN-NODE-646 日志脱敏同源）。
- 与 BFF 取舍：GraphQL 灵活（端自由取字段）但复杂度高；BFF 显式（每端一接口）但接口膨胀——团队规模与端数量决定。
- 追问钩子：为什么 Dataloader 必须「per-request 实例化」——Dataloader 的缓存（batch 内 memoization）在请求级有效；跨请求复用会把 A 用户的查询结果缓存给 B 用户（数据越权——严重事故）；GraphQL 上下文每请求新建 context → dataloader 挂 context 上——「缓存的作用域 = 授权的作用域」是 GraphQL 安全第一课。

```javascript
app.use('/graphql', graphqlHTTP({ schema, context: () => ({
  loaders: {
    user: new DataLoader(keys => db.userBatch(keys)),  // per-request 实例
  } }),
  validationRules: [depthLimit(10), costAnalysis({ maximumCost: 1000 })],
}));
// APQ：客户端只发 hash
```
