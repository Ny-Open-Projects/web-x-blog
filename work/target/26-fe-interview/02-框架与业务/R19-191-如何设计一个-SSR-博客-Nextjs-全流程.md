---
title: [R19-191] 如何设计一个 SSR 博客（Next.js 全流程）？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-191：如何设计一个 SSR 博客（Next.js 全流程）？
**答**：
- 渲染策略：文章详情 SSG（generateStaticParams + ISR revalidate）兼顾 SEO 与性能；列表页 ISR；后台编辑走 Server Actions + on-demand revalidation（revalidatePath）。
- 数据面：Server Component 直接查数据库/调用层（无接口往返），Metadata API 管 SEO（title/description/OG 图）。
- 交互组件下沉：评论框、点赞、代码高亮复制按钮才是 'use client'，正文渲染留在服务端。
- 工程链路：MDX 渲染管线、sitemap/RSS 自动生成、Vercel/自托管 Docker + CDN 缓存头。

```tsx
// app/blog/[slug]/page.tsx —— Next.js SSR 博客文章页
import { notFound } from 'next/navigation';
import { revalidatePath } from 'next/cache';
import type { Metadata } from 'next';
import { db } from '@/lib/db';

// 1. SSG + ISR：构建期生成所有文章，运行时按 revalidate 过期再生
export async function generateStaticParams() {
  const posts = await db.post.findMany({ select: { slug: true } });
  return posts.map(p => ({ slug: p.slug }));
}
export const revalidate = 3600;                 // 1 小时后台再生

// 2. SEO：Metadata API
export async function generateMetadata(
  { params }: { params: Promise<{ slug: string }> },
): Promise<Metadata> {
  const { slug } = await params;
  const post = await db.post.findUnique({ where: { slug } });
  return {
    title: post?.title,
    description: post?.summary,
    openGraph: { title: post?.title, images: [`/api/og?title=${post?.title}`] },
  };
}

// 3. Server Component：直接查库，零客户端数据请求
export default async function PostPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const post = await db.post.findUnique({
    where: { slug },
    include: { author: true },
  });
  if (!post) notFound();

  return (
    <article>
      <h1>{post.title}</h1>
      <MdContent source={post.content} />   {/* RSC 内渲染 MDX，零 JS 下发 */}
      <LikeButton postId={post.id} />       {/* 交互 islands：唯一的客户端组件 */}
      <CommentSection postId={post.id} />
    </article>
  );
}

// 4. 后台编辑：Server Action + 按需失效
// app/admin/actions.ts
'use server';
export async function updatePost(id: string, content: string) {
  await db.post.update({ where: { id }, data: { content } });
  const post = await db.post.findUnique({ where: { id } });
  revalidatePath(`/blog/${post!.slug}`);     // 立即再生该文章，编辑所见即所得
}

// 5. 站点级：app/sitemap.ts 与 RSS 路由
// export async function sitemap() {
//   const posts = await db.post.findMany();
//   return posts.map(p => ({ url: `https://blog.example.com/blog/${p.slug}`, lastModified: p.updatedAt }));
// }
```
