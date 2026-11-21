---
title: [WEB-343] 内存缓存、磁盘缓存、Service Worker 三层是什么关系？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 缓存]
type: 面试题
---

## WEB-343：内存缓存、磁盘缓存、Service Worker 三层是什么关系？
**答**：
- Memory Cache：进程内，快但随 tab 关闭清空，图片/小文件常驻；Disk Cache：持久、容量大，重启可复用。
- Service Worker 最高优先：SW fetch 拦截发生在 HTTP 缓存之前，SW 可以决定走 Cache API 还是透传给 HTTP 缓存。
- 观察技巧：DevTools Network 的 Size 列显示 (memory cache)/(disk cache)/(ServiceWorker)；from disk cache 的文件刷新后仍在。

```javascript
self.addEventListener('fetch', e => {
  // SW 优先级最高：先查 Cache API，再决定回源
  e.respondWith(caches.match(e.request).then(hit =>
    hit || fetch(e.request)));
});
console.log('SW → Cache API → HTTP(memory/disk) 三层依次');
```
