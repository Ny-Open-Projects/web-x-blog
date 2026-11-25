---
title: [PER-1023] Service Worker 缓存策略如何按资源类型分治
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1023：Service Worker 缓存策略如何按资源类型分治

**答**：
- 策略矩阵：HTML→Network First（保新鲜）+ 超时回退缓存；静态资源→Cache First + 后台更新（stale-while-revalidate）；API→按业务（实时数据 Network First，列表可 SWR）。
- 版本管理：cache 名带版本号，activate 清理旧缓存，避免存储无限膨胀。
- 坑：SW 更新有延迟（浏览器下次导航才激活新版本），关键修复不能只依赖 SW 缓存刷新。
- 可观测：缓存命中率、SW 更新失败率作为独立指标监控。

```javascript
const CACHE = 'app-v42';
self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.mode === 'navigate') {
    e.respondWith(fetch(req).then(r => {          // Network First
      caches.open(CACHE).then(c => c.put(req, r.clone())); return r;
    }).catch(() => caches.match(req)));
    return;
  }
  if (/\.(js|css|woff2|png|avif)$/.test(new URL(req.url).pathname)) {
    e.respondWith(caches.match(req).then(hit => { // Stale-While-Revalidate
      const fresh = fetch(req).then(r => {
        caches.open(CACHE).then(c => c.put(req, r.clone())); return r;
      });
      return hit ?? fresh;
    }));
  }
});
self.addEventListener('activate', e =>
  e.waitUntil(caches.keys().then(ks =>
    Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k))))));
```
