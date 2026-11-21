---
title: [ZSM-096] 笔试：手写迷你 useQuery 核心（缓存 + stale + 去重 + 重试）
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-096：手写迷你 useQuery 核心（缓存 + stale + 去重 + 重试）

**题目要求**：
- 实现 `useQuery({ key, fn, staleTime = 0, retry = 1 })`：按 key 缓存；挂载时若缓存 stale 则请求；同 key 并发请求去重（共享同一个 Promise）；失败按 retry 次数重试。
- 返回 `{ data, isLoading, error, refetch }`；组件卸载不影响缓存。
- 支持 refetch 手动刷新；key 变化自动重取。

```javascript
const cache = new Map() // key(字符串化) → { data, error, ts, promise }
const listeners = new Map()

function emit(k) { (listeners.get(k) || []).forEach(fn => fn()) }

function fetchOnce({ kstr, key, fn, staleTime, retry }) {
  const entry = cache.get(kstr)
  if (entry?.promise) return entry.promise          // 去重：在途复用
  const promise = (async () => {
    for (let i = 0; i <= retry; i++) {
      try {
        const data = await fn()
        cache.set(kstr, { data, ts: Date.now() })   // 写缓存
        emit(kstr)
        return data
      } catch (e) {
        if (i === retry) { cache.set(kstr, { ...(entry||{}), error: e }); emit(kstr); throw e }
        await new Promise(r => setTimeout(r, 1000 * 2 ** i)) // 退避
      }
    }
  })().finally(() => { const e2 = cache.get(kstr); if (e2) e2.promise = undefined })
  cache.set(kstr, { ...(entry ?? {}), promise })
  return promise
}

export function useQuery({ key, fn, staleTime = 0, retry = 1 }) {
  const kstr = JSON.stringify(key)
  const [, force] = useState(0)
  useEffect(() => {
    const l = () => force(n => n + 1)
    const ls = listeners.get(kstr) ?? new Set(); ls.add(l); listeners.set(kstr, ls)
    const entry = cache.get(kstr)
    const fresh = entry && !entry.error && Date.now() - entry.ts < staleTime
    if (!fresh) fetchOnce({ kstr, key, fn, staleTime, retry }).catch(() => {})
    return () => { ls.delete(l) }
  }, [kstr, staleTime, retry])

  const entry = cache.get(kstr)
  return {
    data: entry?.data,
    error: entry?.error,
    isLoading: !entry?.data && !entry?.error,
    refetch: () => fetchOnce({ kstr, key, fn, staleTime, retry }).catch(() => {}),
  }
}
```

**评分点**：
- 缓存 Map + JSON.stringify(key) 结构化标识。
- 在途 promise 去重（entry.promise 复用），完成后清空。
- staleTime 新鲜期判断：新鲜不发请求。
- retry 循环带指数退避；最终失败写入 error 并通知。
- key 变化/重渲染触发重取与订阅清理正确。
