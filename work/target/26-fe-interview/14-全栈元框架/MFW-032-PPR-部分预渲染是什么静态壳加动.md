---
title: [MFW-032] Partial Prerendering（PPR）是什么？怎么做到一页同时静态与动态？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-032：Partial Prerendering（PPR）是什么？怎么做到一页同时静态与动态？
**答**：
- PPR（Next 15 实验特性，`experimental.ppr`）：构建时把页面拆成**静态外壳**（预渲染好的 HTML，从 CDN 秒出）+ **动态洞**（Suspense 包住的动态部分，请求时流式填充）——一个页面兼得静态速度与动态个性化。
- 边界判定：动态 API（cookies/headers）与未缓存数据必须包在 `<Suspense>` 内，否则构建报错——Suspense 就是静态/动态的分界线。
- 对比方案：全静态 + client fetch（首屏空白抖动）、全动态 SSR（TTFB 慢）、ISR（数据有延迟）——PPR 是「静态壳 + 动态流」的合体。
- 实现：外壳命中时 TTFB 接近 CDN；动态洞通过 RSC Payload 流式补齐（含 fallback 即时显示）。
- 适用：电商详情（静态商品数据 + 动态库存/推荐）、首页（静态框架 + 动态个性化 banner）。

```tsx
// next.config.js
module.exports = { experimental: { ppr: 'incremental' } };

// app/product/[id]/page.tsx
import { Suspense } from 'react';
import { cookies } from 'next/headers';

export const experimental_ppr = true; // 页面级开启

export default async function Page({ params }) {
  const { id } = await params;
  return (
    <>
      {/* 静态部分：构建期预渲染进外壳 */}
      <ProductInfo id={id} />
      {/* 动态洞：cookies 读取被 Suspense 包住，请求时流式填充 */}
      <Suspense fallback={<CartSkeleton />}>
        <UserCart />
      </Suspense>
    </>
  );
}

async function UserCart() {
  const sessionId = (await cookies()).get('session')?.value; // 动态：不阻塞静态壳
  const cart = await getCart(sessionId);
  return <Cart items={cart} />;
}
```
