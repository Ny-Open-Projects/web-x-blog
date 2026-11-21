---
title: [ARC-373] Service Worker 的资源架构如何设计？缓存策略矩阵
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-373：Service Worker 的资源架构如何设计？
**答**：
- SW 是可编程代理：资源架构的核心是按资源类型分配缓存策略，形成策略矩阵，而不是全局一种策略。
- 策略矩阵：HTML 入口 → network-first（保证版本新鲜，失败回退缓存）；带哈希静态资源 → cache-first + 预热（immutable 永不过期）；API GET → stale-while-revalidate（先回缓存后台更新）；API 写操作 → 离线队列重放。
- 版本升级：SW 文件自身每次发布换 URL（或 byte-diff 触发更新）；skipWaiting + 页面刷新策略要平衡"用户在操作中不强制刷新"。
- 失控防护：缓存容量上限（Cache Storage 配额回收策略）、白名单路径、panic 开关（配置中心一键注销 SW）。
- 与发布链路联动：SW 缓存会让"发版即生效"失效——HTML network-first + 版本号接口轮询双保险。
```javascript
self.addEventListener('fetch', (e) => {
  const url = new URL(e.request.url);
  if (url.pathname.startsWith('/assets/'))            // 哈希资源：cache-first
    return e.respondWith(caches.match(e.request).then(r => r || fetchAndCache(e.request)));
  if (url.pathname === '/')                           // 入口：network-first
    return e.respondWith(fetch(e.request).then(putCache).catch(() => caches.match(e.request)));
  if (url.pathname.startsWith('/api/'))               // API：SWR
    return e.respondWith(staleWhileRevalidate(e.request));
});
```
