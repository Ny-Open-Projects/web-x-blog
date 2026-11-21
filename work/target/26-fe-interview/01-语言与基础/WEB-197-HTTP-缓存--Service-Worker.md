---
title: [WEB-197] HTTP 缓存 + Service Worker + 本地存储的三层缓存体系怎么设计？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-197：HTTP 缓存 + Service Worker + 本地存储的三层缓存体系怎么设计？
**答**：
- 分层职责：HTTP 缓存是默认层（指纹文件长缓存 + HTML 协商缓存）；SW Cache API 管离线与策略（cache-first/SWR）；IndexedDB 管结构化业务数据（接口数据、同步队列）。
- 版本原则：带 hash 的静态资源 Cache-Control 一年 immutable；HTML 不强缓存，靠 SW 网络优先保证版本新鲜。
- 失效一致性：SW 命中旧版本时给"有新版本可用"提示，防止用户长期停留在旧 shell。
- 度量：分别上报三层命中率，验证体系真实收益。

```javascript
// SW 中组合三层：静态走 Cache API，接口数据落 IDB 兜底，HTML 网络优先
self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);
  if (url.pathname.startsWith('/static/')) {
    event.respondWith(cacheFirst(event.request));                 // 指纹资源：缓存优先
  } else if (url.pathname === '/' || url.pathname.startsWith('/app')) {
    event.respondWith(networkFirst(event.request));               // HTML：网络优先
  } else if (url.pathname.startsWith('/api/')) {
    event.respondWith(networkFirstWithIdbBackup(event.request));  // 接口：网络优先 + IDB 兜底
  }
});
async function networkFirstWithIdbBackup(request) {
  try {
    const res = await fetch(request);
    (await caches.open('api-v1')).put(request, res.clone());      // 供快速回读
    return res;
  } catch {
    const cached = await caches.match(request);
    if (cached) return cached;
    const idb = await db.get('apiBackup', request.url);           // 最后兜底：结构化数据
    return idb ? new Response(JSON.stringify(idb), { headers: { 'content-type': 'application/json' } })
               : new Response('offline', { status: 503 });
  }
}
```
