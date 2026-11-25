---
title: [WEB-349] 缓存雪崩、穿透、击穿，放到前端/CDN 侧怎么理解和应对？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 缓存]
type: 面试题
---

## WEB-349：缓存雪崩、穿透、击穿，放到前端/CDN 侧怎么理解和应对？
**答**：
- 雪崩：大量缓存同一时刻过期（如整点发布）→ 回源风暴；前端对应：错开 max-age（加随机抖动）、发布预热。
- 穿透：请求不存在的资源绕过缓存直打源站；对应：负缓存（404 也短缓存）、CDN 缓存空响应、WAF 拦扫描。
- 击穿：热点 key 过期瞬间并发回源；对应：资源预热 + stale-while-revalidate 让旧值先顶住。

```javascript
// max-age 加抖动防雪崩
const maxAge = 3600 + Math.floor(Math.random() * 600); // ±10min
// 负缓存: 404 缓存 5min
const handler = (res) => res.status === 404
  ? { ...res, headers: { 'Cache-Control': 'max-age=300' } } : res;
console.log('抖动 + 负缓存 + swr = 三板斧');
```
