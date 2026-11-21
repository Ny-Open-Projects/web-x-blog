---
title: [DP-134] 如何用缓存代理实现请求缓存装饰器？SWR 策略怎么加？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-134：如何用缓存代理实现请求缓存装饰器？SWR 策略怎么加？（高频）
**答**：
- 最小实现：高阶函数包住 async 请求，Map 按 key（URL+参数序列化）缓存 Promise 本身——缓存 Promise 天然解决并发去重（同 key 同时发起只发一次）。
- SWR（stale-while-revalidate）：先同步返回旧值提升体感，再后台刷新替换——`useSWR` 的核心机制，本质是缓存代理 + 观察者。
- 失效治理：写操作后按资源前缀失效（invalidate 前缀匹配），避免脏读；TTL 兜底防缓存无限增长。

```javascript
// 缓存代理：缓存的是 Promise，并发自动去重
function withCache(fn, { ttl = 30_000, keyFn = (...args) => JSON.stringify(args) } = {}) {
  const store = new Map();                                    // key → { promise, at }
  const wrapped = (...args) => {
    const key = keyFn(...args);
    const hit = store.get(key);
    if (hit && Date.now() - hit.at < ttl) return hit.promise; // TTL 内直接命中
    const promise = fn(...args).catch((e) => { store.delete(key); throw e; }); // 失败即失效
    store.set(key, { promise, at: Date.now() });
    return promise;
  };
  wrapped.invalidate = (prefix = '') => {                     // 失效入口：写后调用
    for (const key of store.keys()) if (key.includes(prefix)) store.delete(key);
  };
  wrapped.revalidate = async (...args) => {                   // SWR：旧值先返，后台刷新
    const key = keyFn(...args);
    const stale = store.get(key)?.promise;
    const fresh = wrapped(...args);                           // 触发后台更新
    if (stale) return { stale: await stale, fresh };
    return { stale: await fresh, fresh };
  };
  return wrapped;
}
const getUserCached = withCache((id) => http.get(`/users/${id}`), { ttl: 60_000 });
const p1 = getUserCached(1), p2 = getUserCached(1);           // 同一 Promise，只发一次请求
console.log(p1 === p2);                                       // true
await saveUser(user);
getUserCached.invalidate('/users/');                          // 写后失效
```
