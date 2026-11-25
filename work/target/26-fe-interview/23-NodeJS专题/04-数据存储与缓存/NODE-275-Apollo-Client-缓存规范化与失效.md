---
title: [NODE-275] Apollo Client 缓存规范化与失效？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-275：Apollo Client 缓存规范化与失效？
**答**:
- 规范化缓存：响应按 __typename:id 拆实体存储，查询结果是实体引用图——同实体多处引用（列表+详情）改一处全更新（ARC-054 normalizr 同款）。
- 失效路径：mutation 后 refetchQueries（粗）vs cache.modify（细，直接改实体）vs 标签失效（服务端配合 NODE-265）。
- 分页缓存：fetchMore merge 函数定义"新页怎么并进已有列表"——cursor 语义在 merge 里实现。
- GC：实体无引用后自动清理（inMemoryCache 的引用计数）。

```typescript
// 规范化写入与细粒度失效
cache.modify({
  id: cache.identify({ __typename: 'Post', id: postId }),
  fields: {
    likes(cached = 0) { return cached + 1; },            // 细粒度：只改这个字段
  },
});
// 分页 merge：
cache.modify({
  fields: {
    feed(existing = [], { toReference, readField }) {
      return [...existing, ...newPage.map(p => toReference(p))];   // 追加语义
    },
  },
});
// 粗粒度：await refetchQueries({ include: ['Feed'] }) —— 简单但流量大
```
