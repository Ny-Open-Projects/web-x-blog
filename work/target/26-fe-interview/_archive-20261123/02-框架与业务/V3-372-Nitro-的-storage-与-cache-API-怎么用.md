---
title: [V3-372] Nitro 的 storage 与 cache API 怎么用？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-372：Nitro 的 storage 与 cache API 怎么用？
**答**：
- `useStorage()`：统一键值存储抽象，driver 可插（memory/fs/redis/Cloudflare KV…），server/api 里 `useStorage('cache').setItem(key, val)`。
- `defineCachedFunction(name, fn, { maxAge, swr })`：函数级缓存，swr 模式先返回旧值再后台刷新，适合排行榜类数据。
- `defineCachedEventHandler` / routeRules 的 `cache`：路由级缓存，配合 CDN 边缘缓存形成多级。
- 命名空间：`useStorage('redis')` 切换 driver；序列化默认 JSON，大对象注意体积与 TTL。
- 实践：商品详情接口用 swr 30s，大促热点数据命中率是吞吐关键。
```javascript
export default defineCachedEventHandler(async (e) => getGoods(e.ctx.params.id),
  { maxAge: 60 * 5, swr: true, name: 'goods' })
```
