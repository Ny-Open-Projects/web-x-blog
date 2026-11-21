---
title: [NODE-049] GraphQL 作为 BFF 怎么用？DataLoader 如何解决 N+1？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-049：GraphQL 作为 BFF 怎么用？DataLoader 如何解决 N+1？
**答**：
- GraphQL BFF：前端一个查询拿到整棵所需数据（按需取字段天然解决裁剪）；schema 即文档，resolver 决定数据来源；`@apollo/server` 或 `graphql-yoga` 起服务。
- **N+1 问题**：查询 10 个作者的名字+文章，默认 resolver 会对每个作者单独查一次文章（1 + 10 次）。**DataLoader** 用"批处理 + 请求级缓存"解决：同一事件循环 tick 内的请求合并为一次批量查询（`WHERE id IN (...)`），且同一 id 重复请求命中缓存。
- 高频追问：GraphQL 的其他坑——查询深度/复杂度限制（防恶意深嵌套打挂服务）、缓存较难（POST 请求难走 HTTP 缓存）、错误不区分状态码。

```javascript
const { ApolloServer } = require('@apollo/server');
const { startStandaloneServer } = require('@apollo/server/standalone');
const DataLoader = require('dataloader');

const typeDefs = `#graphql
  type Author { id: ID!, name: String!, posts: [Post!]! }
  type Post { id: ID!, title: String!, author: Author! }
  type Query { authors: [Author!]! }
`;

// 批量查询函数：一次 IN 查询代替 N 次
const batchAuthors = async (ids) => {
  const rows = await db.query('SELECT * FROM authors WHERE id IN (?)', [ids]);
  // 关键：必须按传入顺序返回，缺失的槽位返回 null
  return ids.map((id) => rows.find((r) => r.id === id) || null);
};

const resolvers = {
  Query: { authors: () => db.query('SELECT * FROM authors') },
  Author: {
    // 每个作者的 posts 本应各查一次 → N+1
    posts: (author, _args, ctx) => ctx.postLoader.load(author.id),
  },
};

// Apollo 中间件：每个请求创建独立的 DataLoader（缓存不可跨请求）
const server = new ApolloServer({
  typeDefs,
  resolvers,
});
const { url } = await startStandaloneServer(server, {
  context: async () => ({
    postLoader: new DataLoader(async (authorIds) => {
      const rows = await db.query(
        'SELECT * FROM posts WHERE author_id IN (?)', [authorIds]);
      return authorIds.map((aid) => rows.filter((r) => r.author_id === aid));
    }),
  }),
});
// 查询 { authors { name posts { title } } } → SQL 只有 2 条：authors 全查 + posts IN 批查
```
