---
title: [WEB-613] 笔试：手写 navigationPreload 集成封装
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 笔试题, 浏览器架构]
type: 笔试题
---

## WEB-613：笔试：手写 navigationPreload 集成封装

**答**：实现 SW 的 navigationPreload 集成：① activate 时开启 preload 并缓存开启状态；② fetch 事件对 navigation 请求：优先 `e.preloadResponse`，超时 3s 未就绪回退自行 fetch；③ preload 响应与缓存命中策略组合：缓存新鲜（<60s）直接回缓存，否则用 preload 响应；④ 统计每条路径的 preload 命中率（存 IndexedDB，activate 时上报）；⑤ preloadResponse 失败静默回退。写出核心实现。

```javascript
// sw.js
self.addEventListener('activate', (e) => {
  e.waitUntil((async () => {
    await self.registration.navigationPreload.enable();
    await reportStats(); // activate 时机上报上一周期命中率
  })());
});

self.addEventListener('fetch', (e) => {
  if (e.request.mode !== 'navigate') return;
  e.respondWith((async () => {
    const cached = await caches.match(e.request);
    const cachedAt = await getCacheTime(e.request.url);
    if (cached && Date.now() - cachedAt < 60_000) return cached; // 新鲜缓存优先

    // preload 与 3s 超时竞速
    const pre = await Promise.race([
      e.preloadResponse.catch(() => null),
      new Promise(r => setTimeout(() => r(null), 3000)),
    ]);
    if (pre) { bumpStat(e.request.url, 'hit'); return pre; }
    bumpStat(e.request.url, 'miss');
    try { return await fetch(e.request); }
    catch { return caches.match('/offline.html'); }
  })());
});
```

**评分点**：
- enable 在 activate 时机正确；preloadResponse 仅对 navigation 请求存在
- 缓存新鲜度与 preload 的优先级组合策略清晰
- 超时竞速回退自行 fetch，preload 失败静默降级
- 命中率统计 + activate 上报，形成可观测闭环
