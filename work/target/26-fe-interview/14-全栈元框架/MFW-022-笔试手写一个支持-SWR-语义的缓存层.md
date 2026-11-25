---
title: [MFW-022] 笔试：手写支持 stale-while-revalidate 语义的缓存层
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-022：笔试：手写支持 stale-while-revalidate 语义的缓存层
**答**：实现 `createSWRCache()`：`get(key, fn, { maxAge, swr })`——maxAge 内直接回新鲜值；超过 maxAge 但在 swr 窗口内，**立即返回旧值并后台异步重取**；超过 swr 则同步等待重取。要求同一 key 并发请求只触发一次重取（请求合并），失败不影响返回旧值。

```javascript
function createSWRCache() {
  const store = new Map(); // key -> { value, storedAt, revalidating: Promise|null }

  async function get(key, fn, { maxAge = 30_000, swr = 300_000 } = {}) {
    const entry = store.get(key);
    const now = Date.now();

    if (entry) {
      const age = now - entry.storedAt;
      if (age <= maxAge) return entry.value;            // 新鲜：直接回
      if (age <= swr) {                                  // 陈旧但可接受：回旧值 + 后台刷新
        revalidate(key, fn);
        return entry.value;
      }
    }
    // 无缓存或彻底过期：同步重取（复用 in-flight）
    await revalidate(key, fn);
    return store.get(key).value;
  }

  function revalidate(key, fn) {
    const entry = store.get(key);
    if (entry?.revalidating) return entry.revalidating; // 请求合并：并发只重取一次
    const p = (async () => {
      try {
        const value = await fn();
        store.set(key, { value, storedAt: Date.now(), revalidating: null });
      } catch (err) {
        // 失败：保留旧值继续可用（不删除），仅记录
        console.error(`[swr] revalidate ${key} failed:`, err.message);
        if (entry) entry.revalidating = null;
        throw err;
      }
    })();
    if (entry) entry.revalidating = p;
    else store.set(key, { value: undefined, storedAt: 0, revalidating: p });
    return p;
  }

  return { get };
}

// ---- 行为示例 ----
const cache = createSWRCache();
const v1 = await cache.get('feed', fetchFeed, { maxAge: 10_000, swr: 60_000 });
// 10s 内：瞬时返回；10~60s：瞬时返回旧值+后台刷新；>60s：等新值

// **评分点**
// 1. 三档语义清晰：fresh（同步回）/ stale-while-revalidate（回旧+后台）/ miss（同步重取）。
// 2. in-flight 请求合并：并发 get 同 key 只发一次重取（存 revalidating Promise）。
// 3. 后台重取失败不影响旧值可用，且清除 revalidating 标记可再次重试。
// 4. 后台刷新用 void/fire-and-forget 且不阻塞返回值——很多人会 await 导致 SWR 退化成 miss。
```
