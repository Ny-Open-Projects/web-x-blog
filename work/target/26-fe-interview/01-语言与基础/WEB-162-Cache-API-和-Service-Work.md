---
title: [WEB-162] Cache API 和 Service Worker 是什么关系？页面里能直接用吗？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-162：Cache API 和 Service Worker 是什么关系？页面里能直接用吗？
**答**：
- Cache API（caches 对象）是独立的存储能力，Service Worker 只是它最常见的"使用方"——SW 不在时页面也能直接读写缓存。
- 二者解耦：预缓存可以由页面发起，请求拦截才是 SW 的职责；注销 SW 不必然清空 Cache Storage。
- 每个 Cache 是 Request/Response 的键值集合，存的是"完整 HTTP 语义"（含头与状态码），与 HTTP 缓存是两套体系。
- 版本化靠缓存命名空间（cache-v1/v2），activate 时清理旧版本；match 支持 ignoreSearch 等匹配参数。

```javascript
// 页面直接使用 Cache API（无需 Service Worker）
const cache = await caches.open('app-shell-v1');
// 写入：可存网络响应，也可手工构造 Response
await cache.put('/api/config', new Response(JSON.stringify({ theme: 'dark' }), {
  headers: { 'content-type': 'application/json' },
}));
// 读取：match 返回 Response 或 undefined
const cached = await cache.match('/api/config', { ignoreSearch: true });
if (cached) console.log('hit:', await cached.json());
// 版本升级时清理旧命名空间
const names = await caches.keys();
await Promise.all(names.filter((n) => n !== 'app-shell-v1').map((n) => caches.delete(n)));
```
