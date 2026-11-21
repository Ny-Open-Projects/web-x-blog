---
title: [MFW-048] 笔试：手写带 TTL 与请求合并的客户端预取缓存
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-048：笔试：手写带 TTL 与请求合并的客户端预取缓存
**题目**：实现 `createPrefetchCache()`：`prefetch(key, fn)` 立即发起（in-flight 合并）；`read(key)` 返回值或 Promise——TTL 内返回缓存值；过期且有缓存值则返回旧值并后台刷新（SWR）；无缓存则等待 fn。`clear(prefix)` 按前缀批量失效；页面卸载自动清空（提供 dispose）。

```javascript
function createPrefetchCache({ ttl = 30_000 } = {}) {
  const store = new Map(); // key -> { value?, promise?, storedAt }
  let disposed = false;

  function prefetch(key, fn) {
    if (disposed) throw new Error('cache disposed');
    const cur = store.get(key);
    if (cur?.promise || (cur?.value && Date.now() - cur.storedAt < ttl)) return cur.promise;
    const promise = Promise.resolve()
      .then(fn)
      .then((value) => { entry.value = value; entry.storedAt = Date.now(); entry.promise = null; return value; })
      .catch((err) => { store.delete(key); throw err; }); // 失败清占位
    const entry = { promise, value: undefined, storedAt: 0 };
    store.set(key, entry);
    return promise;
  }

  function read(key, fn) {
    const cur = store.get(key);
    if (cur?.value) {
      const fresh = Date.now() - cur.storedAt < ttl;
      if (!fresh) prefetch(key, fn);      // 过期：回旧值 + 后台刷新（SWR）
      return cur.value;
    }
    return prefetch(key, fn);             // 无缓存：等待发起中的请求（合并）
  }

  function clear(prefix) {
    for (const k of store.keys()) {
      if (k.startsWith(prefix)) store.delete(k);
    }
  }

  function dispose() { store.clear(); disposed = true; } // 路由卸载时调用

  return { prefetch, read, clear, dispose };
}

// **评分点**
// 1. in-flight 合并：promise 挂在 entry 上，prefetch/read 复用同一 Promise。
// 2. SWR 三态：fresh 直回 / stale 回旧+后台刷 / miss 等 fn。
// 3. clear(prefix) 前缀批量失效——分页列表 key 形如 orders:3，翻页后 clear('orders:')。
// 4. dispose 防泄漏：路由切换后旧缓存不再持有引用， disposed 后再调用要报错。
```
