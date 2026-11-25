---
title: [WCN-739] 笔试：手写 signal + SWR 风格的数据请求缓存 hook
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-739：笔试：手写 signal + SWR 风格的数据请求缓存 hook

**答**：
- 需求：实现 `createSWR(fetcher, ttl)` 返回 `{ get(key), invalidate(key) }`：get 返回缓存数据（Promise），命中且未过期直接返回；过期则后台刷新并返回旧值；同 key 并发只发一个请求；invalidate 清除缓存。
- 要点：用 Map 存 {data,t} 与 inflight；stale 判定用 ttl；后台刷新不阻塞返回；边界：fetcher 抛错时清 inflight 避免永久卡死。

```javascript
function createSWR(fetcher, ttl = 5000) {
  const store = new Map(), inflight = new Map();
  const isStale = (e) => !e || Date.now() - e.t > ttl;
  return {
    get(key) {
      const e = store.get(key);
      if (!isStale(e)) return Promise.resolve(e.data);  // 未过期直接返回
      if (inflight.has(key)) return inflight.get(key);  // 并发去重
      const p = (async () => {
        try {
          const data = await fetcher(key);
          store.set(key, { data, t: Date.now() });
          return data;
        } finally { inflight.delete(key); }             // 失败也清理
      })();
      inflight.set(key, p);
      return e ? Promise.resolve(e.data) : p;           // 有旧值先返回旧值
    },
    invalidate(key) { store.delete(key); },
  };
}
const swr = createSWR(async (k) => k + '!');
console.log(typeof swr.get, typeof swr.invalidate);
```

**评分点**：
- 未过期命中缓存直接返回，过期后台刷新（SWR 语义）。
- 同 key 并发请求去重（inflight Map）。
- fetcher 抛错时 finally 清理 inflight，避免永久 pending。
- invalidate 正确失效，API 简洁可用。
