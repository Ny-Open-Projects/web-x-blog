---
title: [V3-404] 笔试：手写接口数据的多级缓存（内存 → sessionStorage → 网络）
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-404：笔试：手写接口数据的多级缓存（内存 → sessionStorage → 网络）
**答**：实现 `cachedFetch(url, { ttl = 60_000 })`：L1 内存 Map（带 TTL）、L2 sessionStorage（TTL + 时间戳）、L3 网络；命中低层要回填上层；同一 URL 并发请求去重。

```javascript
const mem = new Map()
function cachedFetch(url, { ttl = 60_000 } = {}) {
  if (inflight.has(url)) return inflight.get(url)
  const p = (async () => {
    const now = Date.now()
    const l1 = mem.get(url)
    if (l1 && now - l1.t < ttl) return l1.data
    const l2raw = sessionStorage.getItem('c:' + url)
    if (l2raw) {
      const { t, data } = JSON.parse(l2raw)
      if (now - t < ttl) { mem.set(url, { t, data }); return data } // 回填 L1
    }
    const res = await fetch(url)
    if (!res.ok) throw new Error('fetch failed')
    const data = await res.json()
    mem.set(url, { t: now, data })
    try { sessionStorage.setItem('c:' + url, JSON.stringify({ t: now, data })) } catch {} // 超配额忽略
    return data
  })().finally(() => inflight.delete(url))
  inflight.set(url, p)
  return p
}
const inflight = new Map()
function invalidate(url) {
  mem.delete(url); sessionStorage.removeItem('c:' + url)
}
```
**评分点**：
- TTL 三层一致判断 + 命中低层回填高层。
- inflight 去重（finally 清理）。
- sessionStorage 超配额 try/catch。
- 提供 invalidate 主动失效入口。
