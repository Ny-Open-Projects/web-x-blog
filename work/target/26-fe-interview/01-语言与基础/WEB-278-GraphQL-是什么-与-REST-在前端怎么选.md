---
title: [WEB-278] GraphQL 是什么？与 REST 在前端怎么选？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP]
type: 面试题
---

## WEB-278：GraphQL 是什么？与 REST 在前端怎么选？

**答**：
- GraphQL：客户端声明式指定需要的字段，服务端按查询返回精确结构。核心优势——一次请求取齐多个资源（告别 REST 的多次关联请求）、无 over-fetching（不返回冗余字段）、schema 即文档（强类型，前端 codegen 生成类型）。
- 组成：Query（查）/Mutation（改）/Subscription（订阅），入口只有一个 endpoint，POST query 文本。
- 前端配套：Apollo Client / urql / Relay（缓存规范化、乐观更新、分页）。
- 选型：前端形态多变（多端共用一个 BFF）、接口字段冗余严重、组件数据需求细碎 → GraphQL；接口少而稳定、团队小、缓存简单 → REST 更省心。
- 风险点：N+1 查询（用 DataLoader 解决）、复杂查询拖垮服务端（深度限制/复杂度限制）、HTTP 缓存语义弱化。

```javascript
const QUERY = `
  query ProductPage($id: ID!) {
    product(id: $id) {
      title price
      reviews(first: 10) { author stars }   # 关联数据一次取齐
    }
  }`;
const { data } = await client.query({ query: QUERY, variables: { id } });
// REST 可能需要 /product/:id + /product/:id/reviews 两次请求
```
