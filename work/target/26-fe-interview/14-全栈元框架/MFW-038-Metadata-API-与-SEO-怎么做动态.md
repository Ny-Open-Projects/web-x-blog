---
title: [MFW-038] Metadata API 怎么做动态 SEO？generateMetadata 和静态 metadata 怎么选？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-038：Metadata API 怎么做动态 SEO？generateMetadata 和静态 metadata 怎么选？
**答**：
- 静态：路由文件导出 `metadata` 对象；动态：导出 `async generateMetadata({ params })` 按请求数据生成 title/OG/canonical——App Router 不再需要手工管理 `<head>`。
- `generateMetadata` 与 page 共享 Request Memoization：metadata 里 get 过的数据，page 再取不发第二次请求。
- 分层合并：子路由 metadata 覆盖父级同字段；`title.template` 实现全站「文章名 | 站名」格式。
- OG 图可用 `opengraph-image.tsx` / `ImageResponse`（jsx 绘制）按数据生成分享卡片——元框架独有红利。
- 文件约定 meta：`favicon.ico`、`robots.txt`、`sitemap.ts`（动态生成站点地图）都在 app 目录约定化。

```tsx
// app/blog/[slug]/page.tsx
import type { Metadata } from 'next';

export async function generateMetadata({ params }): Promise<Metadata> {
  const { slug } = await params;
  const post = await getPost(slug); // 与 page 共享 memo，不重复请求
  return {
    title: post.title,
    description: post.excerpt,
    alternates: { canonical: `https://blog.example.com/posts/${slug}` },
    openGraph: { images: [`/api/og?title=${encodeURIComponent(post.title)}`] },
  };
}

export default async function Page({ params }) {
  const { slug } = await params;
  const post = await getPost(slug); // memo 命中
  return <article>{post.title}</article>;
}
```

```tsx
// app/sitemap.ts —— 动态站点地图
export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const posts = await db.post.findMany({ select: { slug: true, updatedAt: true } });
  return posts.map((p) => ({
    url: `https://blog.example.com/posts/${p.slug}`,
    lastModified: p.updatedAt,
  }));
}
```
