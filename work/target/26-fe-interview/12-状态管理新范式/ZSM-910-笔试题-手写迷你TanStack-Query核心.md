---
title: [910] 笔试手写：实现迷你 useQuery（缓存+竞态+staleTime）
date: 2026-11-17
categories: [状态管理新范式]
tags: [前端面试, 笔试题, TanStack Query, 手写]
type: 笔试题
---

## 910：笔试手写：实现迷你 useQuery（缓存+竞态+staleTime）

**答**：实现 createMiniQuery()：返回 { useQuery(key, fn, { staleTime=0 }) }。缓存项 { data, updatedAt, promise }；挂载时：缓存新鲜（now-updatedAt < staleTime）直接返回；否则 inflight promise 复用，无则发起并存储 promise；resolve 后更新缓存并通知订阅者。旧 promise resolve 不覆盖已被替换的 key（竞态）。

```js
function createMiniQuery() {
  const cache = new Map();   // hash -> { data, updatedAt, promise }
  const subs = new Map();    // hash -> Set<rerender>
  function ensure(hash, fn, staleTime) {
    let e = cache.get(hash);
    if (e && Date.now() - e.updatedAt < staleTime) return e.data;
    if (e?.promise) return e.data ?? null;    // inflight 复用
    const p = Promise.resolve(fn())
      .then(data => {
        const cur = cache.get(hash);
        if (cur?.promise !== p) return;       // 竞态：已换新 promise
        cache.set(hash, { data, updatedAt: Date.now(), promise: null });
        (subs.get(hash) || []).forEach(f => f());
      });
    cache.set(hash, { ...e, promise: p, data: e?.data ?? null });
    return cache.get(hash).data;
  }
  return { useQuery(key, fn, opt = {}) {
    const hash = JSON.stringify(key);
    const [, force] = useReducer(x => x + 1, 0);
    if (!subs.has(hash)) subs.set(hash, new Set());
    subs.get(hash).add(force);
    useEffect(() => () => subs.get(hash).delete(force), []);   // 退订
    const data = ensure(hash, fn, opt.staleTime ?? 0);
    return { data, isLoading: data === undefined };
  } };
}
```

**评分点**：
- inflight promise 复用（同 key 并发挂载只发一次）
- 竞态防护：resolve 时校验「自己还是当前 promise」
- staleTime 新鲜度判断；订阅退订防泄漏
- 能讨论：真实库的额外层次（gc/重试/乐观更新/devtools）

