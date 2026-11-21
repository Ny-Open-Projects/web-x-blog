---
title: [WEB-264] Service Worker 缓存策略：三种经典模式
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 缓存]
type: 面试题
---

## WEB-264：Service Worker 缓存策略：三种经典模式

**答**：
- Cache First：命中缓存直接返回，适合带版本 hash 的静态资源（不会变，无需验证）。
- Network First：先网络，失败回退缓存，适合 HTML/API——保证新鲜度又支持离线兜底。
- Stale-While-Revalidate：立即回缓存（快），同时后台拉新缓存供下次用，适合可容忍一版延迟的资源（字体、低频接口）。
- 关键细节：SW 更新有生命周期（skipWaiting/clients.claim 控制立即生效）；缓存版本号命名 + activate 时清理旧缓存；sw.js 本身必须 no-cache。
- 安全限制：必须 HTTPS（localhost 除外）；作用域由 sw.js 路径决定，控制全站要放根目录。

```javascript
const CACHE = 'app-v3';
self.addEventListener('fetch', (e) => {
  const { request } = e;
  if (request.headers.get('accept')?.includes('text/html')) {
    // Network First（HTML）
    e.respondWith(fetch(request).then(res => {
      caches.open(CACHE).then(c => c.put(request, res.clone()));
      return res.clone();
    }).catch(() => caches.match(request)));
    return;
  }
  // Cache First（带 hash 静态资源）
  e.respondWith(caches.match(request).then(hit => hit ||
    fetch(request).then(res => {
      caches.open(CACHE).then(c => c.put(request, res.clone()));
      return res.clone();
    })));
});
self.addEventListener('activate', (e) => e.waitUntil(
  caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
));
```
