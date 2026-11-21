---
title: [ZSM-066] TanStack Query 是什么？它把「服务端状态」当作什么来管理？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-066：TanStack Query 是什么？它把「服务端状态」当作什么来管理？
**答**：
- TanStack Query（React Query）是异步状态管理器，把服务端数据当作**缓存（cache）**而非「复制进本地 store 的状态」。
- 核心抽象：queryKey 唯一标识一份数据 → useQuery 按 key 读写缓存 → 数据有「新鲜度（staleTime）」和「存活期（gcTime）」两个独立时钟。
- 自动处理：请求去重（同 key 并发合并）、窗口聚焦重取、重连重取、失败重试、后台静默刷新（stale-while-revalidate）。
- 写操作用 useMutation，成功后用 invalidateQueries 声明「哪些缓存不新鲜了」，Query 负责择机刷新——数据流从「手动搬数据」变为「声明依赖」。
- 追问钩子：所以「要不要把接口数据放 Redux」在新范式下答案默认是「不要」。

```javascript
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
const qc = useQueryClient()

// 读：key = ['goods', keyword]
const { data, isPending, error } = useQuery({
  queryKey: ['goods', keyword],
  queryFn: () => api.goods(keyword),
})
// 写：成功后失效，不手动搬数据
const add = useMutation({
  mutationFn: api.addGoods,
  onSuccess: () => qc.invalidateQueries({ queryKey: ['goods'] }),
})
```
