---
title: [MFW-232] Server Component 里接 GraphQL 的正确姿势
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## MFW-232：Server Component 接 GraphQL

**答**:
- RSC 内用 fetch 直接发 GraphQL query（原生缓存语义可用——POST+next.revalidate 需注意 POST 默认不缓存，用 GET 模板化或显式 next: { revalidate }）
- Apollo/urql 这类客户端宿主库在 RSC 内不可用（依赖 Context/订阅）——RSC 用轻量请求函数，客户端组件内再用 Apollo（双客户端共存，边界在 props）
- 缓存对齐难题：GraphQL 无原生 tag——用 @block 字段级 revalidate 需自建映射（query 签名 → tag）或用 persisted query hash 当 tag
- 判定：重 GraphQL 生态（Apollo Client/缓存归一化）→ 客户端主导 + RSC 只出壳；轻 GraphQL → RSC 直连 fetch 保持缓存一致

```javascript
// RSC 内：POST + 显式缓存语义
const res = await fetch(GQL, {
  method: 'POST',
  body: JSON.stringify({ query: POST_QUERY, variables }),
  next: { revalidate: 300, tags: [`post:${id}'] },
})
// tag 策略：persistedQueryHash 作 tag → 按查询失效
```
