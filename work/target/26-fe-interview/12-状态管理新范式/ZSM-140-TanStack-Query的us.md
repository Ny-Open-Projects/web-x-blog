---
title: [ZSM-140] 动态数量的请求怎么并行发？useQueries 和 Promise.all 的区别是什么？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-140：动态数量的请求怎么并行发？useQueries 和 Promise.all 的区别是什么？
**答**：
- 一个组件里要发「数量不定的多个查询」（如每个仓库一条状态），useQueries 接收 query 描述数组，返回与输入等长对齐的结果数组，每项仍是完整 Query 状态。
- 与 Promise.all 的本质区别：useQueries 每个查询独立缓存（可单独失效/复用/重试）、独立 error（一个失败不影响其他）、update 单项不整体重渲染；Promise.all 是一次性调用，一败俱败且不进缓存。
- 数组元素可用 `enabled: !!id` 过滤未就绪项；`combine` 选项（v5）可把多项聚合成一个派生值，减少组件重渲染。
- 追问钩子：串行依赖用依赖查询（085 已覆盖）或多级 useQuery 的 enabled 链，不要在 queryFn 里手写 await 链（缓存粒度变粗）。

```javascript
import { useQueries } from '@tanstack/react-query'

function RepoBadges({ repoIds }) {
  const results = useQueries({
    queries: repoIds.map(id => ({
      queryKey: ['repo', id],
      queryFn: () => api.repo(id),
      enabled: !!id,
      staleTime: 60_000,
    })),
    combine: (rs) => ({                       // 聚合派生，单项更新才重渲染
      loading: rs.some(r => r.isLoading),
      badges: rs.map((r, i) => ({ id: repoIds[i], stars: r.data?.stars ?? 0 })),
    }),
  })

  if (results.loading) return <Skeleton/>
  return results.badges.map(b => <Badge key={b.id} {...b}/>)
}
```
