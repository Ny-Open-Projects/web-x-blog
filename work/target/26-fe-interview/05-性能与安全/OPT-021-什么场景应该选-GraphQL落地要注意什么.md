---
title: [OPT-021] 什么场景应该选 GraphQL？落地要注意什么？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-021：什么场景应该选 GraphQL？落地要注意什么？

**答**：
- 优势：客户端按需声明字段（避免多取/少取）、一次请求取多资源、schema 即文档，适合多端差异化取数的场景。
- 成本：HTTP 缓存失效（POST 单端点）、查询深度需要防护（复杂度限制/maxDepth）、N+1 问题要用 DataLoader 批量化。
- 若页面数据形状固定、缓存诉求强，REST + BFF 聚合往往更简单；不要为了技术选 GraphQL。
- 落地组合：Apollo/urql 客户端 + DataLoader resolver + persisted query（把查询语句固化，省流量且便于 CDN 缓存）。

```javascript
// 一一对应：GraphQL resolver 中用 DataLoader 解决 N+1
import { ApolloServer } from '@apollo/server';
import DataLoader from 'dataloader';

// 假设 getAuthorsByIds 底层是一条 WHERE id IN (...) 的批量查询
const authorLoader = new DataLoader(async (ids) => {
  const rows = await db.query('SELECT * FROM author WHERE id = ANY($1)', [ids]);
  // DataLoader 要求按入参顺序返回，做一次对齐
  return ids.map((id) => rows.find((r) => r.id === id) ?? null);
});

const typeDefs = `
  type Book { id: ID! title: String author: Author }
  type Author { id: ID! name: String }
  type Query { books: [Book!]! }
`;

const resolvers = {
  Query: { books: () => db.query('SELECT * FROM book') },
  Book: {
    author: (book) => authorLoader.load(book.authorId), // 100 本书只发 1 次批量查询
  },
};

new ApolloServer({ typeDefs, resolvers });
```
