---
title: [MFW-161] CDN 与 SSR 协同时，stale-while-revalidate 策略怎么设计？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-161：CDN 与 SSR 协同时，stale-while-revalidate 策略怎么设计？
**答**：
- SWR 三段语义：`s-maxage` 内 CDN 直接回缓存（快）；过期后 `stale-while-revalidate` 窗口内**先回旧内容同时后台回源刷新**（用户无感更新）；窗口外才同步回源（等 SSR）。
- 参数设计经验：新闻/商品列表页 `s-maxage=60, swr=300`（一分钟硬缓存+五分钟宽限）；详情页可更长；个人化页面禁用（no-store）。SWR 窗口 > s-maxage，否则退化成同步刷新。
- 与框架 ISR 的关系：Next ISR 在服务端实现类似语义（stale 时回旧缓存并后台再生），CDN 的 SWR 是传输层版本——两者叠加时注意别让 CDN 缓存住「已经是 stale 的再验证响应」造成双重过期。
- 观测指标：CDN 命中率、回源率、stale 服务占比；命中率低于预期多半是 Vary 头或 query 全量进缓存 key。

```ts
// 统一缓存策略生成器：按内容类型给头
type Profile = { smax: number; swr: number; private?: boolean };

const PROFILES: Record<string, Profile> = {
  home:    { smax: 30,  swr: 120 },
  list:    { smax: 60,  swr: 300 },
  detail:  { smax: 600, swr: 1800 },
  user:    { smax: 0,   swr: 0, private: true },
};

export function cacheControl(type: keyof typeof PROFILES): string {
  const p = PROFILES[type];
  if (p.private) return 'private, no-store';
  return `public, s-maxage=${p.smax}, stale-while-revalidate=${p.swr}`;
}
```

```js
// Route Handler 应用
// app/api/products/route.ts
export async function GET() {
  const data = await getProducts();
  return new Response(JSON.stringify(data), {
    headers: {
      'Content-Type': 'application/json',
      'Cache-Control': cacheControl('list'),
      // Vary 最小化：按编码区分，绝不要 Vary: Cookie
      Vary: 'Accept-Encoding',
    },
  });
}
```
