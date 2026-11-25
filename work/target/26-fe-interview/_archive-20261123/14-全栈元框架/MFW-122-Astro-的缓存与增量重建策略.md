---
title: [MFW-122] Astro 大型内容站的缓存与内容更新策略怎么做？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-122：Astro 大型内容站的缓存与内容更新策略怎么做？
**答**：
- 构建期缓存：Astro 缓存 loader 拉取的内容（`loader` 层的 cache），重复构建不重复拉 CMS；CI 上用构建缓存（Vite cache dir）加速。
- 发布更新链路：内容变更 → git push / CMS webhook → CI 增量重建（Astro 5 的 Content Layer 只重建受影响内容）→ 全量静态产物 → CDN 切换。全静态模型下「更新 = 重建」，时效以分钟计。
- 需要秒级时效的部分：用 Server Islands（个性化）或对个别页 opt-in SSR + Cache-Control（如 `s-maxage=60`）。
- 资源缓存纪律：HTML 短缓存/etag、指纹资源 immutable、图片走图片 CDN（astro:assets + 第三方 loader）。

```ts
// astro.config.mjs —— 内容站缓存全景
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://blog.example.com',
  integrations: [sitemap()],
  experimental: {
    // Content Layer 构建缓存（Astro 5）
  },
  vite: {
    build: { cacheDir: 'node_modules/.astro-cache' },
  },
});
```

```ts
// src/pages/api/revalidate.ts —— CMS webhook 触发重建（netlify/vercel deploy hook 代理）
export const POST: APIRoute = async ({ request }) => {
  const secret = new URL(request.url).searchParams.get('secret');
  if (secret !== process.env.REVALIDATE_SECRET) {
    return new Response('forbidden', { status: 403 });
  }
  // 触发平台部署钩子；静态站更新即重建
  await fetch(process.env.DEPLOY_HOOK!, { method: 'POST' });
  return new Response('ok');
};
```

```astro
---
// 需要分钟级时效的 SSR 页
export const prerender = false;
Astro.response.headers.set('Cache-Control', 'public, s-maxage=60, stale-while-revalidate=300');
---
<h1>今日快讯</h1>
```
