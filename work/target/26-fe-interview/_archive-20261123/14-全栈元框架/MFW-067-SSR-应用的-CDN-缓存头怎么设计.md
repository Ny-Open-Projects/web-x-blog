---
title: [MFW-067] SSR 应用的 CDN 缓存头怎么设计？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-067：SSR 应用的 CDN 缓存头怎么设计？
**答**：
- 核心是区分三类资源：**指纹静态资源** `immutable, max-age=31536000`；**HTML/SSR 页面** `s-maxage` 给 CDN 共享缓存 + `stale-while-revalidate` 给过期宽限；**个性化动态内容** `private, no-store` 或从 HTML 中剥离单独请求。
- `s-maxage` 与 `max-age` 的区别：前者管 CDN/代理，后者管浏览器；SSR 页面常设 `s-maxage=60, stale-while-revalidate=300`，让同一页面的洪峰被 CDN 挡住。
- 个性化与缓存共存的关键是**缓存 key 设计**：把 Vary 头控制到最小，个性化部分用客户端请求补齐，或用 Edge 中间件改写 URL（如按 geo/AB 值入 key）。
- `Surrogate-Control`/`CDN-Cache-Control` 等专有头用于 CDN 与浏览器策略解耦；Next 的 `Cache-Control` 由路由段配置自动生成，覆写要谨慎。

```ts
// app/products/[id]/page.tsx
// 电商商品详情：页面级 CDN 缓存 + 个人化数据客户端补齐
export async function generateMetadata(): Promise<Metadata> { /* … */ }

export default async function Page({ params }: { params: Promise<{ id: string }> }) {
  const { id } = use(params);
  return (
    <>
      {/* 公共部分：服务端渲染，CDN 可缓存（由路由 revalidate 生成 s-maxage） */}
      <ProductInfo id={id} />
      {/* 个人化部分：绝不进 CDN 缓存，浏览器端补齐 */}
      <UserCartBadge />   {/* 内部 fetch('/api/cart-count', { cache: 'no-store' }) */}
    </>
  );
}
```

```js
// next.config.js 或 Route Handler 中手动设置
export function GET() {
  return new Response(html, {
    headers: {
      // CDN 缓存 60s，过期后 300s 内可继续回旧内容同时后台刷新
      'Cache-Control': 'public, s-maxage=60, stale-while-revalidate=300',
      'Vary': 'Accept-Encoding', // 尽量小，不要 Vary: Cookie（会击穿缓存）
    },
  });
}
```
