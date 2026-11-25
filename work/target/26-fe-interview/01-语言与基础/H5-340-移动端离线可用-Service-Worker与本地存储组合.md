---
title: [H5-340] 移动端离线可用：Service Worker 与本地存储组合方案
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 面试题, PWA]
type: 面试题
---

## H5-340：移动端离线可用：Service Worker 与本地存储组合方案

**答**：
- 离线分层：壳离线（SW 预缓存 HTML/CSS/JS，导航请求 cache-first）+ 数据离线（IndexedDB 缓存列表/详情数据，stale-while-revalidate）+ 操作离线（队列暂存，网络恢复重放）
- IndexedDB 是唯一正解：localStorage 只有 5MB 且同步阻塞，IndexedDB 容量大、事务型、可存 Blob——图片缓存也能放
- 离线操作队列：写操作失败时按业务语义入队（带幂等键），SW background sync 或下次启动重放；重放要处理「数据已过期」冲突（版本号/时间戳校验）
- 缓存策略组合拳：静态资源 install 时预缓存（工作箱 precache）；API 按性质分：配置类 cache-first、列表 SWR、用户数据 network-first + IDB 兜底
- 更新与存储配额：navigator.storage.estimate() 监控配额，persist() 申请持久化存储防被清理；SW 更新用 skipWaiting + clients.claim 时序控制

```javascript
// SW: 数据离线 SWR + IDB 兜底
self.addEventListener('fetch', (e) => {
  if (!e.request.url.includes('/api/feed')) return;
  e.respondWith((async () => {
    const cache = await caches.open('feed-v1');
    const cached = await cache.match(e.request);
    const net = fetch(e.request).then((res) => { cache.put(e.request, res.clone()); return res; })
      .catch(() => cached || offlineFallback(e.request));
    return cached || net;                      // stale-while-revalidate
  })());
});
```

```javascript
// 页面: 离线写操作队列
async function submitLike(id) {
  try { await api.post('/like', { id }); }
  catch {
    const q = await idb.get('ops') || [];
    q.push({ url: '/like', body: { id }, key: `like:${id}` }); // 幂等键
    await idb.set('ops', q);
  }
}
```
