---
title: [WEB-354] Service Worker 的缓存策略有哪些？什么场景选哪个？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 缓存]
type: 笔试题
---

## WEB-354：Service Worker 的缓存策略有哪些？什么场景选哪个？
**答**：
- Cache First：静态不变资源（字体、图片），命中即用，最快；配合版本化缓存名清理。
- Network First：接口类，先网络失败落缓存（新闻列表）；Stale-While-Revalidate：接口高频访问，旧值秒回+后台更新。
- 选型原则：按"新鲜度容忍度"选；写操作与鉴权请求永远 Network Only。

```javascript
const strategies = {
  '/assets/': 'cacheFirst', '/api/news': 'networkFirst',
  '/api/feed': 'staleWhileRevalidate', '/api/order': 'networkOnly',
};
async function handle(req) {
  const s = matchRoute(req.url);
  if (s === 'cacheFirst') {
    const hit = await caches.match(req);
    return hit || put(fetch(req));
  }
  if (s === 'staleWhileRevalidate') {
    const cached = await caches.match(req);
    fetch(req).then(r => put(r));        // 后台更新
    return cached || fetch(req);
  }
  return fetch(req);                     // networkFirst/Only 同理
}
console.log('新鲜度容忍度决定策略');
```

**评分点**：
- 结论先行，机制一句话讲透
- 覆盖攻击面/异常分支与边界条件
- 代码可运行、命名清晰、有防御性处理
- 主动给出工程取舍与常见坑
