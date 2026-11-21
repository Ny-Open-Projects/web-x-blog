---
title: [ZSM-160] RTK Query 是什么？它和 TanStack Query 同时存在时怎么选、怎么分工？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-160：RTK Query 是什么？它和 TanStack Query 同时存在时怎么选、怎么分工？
**答**：
- RTK Query 是 Redux Toolkit 内置的取数层：createApi 定义 endpoint，自动生成 hooks，数据进 Redux store（归一化 tag 缓存），提供 tagTypes/invalidateTags 失效模型——本质是「Redux 生态内的 Apollo 式缓存」。
- 选型逻辑：项目已重度 Redux（RTK slice、中间件生态、devtools 工作流）→ RTK Query 顺手，缓存与 store 同源；新项目无 Redux 包袱 → TanStack Query 更轻、API 更现代。
- 分工共存（老项目过渡期）：RTK Query 承接 Redux 页面的取数，TanStack Query 承接新模块，二者缓存独立；失效口径要在文档里对齐（同一资源两个缓存必须同一策略，否则各刷各的）。
- 追问钩子：RTK Query 的 tag 失效是「声明式依赖」（providesTags/invalidatesTags），TanStack Query 是「命令式清单」（手动 invalidate），能对比说出两种失效哲学。

```javascript
import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'

export const goodsApi = createApi({
  reducerPath: 'goodsApi',
  baseQuery: fetchBaseQuery({ baseUrl: '/api' }),
  tagTypes: ['Goods'],
  endpoints: (build) => ({
    getGoods: build.query({
      query: (id) => `goods/${id}`,
      providesTags: (r, e, id) => [{ type: 'Goods', id }],   // 声明式缓存依赖
    }),
    updateGoods: build.mutation({
      query: ({ id, patch }) => ({ url: `goods/${id}`, method: 'PATCH', body: patch }),
      invalidatesTags: (r, e, { id }) => [{ type: 'Goods', id }], // 声明式失效
    }),
  }),
})

export const { useGetGoodsQuery, useUpdateGoodsMutation } = goodsApi
```
