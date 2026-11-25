---
title: [WEB-028] 如何用 Service Worker + Cache Storage 实现可编程缓存？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-028：如何用 Service Worker + Cache Storage 实现可编程缓存？
**答**：
- Service Worker 是运行在页面之外的脚本，能拦截同源页面发出的所有请求，缓存策略由代码决定。
- 常见策略：Cache First 适合静态资源与字体；Network First 适合接口数据；Stale-While-Revalidate 先给旧值再后台更新。
- 缓存有版本化与清理问题：新版本 SW 安装后要删除旧缓存，否则体积无限膨胀。
- SW 只能拦截 HTTPS（localhost 除外）页面下的请求，作用域由脚本路径决定。

```javascript
// sw.js：三种策略并存的可编程缓存
const CACHE_V = 'app-cache-v2';
const PRECACHE = ['/index.html', '/static/app.js', '/static/app.css'];

self.addEventListener('install', (event) => {
  event.waitUntil(caches.open(CACHE_V).then((c) => c.addAll(PRECACHE)));
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_V).map((k) => caches.delete(k)))
    )
  );
});

self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);

  if (url.pathname.startsWith('/api/')) {
    // 接口：Network First，断网时兜底旧数据
    event.respondWith(
      fetch(event.request)
        .then((res) => {
          const copy = res.clone();
          caches.open(CACHE_V).then((c) => c.put(event.request, copy));
          return res;
        })
        .catch(() => caches.match(event.request))
    );
  } else {
    // 静态资源：Cache First，未命中才走网络
    event.respondWith(
      caches.match(event.request).then(
        (cached) =>
          cached ||
          fetch(event.request).then((res) => {
            const copy = res.clone();
            caches.open(CACHE_V).then((c) => c.put(event.request, copy));
            return res;
          })
      )
    );
  }
});
```

```javascript
// 页面侧注册 Service Worker
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js', { scope: '/' }).then((reg) => {
      console.log('SW registered, scope:', reg.scope);
    });
  });
}
```

## 五、Cookie 与 Web Storage
