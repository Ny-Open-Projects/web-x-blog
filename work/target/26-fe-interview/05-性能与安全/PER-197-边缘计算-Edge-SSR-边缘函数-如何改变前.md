---
title: [PER-197] 边缘计算（Edge SSR/边缘函数）如何改变前端的性能与安全？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-197：边缘计算（Edge SSR/边缘函数）如何改变前端的性能与安全？

**答**：
- 性能红利：渲染与个性化逻辑搬到离用户最近的 PoP，TTFB 从中心机房 200ms+ 压到边缘 30ms 级；配合边缘缓存，匿名页可 0 回源。
- 关键设计：**边缘验签**（JWT 在边缘验证，不回源查会话）+ **分层缓存**（匿名页 public 缓存、登录页 no-store）+ 流式渲染。
- 新增约束：边缘函数有 CPU 时限与冷启动（几十 ms），重计算仍应下沉；调试与可观测要用边缘专属的 trace 方案（与 PER-163 的 traceId 打通）。
- 安全注意：边缘代码同样跑在服务端边界，密钥管理走平台 KMS，不要把服务端密钥下放到边缘 bundle。

```javascript
// 边缘函数：边缘渲染骨架 + 边缘验签 + 分层缓存
// deploy: edge worker on CDN node
export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const cache = caches.default;

    // 1. 匿名骨架命中边缘缓存，0 回源
    let res = await cache.match(request);
    if (res) return res;

    // 2. 边缘验签：JWT 就地验证，不回源查会话
    const user = await verifyJwt(request.headers.get('Cookie'), env.SECRET);
    res = new Response(renderShell({ nickname: user?.nickname ?? '游客' }), {
      headers: {
        'Content-Type': 'text/html',
        'Cache-Control': user ? 'private, no-store' : 'public, max-age=60', // 分层缓存
        'X-Edge-PoP': request.cf?.colo ?? 'unknown',
      },
    });
    if (!user) ctx.waitUntil(cache.put(request, res.clone())); // 只有匿名页可缓存
    return res;
  },
};
// 收益：TTFB 从中心机房 200ms 级压到边缘 30ms 级；注意边缘函数有 CPU 时限与冷启动
```
