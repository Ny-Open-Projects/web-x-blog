---
title: [FRP-163] SWR 的 mutate 与数据 reconcile 是怎么做的？乱序响应如何防护？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-163：SWR 的 mutate 与数据 reconcile 是怎么做的？乱序响应如何防护？

**答**：
- SWR 的缓存同样是 `Map<key, { data, isValidating, timestamp }>`；`mutate(key, updater, opts)` 可本地改值——`revalidate: false` 纯本地，默认"先改 + 后台 revalidate"。
- reconcile 的关键：请求返回后**只在数据"比缓存新"时替换**——用 `timestamp/请求序号` 对比，丢弃过期响应（stale response 保护）。
- `dedupingInterval`（默认 2s）：同 key 在窗口内的多次请求去重；`keepPreviousData` 让 key 切换时保留旧数据避免闪空。
- 对比 TanStack：SWR 更薄（无 gcTime/观察者计数，缓存常驻）， TanStack 有完整的查询生命周期——选型差异由此而来。

```javascript
// 简化实现，帮助理解 SWR 的 mutate 与乱序防护
const cache = new Map();  // key -> { data, timestamp, isValidating }
const keyListeners = new Map();
let requestSeq = 0;

function useSWR(key, fetcher) {
  const entry = cache.get(key);
  const shouldFetch = !entry || Date.now() - entry.timestamp > DEDUPING_INTERVAL;
  if (shouldFetch && !entry?.isValidating) {
    const seq = ++requestSeq;                    // 请求序号
    cache.set(key, { ...entry, isValidating: true });
    fetcher(key).then(data => {
      const cur = cache.get(key);
      // reconcile 核心：只接受"不早于当前缓存"的响应
      if (seq >= (cur.seq ?? 0)) {
        cache.set(key, { data, timestamp: Date.now(), isValidating: false, seq });
        notify(key);
      } // else：过期响应，直接丢弃
    });
  }
  return { data: entry?.data, isValidating: entry?.isValidating };
}

function mutate(key, updater, { revalidate = true } = {}) {
  const entry = cache.get(key);
  const next = typeof updater === 'function' ? updater(entry?.data) : updater;
  if (next !== undefined) {
    cache.set(key, { data: next, timestamp: Date.now(), seq: requestSeq + 1 });
    notify(key);                                 // 本地立即生效
  }
  if (revalidate) {
    // 后台 revalidate：完成后的 reconcile 会用真值校正本地改动
    fetcher(key).then(data => { cache.set(key, { data, timestamp: Date.now() }); notify(key); });
  }
}

// 乱序防护演示：
// t0: mutate('user', { name: '本地改动' })
// t1: revalidate 请求 A 发出
// t2: 另一组件也触发请求 B（更晚发出）
// t3: A 先返回（旧数据）-> seq 检查失败 -> 丢弃，不覆盖
// t4: B 返回（新数据）-> seq 通过 -> 上屏
```
