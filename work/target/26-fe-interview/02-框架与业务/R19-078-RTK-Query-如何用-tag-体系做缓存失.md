---
title: [R19-078] RTK Query 如何用 tag 体系做缓存失效？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-078：RTK Query 如何用 tag 体系做缓存失效？
**答**：
- 服务端状态的核心难题不是"存"，而是"写之后读怎么办"：RTK Query 用 providesTags / invalidatesTags 声明依赖关系。
- 列表查询提供 `LIST` 标签 + 每条数据的 `{type, id}` 标签；新增使 LIST 失效，点赞只失效单条。
- 失效后 RTK Query 自动 refetch 活跃订阅，组件层零手动逻辑。
- 对比手写 Zustand + fetch：不用自己维护"改完列表要不要刷新"的时序问题。

```typescript
// api.ts —— RTK Query 用 tag 体系声明缓存关系
import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

export const api = createApi({
  baseQuery: fetchBaseQuery({ baseUrl: '/api' }),
  tagTypes: ['Post'],
  endpoints: builder => ({
    getPosts: builder.query<Post[], void>({
      query: () => 'posts',
      providesTags: result =>
        result
          ? [...result.map(p => ({ type: 'Post' as const, id: p.id })), { type: 'Post', id: 'LIST' }]
          : [{ type: 'Post', id: 'LIST' }],
    }),
    addPost: builder.mutation<Post, NewPost>({
      query: body => ({ url: 'posts', method: 'POST', body }),
      invalidatesTags: [{ type: 'Post', id: 'LIST' }],   // 新增后 LIST 失效自动 refetch
    }),
    likePost: builder.mutation<Post, string>({
      query: id => ({ url: `posts/${id}/like`, method: 'POST' }),
      invalidatesTags: (r, e, id) => [{ type: 'Post', id }], // 精确失效单条
    }),
  }),
});
```
