---
title: [DP-324] 笔试题：手写 SW 缓存策略（cache-first + swr）？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-324：笔试题：手写 SW 缓存策略（cache-first + swr）？
**题目**：在 Service Worker 实现路由级策略：1) 静态资源 cache-first；2) HTML stale-while-revalidate；3) API network-first；4) 缓存版本化与 activate 清理旧缓存。
**评分点**：
- 策略实现正确（三种响应来源）。
- swr 不阻塞当前响应（缓存立即返回+后台刷新）。
- activate 清理旧版本缓存（保留当前）。
- respondWith 请求 clone 语义正确（res.clone() 再 put）。
```javascript
const CACHE = 'app-v1';
self.addEventListener('install', e => e.waitUntil(caches.open(CACHE)));
self.addEventListener('activate', e => e.waitUntil(
  caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))));  // 4)
self.addEventListener('fetch', e => {
  const url = new URL(e.request.url);
  if (/\.(js|css|png|woff2)$/.test(url.pathname))
    return e.respondWith(cacheFirst(e.request));            // 1)
  if (e.request.mode === 'navigate')
    return e.respondWith(staleWhileRevalidate(e.request));  // 2)
  if (url.pathname.startsWith('/api/'))
    return e.respondWith(networkFirst(e.request));          // 3)
});
async function cacheFirst(req) {
  return (await caches.match(req)) ?? fetch(req);
}
async function networkFirst(req) {
  try { const res = await fetch(req); return res; }
  catch { return await caches.match(req) ?? new Response('offline', { status: 503 }); }
}
async function staleWhileRevalidate(req) {
  const cache = await caches.open(CACHE);
  const cached = await cache.match(req);
  const net = fetch(req).then(res => { cache.put(req, res.clone()); return res; });  // 4) clone
  return cached ?? net;
}
```
