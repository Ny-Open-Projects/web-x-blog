---
title: [MFW-712] Edge SSG 的缓存一致性
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-712：Edge SSG 缓存一致性

**答**:
- Edge SSG（edge 渲染的 SSG 页面——Vercel Edge Cache/Cloudflare Cache API）的缓存一致性：1) **多边缘节点的一致性**（SSG 产物缓存在 N 个 PoP——revalidate 需要广播到所有节点（中心化失效 → 边缘传播延迟——「旧内容窗口」= 各 PoP 更新不同步）；2) purge by tag（CDN Surrogate-Key RBL-662——广播失效）；3) **边缘的 stale-while-revalidate**（过期即返回旧值 + 后台刷新——PoP 独立刷新（不同 PoP 的刷新时间差——短暂不一致窗口可接受）。
- 与中心化 SSG 的差异：中心（CDN 拉源站——源站是唯一真源：CDN 全部同源失效）；Edge SSG（edge 渲染 = 边缘自身是渲染点——多 PoP 各自渲染/各自缓存——失效需广播）。
- 一致性的容忍度：页面内容变更的传播延迟（秒级可接受 vs 分钟级——业务的容忍度决定缓存策略 RBL-509）；「stale 的可接受度」= 内容变更频率 × 用户敏感度。
- 追问钩子：为什么「Edge SSG 的一致性窗口」比「中心 SSG」更大？——中心：源站更新 → CDN 全部拉新（被动——TTL 到期才拉或主动 purge——一次 purge 全一致）；Edge：每个 PoP 各自渲染/缓存——revalidate 需要广播到 N 个 PoP（传播延迟）+ 各 PoP 独立刷新（时间差）；「多副本一致性」的经典难题：Edge SSG 的 PoP = 分布式缓存副本——CAP 的选择：可用性优先（各 PoP 独立 stale-while-revalidate）牺牲强一致——短暂不一致窗口 = 架构的接受成本。

```typescript
// Edge SSG 的缓存失效广播
// 1) 中心事件 → 广播到所有 PoP
async function broadcastInvalidate(tag: string) {
  await fetch(`https://api.cloudflare.com/client/v4/zones/${ZONE_ID}/purge_cache`, {
    method: 'POST',
    headers: { Authorization: `Bearer ${CF_TOKEN}` },
    body: JSON.stringify({ tags: [tag] }),               // tag 广播：全 PoP 失效
  });
}
// 2) Edge 端的 stale-while-revalidate
export default {
  async fetch(req, env, ctx) {
    const cache = caches.default;
    const cached = await cache.match(req);
    if (cached) {
      const age = Date.now() - parseInt(cached.headers.get('x-rendered-at') ?? '0');
      if (age < 60000) return cached;                    // 60s 内新鲜
      // 过期：返回旧值 + 后台刷新
      ctx.waitUntil(revalidate(req, env, cache));        // waitUntil：不阻塞响应
      return cached;                                     // stale-while-revalidate
    }
    return revalidate(req, env, cache);
  },
};
// 各 PoP 独立刷新：时间差 = 短暂不一致窗口
```
