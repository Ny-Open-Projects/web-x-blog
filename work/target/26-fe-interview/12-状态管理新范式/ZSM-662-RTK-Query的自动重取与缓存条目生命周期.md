---
title: [ZSM-662] RTK Query 的缓存条目生命周期：subscription refCount 与 keepUnusedDataFor
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-662：RTK Query 的缓存条目生命周期：subscription refCount 与 keepUnusedDataFor

**答**：
- RTK Query 的缓存条目（QueryCacheEntry）生命周期与 TanStack Query 高度同构：组件挂载 `initiate` → subscriptionCount++；无引用后 `keepUnusedDataFor`（默认 60s）计时，到期移除条目。所有数据以普通 Redux state 形态存在（`state.api.queries`），这让 DevTools/时间旅行/持久化「免费获得」。
- 自动重取决策与 TanStack 差异：RTK Query 默认 `refetchOnMountOrArgChange: false`（挂载用缓存，不管新旧），TanStack 默认 staleTime: 0（挂载必拉）——迁移时这个默认值差异是最大的行为坑。策略参数对应关系：`staleTime → refetchOnMountOrArgChange（秒数）`、`gcTime → keepUnusedDataFor`、`refetchOnFocus → refetchOnFocus`。
- **参数变更 = 新条目**：同 endpoint 不同 args 各自缓存条目（`getPosts({page:1})` 与 `({page:2})` 独立）—— invalidateTags 或手动 refetch 才批量更新。
- pollingInterval：条目级的定时 refetch（实时行情类）——挂载期间每 N 秒拉，unmount 停；与 WS 推送选型：轮询简单但延迟大，推送实时但要处理重连/追平（ZSM-646）。
- 追问钩子：RTK Query 的状态在 Redux store 里可见——可以 dispatch `api.util.selectInvalidatedBy` / `updateQueryData`（乐观更新官方 API）做精细控制，这是它与 TanStack（非 Redux 生态）最大的差异点。

```javascript
import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'

export const api = createApi({
  reducerPath: 'api',
  baseQuery: fetchBaseQuery({ baseUrl: '/api' }),
  tagTypes: ['Post'],
  endpoints: (builder) => ({
    getPosts: builder.query({
      query: (page) => `/posts?page=${page}`,
      providesTags: (result, error, page) => result?.map((p) => ({ type: 'Post', id: p.id })) ?? [],
      keepUnusedDataFor: 120,          // 无人引用保留 120s（默认 60）
      refetchOnMountOrArgChange: 300,  // 挂载/参数变化超 5 分钟才重拉
      pollingInterval: 30000,          // 挂载期间 30s 轮询
    }),
    updatePost: builder.mutation({
      query: ({ id, ...patch }) => ({ url: `/posts/${id}`, method: 'PATCH', body: patch }),
      invalidatesTags: (r, e, { id }) => [{ type: 'Post', id }],
      // 乐观更新：官方 API updateQueryData
      onQueryStarted: async ({ id, ...patch }, { dispatch, queryFulfilled }) => {
        const undo = dispatch(api.util.updateQueryData('getPosts', undefined, (draft) => {
          const p = draft.find((x) => x.id === id)
          if (p) Object.assign(p, patch)
        }))
        try { await queryFulfilled } catch { undo.undo() }   // 失败回滚
      },
    }),
  }),
})
```
