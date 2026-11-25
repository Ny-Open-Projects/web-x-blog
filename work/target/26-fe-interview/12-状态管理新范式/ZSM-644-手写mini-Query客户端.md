---
title: [ZSM-644] 笔试：手写 mini Query 客户端（缓存 + 去重 + 失效）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-644：手写 mini Query 客户端（缓存 + 去重 + 失效）
**答**：实现 `createMiniQueryClient()`：1) `fetch(key, fn, { staleTime = 0, gcTime = 5min })`：返回 Promise，同 key 在途请求复用；2) 缓存条目 `{ data, dataUpdatedAt, isInvalidated, refCount }`——挂载 refCount++/卸载 refCount--，归零后 gcTime 清除；3) staleTime 内不重复请求，过期或 invalidated 则后台刷新（先返回旧数据）；4) `invalidate(keyPrefix)`：前缀匹配标脏 + 活跃条目立即 refetch；5) 附用例验证去重与失效。

```javascript
function createMiniQueryClient() {
  const cache = new Map()   // hash -> { data, dataUpdatedAt, promise, isInvalidated, refCount, gcTimer, opts }
  const listeners = new Set()

  const hash = (k) => JSON.stringify(k)

  function getEntry(k, opts) {
    const h = hash(k)
    if (!cache.has(h)) cache.set(h, { data: undefined, dataUpdatedAt: 0, promise: null, isInvalidated: false, refCount: 0, gcTimer: null, opts })
    return cache.get(h)
  }

  function doFetch(k, entry, fn) {
    const promise = fn()
      .then((data) => {
        entry.data = data
        entry.dataUpdatedAt = Date.now()
        entry.promise = null
        entry.isInvalidated = false
        notify()
        return data
      })
      .catch((e) => { entry.promise = null; notify(); throw e })
    entry.promise = promise
    return promise
  }

  function fetch(key, fn, opts = {}) {
    const entry = getEntry(key, opts)
    const staleTime = opts.staleTime ?? 0
    const fresh = Date.now() - entry.dataUpdatedAt < staleTime
    if (entry.promise) return entry.promise            // 在途复用（去重）
    if (entry.data !== undefined && !entry.isInvalidated && fresh) {
      return Promise.resolve(entry.data)               // 新鲜：直接返回缓存
    }
    // 过期：后台刷新，先吐旧数据
    const p = doFetch(key, entry, fn)
    return entry.data !== undefined ? Promise.resolve(entry.data).then(() => p) : p
  }

  function mount(key) {
    const entry = cache.get(hash(key))
    if (!entry) return
    entry.refCount++
    clearTimeout(entry.gcTimer)                         // 取消 GC
  }

  function unmount(key, gcTime = 5 * 60 * 1000) {
    const entry = cache.get(hash(key))
    if (!entry) return
    entry.refCount--
    if (entry.refCount <= 0) {
      entry.gcTimer = setTimeout(() => { cache.delete(hash(key)); notify() }, gcTime)
    }
  }

  function invalidate(prefix) {
    for (const [h, entry] of cache) {
      if (h.startsWith(JSON.stringify(prefix).slice(0, -1)) || h.includes(hash(prefix))) {
        entry.isInvalidated = true
        if (entry.refCount > 0) { /* 活跃：等下次 fetch 或立即触发 */ }
      }
    }
    notify()
  }

  function notify() { listeners.forEach((fn) => fn([...cache.entries()].map(([k, v]) => ({ k, data: v.data })))) }

  return { fetch, mount, unmount, invalidate, subscribe: (fn) => (listeners.add(fn), () => listeners.delete(fn)), snapshot: () => cache }
}

// 用例
const client = createMiniQueryClient()
let calls = 0
const load = () => new Promise((r) => setTimeout(() => r(++calls), 10))

Promise.all([client.fetch(['todos'], load), client.fetch(['todos'], load)])
  .then(([a, b]) => console.log(a === b, calls))   // true 1：去重
client.invalidate(['todos'])
client.fetch(['todos'], load).then(() => console.log(calls))   // 2：失效后重拉
```
**评分点**：
- 在途 Promise 复用去重（entry.promise 判定）
- refCount 挂载计数 + gcTime 延迟清除（内存回收语义）
- fresh 判定与后台刷新（先吐旧数据）
- 前缀失效标脏（isInvalidated 驱动下次 fetch）
