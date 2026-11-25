---
title: [WCN-712] 组件库资源如何做 CDN 加速与离线可用（Service Worker 缓存）？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-712：组件库资源如何做 CDN 加速与离线可用（Service Worker 缓存）？

**答**：
- 结论：组件 JS/CSS 走 CDN + 强缓存（内容 hash 文件名），HTML 走协商缓存；用 Service Worker 预缓存核心组件资源，实现首屏后离线可用。
- 缓存策略按资源类型区分：带 hash 静态资源用 cache-first；组件元数据/配置用 stale-while-revalidate；版本号变更时主动清理旧缓存。
- 追问钩子：SW 缓存了旧版本组件 JS，发布新版本后用户仍看到旧组件怎么办？考察缓存版本管理与激活清理。

```javascript
// Service Worker 安装期预缓存
const CACHE = 'ds-v2.3.0';
const PRECACHE = ['/ds/core.js', '/ds/button.js', '/ds/theme.css'];
self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(PRECACHE)));
});
self.addEventListener('fetch', (e) => {
  const url = new URL(e.request.url);
  if (url.pathname.includes('/ds/')) {
    e.respondWith(
      caches.match(e.request).then((hit) => hit || fetch(e.request).then((res) => {
        const cp = res.clone(); caches.open(CACHE).then((c) => c.put(e.request, cp)); return res;
      }))
    );
  }
});
self.addEventListener('activate', (e) => {
  e.waitUntil(caches.keys().then((ks) => Promise.all(
    ks.filter((k) => k !== CACHE).map((k) => caches.delete(k))))); // 清旧版本
});
```
