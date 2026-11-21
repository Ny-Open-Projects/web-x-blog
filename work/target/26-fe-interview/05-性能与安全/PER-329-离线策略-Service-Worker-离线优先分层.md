---
title: [PER-329] 离线优先（Offline-first）的分层策略：壳/数据/媒体各用什么缓存策略？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-329：离线优先（Offline-first）的分层策略：壳/数据/媒体各用什么缓存策略？

**答**：
- 三层资源三种策略：① 应用壳（HTML/核心 JS/CSS）——预缓存（install 时全部拉好）+ 更新时新版本预取，离线可用是硬承诺；② 业务数据（接口 JSON）——stale-while-revalidate 或"网络优先 + 缓存兜底"，配离线队列把写请求攒起来恢复后重放；③ 媒体（图片/视频）——cache-first + LRU 容量上限（占配额大头，必须限额）。
- 离线写队列（Background Sync 或自实现）：写请求失败入队（带幂等键），SW 的 sync 事件触发重放；顺序与依赖要保持（同实体操作按序）。
- 离线状态可感知：UI 明确展示"离线，展示缓存数据于 10 分钟前"（数据新鲜度标注），避免用户把旧数据当真。
- 版本与清理：预缓存清单版本化，activate 时清旧缓存；媒体缓存按容量 LRU（PER-322 模式）。

```javascript
// SW 内三分层路由
self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);
  if (event.request.method !== 'GET') return event.respondWith(enqueueForSync(event.request)); // 写请求离线队列
  if (url.pathname.startsWith('/api/')) return event.respondWith(networkFirstWithFallback(event.request));
  if (/\.(mp4|avif|jpe?g|png)$/.test(url.pathname)) return event.respondWith(cacheFirstLRU(event.request));
  return event.respondWith(precacheFirst(event.request));   // 应用壳
});
async function networkFirstWithFallback(req) {
  try {
    const res = await fetch(req);
    const cache = await caches.open('data-v1');
    cache.put(req, res.clone());
    return res;
  } catch {
    const hit = await caches.match(req);
    if (hit) return new Response(await hit.clone().text(), { headers: { 'X-From-Cache': '1', ...hit.headers?.get('content-type') && { 'Content-Type': hit.headers.get('content-type') } } });
    return new Response(JSON.stringify({ offline: true }), { headers: { 'Content-Type': 'application/json' } });
  }
}
// 页面读响应头 X-From-Cache 标注"离线数据（可能过期）"
```
