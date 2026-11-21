---
title: [PER-089] HTTP 缓存与 Service Worker 如何组合成策略矩阵？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-089：HTTP 缓存与 Service Worker 如何组合成策略矩阵？

**答**：
- 分工：HTTP 缓存是**浏览器与源站/CDN** 之间的机制，SW 缓存是**页面可控**的一层，能做策略编排（先网后缓、先缓后网、预取）。
- 策略矩阵：带 hash 的静态资源 **Cache-First（一年强缓存）**；HTML **Network-First**（保证发版即生效）+ SW 兜底离线；API 数据 **Stale-While-Revalidate**（先给旧值再后台更新）；字体图片 Cache-First。
- SW 的独特价值：离线可用、精确的失败降级、预缓存下一跳资源、上报缓存命中率。
- 注意版本迁移：旧 SW 要 `self.skipWaiting()` + 客户端 `clients.claim()`，缓存命名带版本号，activate 时清理旧版本。

```javascript
// Service Worker：按资源类型的缓存策略矩阵
const CACHE = 'app-v42';
const PRECACHE = ['/', '/offline.html', '/fonts/brand.woff2'];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(PRECACHE)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', (e) => {
  e.waitUntil(caches.keys().then((keys) =>
    Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))) // 清理旧版本
  ).then(() => self.clients.claim()));
});

self.addEventListener('fetch', (e) => {
  const url = new URL(e.request.url);
  const strategy =
    url.pathname.startsWith('/assets/') ? cacheFirst :   // hash 静态资源：缓存优先
    url.pathname === '/' || url.pathname.endsWith('.html') ? networkFirst : // HTML：网络优先
    url.pathname.startsWith('/api/') ? staleWhileRevalidate :              // API：旧值先回后台刷新
    cacheFirst;                                                            // 字体图片等

  e.respondWith(strategy(e.request));
});

async function cacheFirst(req) {
  const hit = await caches.match(req);
  if (hit) return hit;
  const res = await fetch(req);
  if (res.ok) caches.open(CACHE).then((c) => c.put(req, res.clone()));
  return res;
}

async function networkFirst(req) {
  try {
    const res = await fetch(req);
    caches.open(CACHE).then((c) => c.put(req, res.clone()));
    return res;
  } catch {
    return (await caches.match(req)) ?? caches.match('/offline.html'); // 离线兜底页
  }
}

async function staleWhileRevalidate(req) {
  const hit = await caches.match(req);
  const net = fetch(req).then((res) => {
    if (res.ok) caches.open(CACHE).then((c) => c.put(req, res.clone()));
    return res;
  });
  return hit ?? net; // 有旧值立即返回，同时网络刷新缓存
}
```
