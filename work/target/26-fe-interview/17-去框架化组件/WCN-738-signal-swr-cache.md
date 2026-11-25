---
title: [WCN-738] Signals 与 SWR/请求缓存（stale-while-revalidate）如何结合？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-738：Signals 与 SWR/请求缓存（stale-while-revalidate）如何结合？

**答**：
- 结论：用 signal 存缓存数据，用 computed 派生「是否过期」；读取时若 stale 则后台 revalidate，成功写回 signal 触发细粒度更新；用 key 做请求去重与缓存分区。
- 竞态用 epoch/AbortController 治理，避免旧响应覆盖；错误与 loading 用独立 signal；支持乐观更新（先写缓存再发请求，失败回滚）。
- 追问钩子：多个组件同时请求同一 key 如何只发一个请求？考察「请求 Promise 缓存（dedupe）」。

```javascript
const cache = signal(new Map());
const inflight = new Map();
function useSWR(key, fetcher) {
  if (inflight.has(key)) return inflight.get(key);   // 请求去重
  const p = fetcher(key).then((data) => {
    const m = new Map(cache.value); m.set(key, { data, t: Date.now() });
    cache.value = m;                                 // 写回触发更新
    inflight.delete(key);
    return data;
  });
  inflight.set(key, p);
  return p;
}
const stale = (entry, ttl = 5000) => !entry || Date.now() - entry.t > ttl;
console.log(typeof useSWR, 'stale 判定:', stale({ t: 0 }));
```
