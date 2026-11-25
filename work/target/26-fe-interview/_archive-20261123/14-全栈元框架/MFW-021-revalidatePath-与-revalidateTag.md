---
title: [MFW-021] revalidatePath 和 revalidateTag 的区别是什么？各自失效什么？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-021：revalidatePath 和 revalidateTag 的区别是什么？各自失效什么？
**答**：
- `revalidatePath('/products')`：**按 URL 失效**——清掉该路径的 Full Route Cache + Client Router Cache，同时该路由上所有 Data Cache 条目一并失效（一次调用失效整条链）。
- `revalidateTag('products')`：**按标签失效**——只清打了该 tag 的 Data Cache 条目及其引用的 Full Route，影响面更小、更精准。
- 选型：内容管理系统后台「文章发布后刷新文章页」用 path；「商品价格变更，所有引用价格的页面都要更新」用 tag。
- 两者都只能在 Server Action 或 Route Handler 中调用；都是「标记失效」而非立即重渲染——下一次请求才再生。
- 组合惯例：写操作里先写库 → `revalidateTag(实体tag)` → 需要强刷列表时补 `revalidatePath`。

```ts
// app/actions.ts
'use server';
import { revalidatePath, revalidateTag } from 'next/cache';

export async function publishPost(postId: string) {
  await db.post.update({ where: { id: postId }, data: { status: 'published' } });
  revalidatePath(`/posts/${postId}`); // 精确刷新这一篇文章的路由
  revalidateTag('posts-list');        // 首页/列表页引用了 posts-list 数据缓存
}
```

```ts
// app/api/webhook/cms/route.ts —— CMS 回调也可以触发失效
export async function POST(req: Request) {
  const { slug } = await req.json();
  // path 失效支持层次：'/' 刷新全部；'/blog/[slug]' 命中动态段所有实例
  revalidatePath(`/blog/${slug}`, 'page');
  revalidateTag(`post-${slug}`);
  return Response.json({ ok: true });
}
```
