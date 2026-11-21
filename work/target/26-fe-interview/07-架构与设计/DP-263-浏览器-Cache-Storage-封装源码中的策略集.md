---
title: [DP-263] 源码识别：SW 缓存封装源码中的策略集（cache-first 等）？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-263：源码识别：SW 缓存封装源码中的策略集？
**答**:
- 策略模式（教科书级）：cache-first/network-first/stale-while-revalidate/cache-only/network-only——同 respond(request) 接口不同策略，按路由注入（workbox 的 registerRoute）。
- 备忘录：Cache Storage 是持久化备忘录；缓存版本化（caches.open('v1')）支持整批失效。
- 状态机：install → waiting → activating → active（双 SW 并存的版本切换状态机）。
- 识别要点：能说清"HTML 用 network-first（保新鲜）、静态资源 cache-first（immutable）"的选型理由。

```javascript
// workbox 风格策略注册
const strategies = {
  cacheFirst: async (req, cacheName) => {
    const cache = await caches.open(cacheName);
    return (await cache.match(req)) ?? fetchAndPut(req, cache);
  },
  networkFirst: async (req, cacheName) => {
    const cache = await caches.open(cacheName);
    try { const res = await fetch(req); cache.put(req, res.clone()); return res; }
    catch { return await cache.match(req); }                  // 网络失败回缓存
  },
  swr: async (req, cacheName) => {
    const cache = await caches.open(cacheName);
    const cached = await cache.match(req);
    const net = fetch(req).then(res => { cache.put(req, res.clone()); return res; });
    return cached ?? net;                                     // 立即给缓存，后台刷新
  },
};
self.addEventListener('fetch', e => {
  const url = new URL(e.request.url);
  if (url.pathname.startsWith('/api/')) e.respondWith(strategies.networkFirst(e.request, 'api'));
  else if (/\.(js|css|png)$/.test(url.pathname)) e.respondWith(strategies.cacheFirst(e.request, 'assets'));
  else if (e.request.mode === 'navigate') e.respondWith(strategies.swr(e.request, 'pages'));
});
```
