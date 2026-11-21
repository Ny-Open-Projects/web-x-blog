---
title: [ZSM-147] 怎么把 TanStack Query 缓存持久化到 localStorage？persistQueryClient 的适用场景和坑是什么？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-147：怎么把 TanStack Query 缓存持久化到 localStorage？persistQueryClient 的适用场景和坑是什么？
**答**：
- 用 `persistQueryClient` + `createAsyncStoragePersister`：缓存序列化写 localStorage/IndexedDB，页面刷新后 hydrate 回内存，首屏直接有数据（配 staleTime 才不会立刻重取）。
- 适用：离线可用的 PWA、刷新后不想闪 loading 的重型列表；不适合频繁变化或含敏感信息的数据（token 明文落盘是事故）。
- 坑一：buster（缓存版本号）必须随数据结构升级递增，否则 hydrate 旧结构直接崩；坑二：序列化体积失控，要配 `dehydrateOptions` 只挑白名单 key；坑三：多标签页同时写互相覆盖，需要节流或 IndexedDB。
- 追问钩子：与 service worker 缓存的分工——SW 管 HTTP 层、Query persist 管「应用视角的响应缓存」，两层叠加要防语义冲突。

```javascript
import { persistQueryClient } from '@tanstack/react-query-persist-client'
import { createAsyncStoragePersister } from '@tanstack/query-async-storage-persister'

const persister = createAsyncStoragePersister({
  storage: localStorage,
  key: 'app-query-cache',
  throttleTime: 1000,                    // 写盘节流
})

const queryClient = new QueryClient({
  defaultOptions: {
    queries: { staleTime: 60_000, gcTime: 1000 * 60 * 60 * 24 }, // 持久化要延长 gcTime
  },
})

export function Root() {
  return (
    <PersistQueryClientProvider client={queryClient}
      persistOptions={{ persister, buster: 'v3',   // 结构升级必须换版本号
        dehydrateOptions: {
          shouldDehydrateQuery: (q) => q.queryKey[0] === 'goods-list', // 白名单
        } }}>
      <App/>
    </PersistQueryClientProvider>
  )
}
```
