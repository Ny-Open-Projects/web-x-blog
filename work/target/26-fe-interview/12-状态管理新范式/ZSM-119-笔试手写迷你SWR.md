---
title: [ZSM-119] 笔试：手写迷你 SWR 核心（缓存 + 去重 + stale-while-revalidate + mutate）
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-119：手写迷你 SWR 核心（缓存 + 去重 + stale-while-revalidate + mutate）
**答**：实现 `useSWR(key, fetcher, options)`，要求：1) 缓存命中先返回旧数据（stale）；2) dedupingInterval 内同 key 请求合并；3) `mutate(key, data?)` 支持写缓存/失效重取/函数式更新；4) key 变化时返回对应缓存。边界：key 为 null 不请求；fetcher 抛错不影响已有缓存；多组件订阅同 key 同步更新。用 React 实现核心逻辑即可。

```javascript
const cache = new Map()      // key -> data
const inflight = new Map()   // key -> Promise
const listeners = new Map()  // key -> Set<fn>

function emit(key, data) {
  cache.set(key, data)
  listeners.get(key)?.forEach(fn => fn(data))
}

export function useSWR(key, fetcher, { dedupingInterval = 2000 } = {}) {
  const [data, setData] = useState(key ? cache.get(key) : undefined)
  useEffect(() => {
    if (!key) { setData(undefined); return }
    setData(cache.get(key))                       // 切 key 先取缓存
    if (!listeners.has(key)) listeners.set(key, new Set())
    listeners.get(key).add(setData)
    revalidate(key, fetcher, dedupingInterval)    // 触发验证
    return () => { listeners.get(key)?.delete(setData) }
  }, [key])
  return { data }
}

function revalidate(key, fetcher, dedupingInterval) {
  if (inflight.has(key)) return inflight.get(key)   // 去重：复用进行中请求
  const p = Promise.resolve(fetcher(key))
    .then(d => { emit(key, d); return d })
    .catch(() => {})                                // 失败不动缓存
    .finally(() => inflight.delete(key))
  inflight.set(key, p)
  return p
}

export function mutate(key, data, { revalidate: rerun = false } = {}) {
  if (typeof data === 'function') data = data(cache.get(key)) // 函数式更新
  if (data !== undefined) emit(key, data)
  if (rerun) inflight.delete(key)                   // 允许重新请求
  return data !== undefined ? Promise.resolve(data) : Promise.resolve()
}

// 评分点：
// 1. 缓存/inflight/listeners 三张 Map 的职责划分是否清晰
// 2. stale 先渲染：mount 时立即读缓存，不等 revalidate
// 3. 去重窗口：inflight 命中直接复用 Promise，不发网络请求
// 4. mutate 三形态：写缓存 / 函数式 / 失效重取，均广播订阅者
// 5. 卸载清理 listeners，防止泄漏与对已卸载组件 setState
```
