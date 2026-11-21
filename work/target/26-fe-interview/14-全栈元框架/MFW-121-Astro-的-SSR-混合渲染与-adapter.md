---
title: [MFW-121] Astro 的 SSR 混合渲染怎么配置？adapter 体系什么样？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-121：Astro 的 SSR 混合渲染怎么配置？adapter 体系什么样？
**答**：
- Astro 5 的模型：默认全站静态（`output: 'static'`），需要 SSR 的页面**逐页 opt-in**（`export const prerender = false`），或全站 SSR 再逐页 opt-out——「默认静态、按需服务端」是 Astro 混合渲染的姿态。
- adapter：`@astrojs/node`（自托管）、`@astrojs/vercel`、`@astrojs/cloudflare` 等；SSR 页面运行在 adapter 提供的运行时，静态部分照常预渲染。
- 缓存策略：SSR 页可用 `Astro.response.headers` 设 Cache-Control；配合 Server Islands 做到「主体缓存 + 个性化实时」。
- 与 Next 对照：Next 默认静态化靠缓存决定，Astro 默认静态靠 prerender 标志决定——Astro 的切换开关更直白。

```ts
// astro.config.mjs
import { defineConfig } from 'astro/config';
import node from '@astrojs/node';

export default defineConfig({
  output: 'static',           // 默认静态
  adapter: node({ mode: 'standalone' }), // SSR 页跑在 Node standalone
});
```

```astro
---
// src/pages/dashboard.astro —— opt-in SSR
export const prerender = false; // 这页走服务端渲染

import { cookies } from 'astro:user'; // 仅 SSR 页可用
const user = await getUser(cookies());
Astro.response.headers.set('Cache-Control', 'private, no-store'); // 个性化页禁缓存
---
<p>你好，{user?.name}</p>
```

```astro
---
// src/pages/products/[id].astro —— 静态页 + 按需路径
export async function getStaticPaths() {
  const products = await db.product.findMany({ select: { id: true } });
  return products.map((p) => ({ params: { id: p.id } }));
}
export const prerender = true; // 显式静态（默认即是）
---
<h1>商品</h1>
```
