---
title: [NODE-277] 边缘渲染与 CDN 缓存的配合？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-277：边缘渲染与 CDN 缓存的配合？
**答**:
- 边缘渲染：SSR 下沉到边缘节点（Cloudflare Workers/Vercel Edge）——就近渲染，TTFB 全球稳定；限制：无持久连接/无 fs/轻运行时。
- CDN 缓存 SSR 结果：HTML 带 s-maxage + stale-while-revalidate → 边缘缓存渲染产物，源站只做回源刷新。
- 个性化分离：公共 HTML 缓存 + 个性化数据客户端补拉（或 edge include ESI）——缓存命中与个性化兼得。
- 回源保护：SWR + 单飞（NODE-345 同款，CDN 层 request coalescing）。

```text
# CDN 层策略（Cache-Control）
Cache-Control: s-maxage=60, stale-while-revalidate=300
# 60s 内：边缘直接返回；60~360s：返回旧值同时后台回源刷新
# 个性化：HTML 公共部分缓存，<script>window.__USER__=null</script> + 客户端 /me 补拉
# ESI（边缘包含）：<esi:include src="/_fragments/user-bar" /> —— 边缘拼装个性化片段
```
```javascript
// Edge Worker 渲染（概念）
export default {
  async fetch(req, env) {
    const cache = caches.default;
    const hit = await cache.match(req);
    if (hit) return hit;                            // 边缘命中
    const html = await renderOnEdge(req, env);      // 轻量 SSR（无重依赖）
    const res = new Response(html, { headers: { 'Cache-Control': 's-maxage=60' } });
    ctx.waitUntil(cache.put(req, res.clone()));
    return res;
  },
};
```
