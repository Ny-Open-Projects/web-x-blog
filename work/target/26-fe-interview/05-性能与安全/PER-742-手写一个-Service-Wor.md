---
title: [PER-742] 手写一个 Service Worker 多策略缓存路由：按 URL 分类应用 cache-first/network-first/SWR，带离线回退
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-742：手写一个 Service Worker 多策略缓存路由：按 URL 分类应用 cache-first/network-first/SWR，带离线回退

**答**：
- 实现：`fetch` 事件里按路由表匹配策略——静态 hash 资源 cache-first、API network-first（AbortController 3s 超时回退缓存）、图片 SWR（缓存先回 + 后台更新）；未匹配走网络；导航请求 fallback 到 precache 的 App Shell（离线可用）。
- 要点：缓存命名分桶（runtime-static/runtime-api/runtime-img）便于清理；缓存条数上限（图片 200 条 LRU）；超时回退不能 abort 已缓存的慢请求重复发送。
- 边界：POST 请求不缓存；Range 请求（视频）不拦（透传）；版本升级清理旧缓存（activate 时删非当前版本）。
- 评分点：分桶缓存与 Range 透传。

```javascript

const VERSION = 'v7';
const ROUTES = [
  { match: /\.(js|css|woff2)$/, strategy: 'cacheFirst', bucket: 'static' },
  { match: /\/api\//, strategy: 'networkFirst', bucket: 'api', timeout: 3000 },
  { match: /\.(png|webp|avif|jpg)$/, strategy: 'swr', bucket: 'img', max: 200 },
];
self.addEventListener('fetch', (e) => {
  const url = new URL(e.request.url);
  if (e.request.method !== 'GET' || e.request.headers.has('range')) return;  // POST/Range 透传
  const rule = ROUTES.find(r => r.match.test(url.pathname));
  if (rule) e.respondWith(handle(e.request, rule));
  else if (e.request.mode === 'navigate')
    e.respondWith(caches.match('/shell.html'));                 // 离线导航回退 App Shell
});
async function handle(req, { strategy, bucket, timeout, max }) {
  const cache = await caches.open(`${VERSION}-${bucket}`);
  if (strategy === 'cacheFirst') {
    const hit = await cache.match(req);
    return hit ?? netAndCache(req, cache);
  }
  if (strategy === 'networkFirst') {
    try {
      const res = await withTimeout(fetch(req), timeout);
      cache.put(req, res.clone());
      return res;
    } catch { return (await cache.match(req)) ?? Response.error(); }
  }
  // SWR：缓存先回 + 后台更新
  const hit = await cache.match(req);
  const refresh = netAndCache(req, cache).catch(() => {});
  return hit ?? refresh;
}
async function netAndCache(req, cache) {
  const res = await fetch(req);
  if (res.ok) { await cache.put(req, res.clone()); trimCache(cache, 200); } // LRU 上限
  return res;
}
self.addEventListener('activate', (e) => e.waitUntil(
  caches.keys().then(keys =>
    Promise.all(keys.filter(k => !k.startsWith(VERSION)).map(k => caches.delete(k)))))); // 旧版清理
```
