---
title: [OPT-126] Service Worker 预缓存关键资源怎么落地，如何处理版本失效？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-126：Service Worker 预缓存关键资源怎么落地，如何处理版本失效？

**答**：
- 预缓存 = 构建期把带 hash 的 JS/CSS/首屏图片清单写进 SW，install 阶段静默拉全量，用户二次访问全部命中 Cache。
- 用 Workbox 的 `precacheAndRoute`：manifest 由构建插件（vite-plugin-pwa / workbox-webpack-plugin）自动生成，hash 变化即自动更新。
- 更新策略：新 SW install 完成后 `skipWaiting` 也要谨慎——资源版本和页面版本可能不一致，常规做法是"新 SW 等 old 控制的页面关闭再接管"，或提示用户刷新。
- 预缓存清单要设体积上限（一般 ≤ 2MB），首屏图片按需 runtime cache 补充。

```javascript
// 一一对应：Workbox 预缓存 + 版本更新策略
import { registerRoute } from 'workbox-routing';
import { precacheAndRoute, createHandlerBoundToURL } from 'workbox-precaching';
import { CacheFirst } from 'workbox-strategies';
import { ExpirationPlugin } from 'workbox-expiration';

// 构建插件注入的 manifest：[{url, revision}]，hash 资源 revision 为 null
precacheAndRoute(self.__WB_MANIFEST);

// App Shell 模式：导航请求回退到预缓存的 index.html，离线也能打开
registerRoute(
  ({ request }) => request.mode === 'navigate',
  createHandlerBoundToURL('/index.html')
);

// 首屏图片运行时缓存：CacheFirst + 30 天过期，不占预缓存配额
registerRoute(
  ({ request }) => request.destination === 'image',
  new CacheFirst({
    cacheName: 'hero-images',
    plugins: [new ExpirationPlugin({ maxEntries: 60, maxAgeSeconds: 60 * 60 * 24 * 30 })],
  })
);

// 版本更新：新 SW 就绪后通知页面提示刷新，而不是立即 skipWaiting
self.addEventListener('message', e => {
  if (e.data === 'SKIP_WAITING') self.skipWaiting(); // 用户点了刷新按钮才接管
});
```
