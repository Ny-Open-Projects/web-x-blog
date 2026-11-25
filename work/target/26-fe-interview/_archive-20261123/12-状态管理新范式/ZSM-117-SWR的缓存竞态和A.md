---
title: [ZSM-117] SWR 怎么防止快速切换参数时的响应竞态？AbortController 什么时候该用？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-117：SWR 怎么防止快速切换参数时的响应竞态？AbortController 什么时候该用？
**答**：
- 竞态场景：搜索框连续输入，先发的慢请求后返回，把新关键词的结果覆盖掉。SWR 对同 key 去重解决了并发，但 key 随参数变化时旧 key 的响应仍可能晚到。
- SWR 的第一道防线：组件卸载或 key 变化后，旧 key 响应不会写进新 key 的缓存（按 key 隔离），所以缓存层天然安全；风险在于 fetcher 内部自行 setState 的写法。
- 正解：fetcher 不做任何副作用，渲染完全由 useSWR 返回值驱动；确需取消真实请求省带宽时，fetcher 里用 AbortController，SWR 会在 key 变化时通过 AbortSignal 取消。
- 追问钩子：能说清「竞态的本质是响应与请求的 key 不匹配」比背 API 更加分。

```javascript
import useSWR from 'swr'

// fetcher 接收 SWR 传入的 AbortSignal（v2 支持 { signal }）
const searchFetcher = ([url, signal]) => fetch(url, { signal }).then(r => r.json())

function SearchBox({ keyword }) {
  const debounced = useDebounce(keyword, 300)      // 先防抖
  const { data, isLoading } = useSWR(
    debounced ? `/api/search?kw=${debounced}` : null,
    ([url, signal]) => searchFetcher([url, signal])
  )
  // data 永远对应「当前 debounced key」，慢响应不会串台
  return <Results items={data?.list ?? []} loading={isLoading}/>
}
```
