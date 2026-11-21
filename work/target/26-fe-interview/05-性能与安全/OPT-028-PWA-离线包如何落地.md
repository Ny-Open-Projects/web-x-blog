---
title: [OPT-028] PWA 离线包如何落地？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-028：PWA 离线包如何落地？

**答**：
- 三件套：`manifest.json`（可安装元信息）+ Service Worker（离线控制）+ HTTPS。
- 核心是 App Shell 模式：把外壳（HTML 骨架、公共 CSS/JS、字体）在 install 阶段**预缓存**，内容数据走运行时缓存。
- 构建期用 workbox 自动生成 precache manifest（带 revision hash），文件一变 URL 即变，避免手写缓存清单。
- 离线兜底：导航请求失败时返回缓存的 `/offline.html`，体验不白屏。

```javascript
// 一一对应：SW 注册 + workbox 预缓存 App Shell
// main.js —— 页面侧注册
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js').then((reg) => {
      reg.addEventListener('updatefound', () => console.log('发现新版本 SW'));
    });
  });
}

// sw.js —— workbox 构建产物（示意），预缓存外壳 + 离线兜底
import { registerRoute } from 'workbox-routing';
import { NetworkFirst } from 'workbox-strategies';
import { precacheAndRoute, createHandlerBoundToURL } from 'workbox-precaching';

precacheAndRoute(self.__WB_MANIFEST); // 构建期生成的带 hash 清单

// App Shell：外壳文件离线可用，导航请求失败时用缓存的 index.html 兜底
registerRoute(
  ({ request }) => request.mode === 'navigate',
  createHandlerBoundToURL('/index.html')
);

// 数据接口：网络优先，离线回落上次数据
registerRoute(
  ({ url }) => url.pathname.startsWith('/api/'),
  new NetworkFirst({ cacheName: 'api-cache', networkTimeoutSeconds: 3 })
);
```
