---
title: [OPT-023] stale-while-revalidate 如何提升接口加载体感？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-023：stale-while-revalidate 如何提升接口加载体感？

**答**：
- 语义：`Cache-Control: stale-while-revalidate=N`——缓存过期后的 N 秒内，**先立即返回旧内容，同时后台异步刷新**，下次请求就是新的。
- 对用户：请求"永远秒回"（拿旧缓存）；对数据：后台静默更新，最终一致。
- 浏览器与 CDN（如 Cloudflare）都支持；也可在应用层手写同样的策略以获得更细的控制。
- 适合：允许短暂陈旧的读多写少数据（首页 feed、商品列表）；不适合余额、库存等强实时数据。

```javascript
// 一一对应：应用层手写 stale-while-revalidate 策略
const cache = new Map(); // key -> { value, ts }

async function swrFetch(url, maxAge = 30_000, swr = 60_000) {
  const hit = cache.get(url);
  const now = Date.now();

  // 命中新鲜缓存：直接返回，不发请求
  if (hit && now - hit.ts < maxAge) return hit.value;

  // 命中过期但在 SWR 窗口内：先返回旧值，后台刷新
  if (hit && now - hit.ts < maxAge + swr) {
    fetch(url).then((r) => r.json()).then((v) => cache.set(url, { value: v, ts: Date.now() }));
    return hit.value;
  }

  // 完全没缓存：同步等待请求
  const res = await fetch(url).then((r) => r.json());
  cache.set(url, { value: res, ts: Date.now() });
  return res;
}
```
