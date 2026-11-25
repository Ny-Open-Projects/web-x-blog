---
title: [MFW-018] Full Route Cache 的生成条件是什么？哪些情况会导致动态渲染？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-018：Full Route Cache 的生成条件是什么？哪些情况会导致动态渲染？
**答**：
- 静态渲染条件：路由**无动态函数**（cookies/headers/searchParams 未读）且**无未缓存数据**（fetch 都带缓存语义或 revalidate 配置），构建期即产出 HTML 存入 Full Route Cache。
- 触发动态渲染的因素：读 `cookies()/headers()/draftMode()`、用 `connection()`、读取 `searchParams`（page props）、有未配置缓存的 fetch（v14 默认）、`dynamic = 'force-dynamic'`。
- 中间产物：`revalidate` 设定后，静态页会在过期后由**下一次请求触发后台再生成**（ISR），请求期间仍回旧 HTML。
- `dynamic = 'error'`：发现动态因素直接构建报错，用于强约束静态化；`force-static` 则反方向压制成静态。
- 排查手段：构建日志里的 ○（静态）/ƒ（动态）标记；或 `unstable_noStore` 显式声明不缓存。

```jsx
// app/dashboard/page.tsx
import { cookies } from 'next/headers';

export const dynamic = 'force-dynamic'; // 显式声明：每请求渲染
// 或 export const revalidate = 0; 等价效果

export default async function Page() {
  const theme = (await cookies()).get('theme')?.value; // 读动态函数 → 动态渲染
  return <div className={theme}>实时仪表盘</div>;
}
```

```jsx
// app/blog/[slug]/page.tsx —— 静态 + ISR
export const revalidate = 60; // 60s 后台再生成

export async function generateStaticParams() {
  const posts = await db.post.findMany({ select: { slug: true } });
  return posts.map((p) => ({ slug: p.slug })); // 构建期预渲染全部文章
}

export default async function Post({ params }) {
  return <article>{(await getPost(params.slug)).title}</article>;
}
```
