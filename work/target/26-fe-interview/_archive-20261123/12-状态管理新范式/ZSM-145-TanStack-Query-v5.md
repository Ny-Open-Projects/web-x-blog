---
title: [ZSM-145] TanStack Query v4 升 v5 有哪些破坏性变更？迁移清单怎么列？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-145：TanStack Query v4 升 v5 有哪些破坏性变更？迁移清单怎么列？
**答**：
- 对象签名强制：`useQuery(key, fn, opts)` 改为 `useQuery({ queryKey, queryFn, ...opts })`，codemod 可批量改。
- 状态改名：isLoading → isPending（isLoading 保留为组合标志）；缓存时间配置 cacheTime → gcTime。
- useInfiniteQuery 必填 `initialPageParam`，getPrevious/NextPageParam 行为调整（支持 maxPages 双向）。
- keepPreviousData 选项移除，改为 `placeholderData: keepPreviousData`（import 工具函数）；回调 onChange/onSuccess 移除——副作用改用 useEffect 或 mutation 回调，这是迁移时最容易漏的一项。
- 迁移方法：官方 codemod 起步 + TS 编译错误清单兜底 + 关键路径回归，单独列出「移除的回调」人工排查。

```javascript
// v4 → v5 逐项对照
// v4:
// useQuery(['goods', id], () => api.goods(id), { cacheTime: 60_000,
//   keepPreviousData: true, onSuccess: (d) => log(d) })
// v5:
import { keepPreviousData } from '@tanstack/react-query'

useQuery({
  queryKey: ['goods', id],
  queryFn: () => api.goods(id),
  gcTime: 60_000,                       // cacheTime → gcTime
  placeholderData: keepPreviousData,    // keepPreviousData 选项 → placeholderData
})
// onSuccess 移除：改副作用
useEffect(() => { if (data) log(data) }, [data])
```
