---
title: [ZSM-111] SWR 的 dedupingInterval 去重是怎么实现的？缓存会不会无限增长怎么治理？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-111：SWR 的 dedupingInterval 去重是怎么实现的？缓存会不会无限增长怎么治理？
**答**：
- 去重实现：同 key 的 revalidate 请求在 dedupingInterval（默认 2000ms）窗口内共享同一个 in-flight Promise，新订阅者直接挂在这个 Promise 上，不发真实网络请求。
- 缓存增长治理：SWR 默认不自动 GC，长生命周期大列表会撑内存；手段有三——key 里固定分页范围、路由卸载后不再访问的缓存可用 `provider` 换成带 LRU 的自定义缓存、大对象存前先做字段裁剪。
- 自定义 provider 实现 Map 接口（get/set/delete/keys）即可全量替换默认 WeakMap 式缓存，是 SWR 高级考点。
- 追问钩子：对比 TanStack Query 的 gcTime 自动回收，SWR 需要显式治理，这常被当成选型减分项，要能主动说出对策。

```javascript
import { cache } from 'swr'
import { LRUCache } from 'lru-native'

// 自定义带容量上限的缓存 provider
const lru = new LRUCache({ max: 500 })

export const swrProvider = {
  get: (key) => lru.get(key),
  set: (key, value) => lru.set(key, value),
  delete: (key) => lru.delete(key),
  keys: () => lru.keys(),
}

// <SWRConfig value={{ provider: () => swrProvider }}>

// 字段裁剪：只留列表需要的列，避免整对象进缓存
export const listFetcher = async (url) => {
  const raw = await fetcher(url)
  return raw.items.map(({ id, title, cover }) => ({ id, title, cover }))
}
```
