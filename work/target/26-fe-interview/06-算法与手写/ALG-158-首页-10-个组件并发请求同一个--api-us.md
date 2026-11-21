---
title: [ALG-158] 首页 10 个组件并发请求同一个 `/api/user/info`，接口瞬间被打 10 次（缓存击穿）。如何用 singleflight 合并？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-158：首页 10 个组件并发请求同一个 `/api/user/info`，接口瞬间被打 10 次（缓存击穿）。如何用 singleflight 合并？
**答**：singleflight：以请求 key 为索引，第一个请求发起后把 Promise 存入 `inflight` Map，后续同 key 请求直接复用这个 Promise；请求 settle（成功或失败）后在 finally 删除，放行下一次。这样并发塌缩成 1 个网络请求，所有调用方拿到同一结果/同一异常。时间 O(1) 每次 load，空间 O(进行中的 key 数)。

```javascript
function createSingleflight() {
  const inflight = new Map(); // key -> 进行中的 Promise
  return async function load(key, fetcher) {
    if (inflight.has(key)) return inflight.get(key); // 并发请求合并成同一次
    const p = (async () => {
      try {
        return await fetcher();
      } finally {
        inflight.delete(key); // 成功失败都放行，下一次重新发起
      }
    })();
    inflight.set(key, p);
    return p;
  };
}
const loadUser = createSingleflight();
// 首页 10 个组件同时 loadUser('user:me', () => fetch('/api/user/info'))
// => 实际只发 1 个网络请求，10 个调用方共享结果
```
