---
title: [ALG-159] 手写一个 SWR（stale-while-revalidate）缓存：有缓存先返回旧数据立即渲染，同时后台静默更新，更新完触发回调刷新视图？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-159：手写一个 SWR（stale-while-revalidate）缓存：有缓存先返回旧数据立即渲染，同时后台静默更新，更新完触发回调刷新视图？
**答**：三级判断：① 缓存新鲜（未过 TTL）直接返回；② 有缓存但过期——先同步返回旧数据，再后台发请求，完成后写缓存并通知订阅者；③ 无缓存——发起请求并挂到缓存槽（进行中的 Promise 也要能被复用，与 singleflight 合流）。核心是"返回旧值"与"触发更新"是两条独立路径。时间 O(1)，空间 O(key 数)。

```javascript
function createSWR(key, fetcher, { ttl = 60000 } = {}) {
  const cache = new Map(); // key -> { data, ts, promise }
  const listeners = new Set();
  return {
    on(fn) { listeners.add(fn); return () => listeners.delete(fn); },
    async get() {
      const hit = cache.get(key);
      if (hit && Date.now() - hit.ts < ttl) return hit.data;      // 1. 新鲜直接回
      if (hit && hit.promise) return hit.promise;                 // 2. 请求进行中复用
      if (hit) {
        // 3. 有旧数据：先回旧值，后台静默 revalidate
        const p = fetcher()
          .then(d => { cache.set(key, { data: d, ts: Date.now() }); })
          .finally(() => { const h = cache.get(key); delete h.promise; listeners.forEach(f => f(h.data)); });
        cache.set(key, { ...hit, promise: p });
        return hit.data;                    // 先渲染旧数据
      }
      // 4. 无缓存：发请求，Promise 也挂进缓存供复用
      const p = fetcher().then(d => { cache.set(key, { data: d, ts: Date.now() }); return d; });
      cache.set(key, { promise: p });
      return p;
    },
  };
}
```
