---
title: [ZSM-101] SWR 是什么？它和 TanStack Query 的定位与取舍有什么不同？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-101：SWR 是什么？它和 TanStack Query 的定位与取舍有什么不同？
**答**：
- SWR 是 Vercel 出的服务端状态 Hook，核心口号 stale-while-revalidate：先返回缓存旧数据（stale），再后台重新验证（revalidate），用户零等待看到内容，回来后自动更新。
- 机制上 SWR 极简：靠 key 全局缓存 Map + getter/setter，请求去重（同 key 并发只发一次）、焦点重验证、断网重连重验证都是内置默认行为。
- 与 TanStack Query 的取舍：SWR 体量小、API 少（useSWR / mutate / useSWRInfinite 三件套）适合中小应用；TanStack Query 的 staleTime/gcTime 分离、mutation 体系、devtools、乐观更新工具链更完整，适合重服务端交互的中后台。
- 一句话定位：SWR 是「缓存优先的取数 Hook」，TanStack Query 是「服务端状态管理框架」，面试时先说清自己项目里选了哪个、为什么。

```javascript
import useSWR from 'swr'

const fetcher = (url) => fetch(url).then(r => {
  if (!r.ok) throw new Error(r.status)     // 和 Query 一样：不能吞错
  return r.json()
})

function GoodsList() {
  // key 必须稳定：参数拼进 key 才能按参数缓存
  const { data, error, isLoading, isValidating } = useSWR(
    '/api/goods?page=1', fetcher,
    { revalidateOnFocus: true, dedupingInterval: 2000 }
  )
  if (isLoading) return <Spinner/>
  if (error) return <ErrorView retry={() => mutate('/api/goods?page=1')}/>
  // data 先给缓存旧值（stale），SWR 同时后台重取，回来无感刷新
  return <List items={data} refreshing={isValidating}/>
}
```
