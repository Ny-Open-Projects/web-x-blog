---
title: [PER-1075] 手写一个 API 缓存封装：TTL + 写失效 + SWR
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1075：手写一个 API 缓存封装：TTL + 写失效 + SWR

**答**：
- 需求：实现 createAPICache(ttlMs)。get(key, fetcher) 返回 { value, fromCache }：命中未过期直接返回；过期返回旧值（fromCache: true）并后台刷新；无缓存请求并存储。invalidate(prefix) 删除匹配键。set(key, value) 手动写入。getAllKeys() 输出当前键列表。
- 边界：fetcher 抛错时若有旧值返回旧值并上报；后台刷新失败静默；同一 key 并发刷新合并为一次。
- 评分点：TTL 判断；SWR 旧值+后台刷新；刷新合并；前缀失效

```javascript
function createAPICache(ttlMs = 60_000) {
  const store = new Map(); const refreshing = new Set();
  async function get(key, fetcher) {
    const hit = store.get(key);
    if (hit && Date.now() - hit.t < ttlMs)
      return { value: hit.v, fromCache: true };
    if (hit) {                                     // 过期：SWR
      if (!refreshing.has(key)) {
        refreshing.add(key);
        fetcher().then(v => store.set(key, { v, t: Date.now() }))
          .catch(e => report({ type: 'swr-refresh-fail', key, msg: e.message }))
          .finally(() => refreshing.delete(key));
      }
      return { value: hit.v, fromCache: true };
    }
    try {
      const v = await fetcher();
      store.set(key, { v, t: Date.now() });
      return { value: v, fromCache: false };
    } catch (e) { throw e; }                       // 无旧值只能抛
  }
  return {
    get,
    set: (key, v) => store.set(key, { v, t: Date.now() }),
    invalidate: prefix => {
      for (const k of [...store.keys()])
        if (k.startsWith(prefix)) store.delete(k);
    },
    getAllKeys: () => [...store.keys()],
  };
}
```
