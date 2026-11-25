---
title: [MFW-031] Next.js 15 的异步 request API（await cookies/headers）改了什么？为什么？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-031：Next.js 15 的异步 request API（await cookies/headers）改了什么？为什么？
**答**：
- Next 15 起 `cookies()`、`headers()`、`draftMode()`、`params`、`searchParams` 全部变为**异步**（返回 Promise），同步用法直接报错。
- 动机：为「动态 IO」与流式渲染铺路——渲染可以在动态值未就绪时先进行，等真正用到时再 resolve，配合 Partial Prerendering（PPR）实现「静态壳 + 动态洞」。
- 迁移要点：`const cookieStore = await cookies()`；page/layout 的 props 里 `params` 与 `searchParams` 也都 Promise 化：`const { slug } = await params`。
- 类型上 page 的 props 要用 `Promise<params>`（Next 15 generated types）；客户端组件收到的 searchParams 也同理。
- 好处：await 边界即挂起点，天然接入 Suspense 流式——把「读 cookies」这一步变成可让路的 IO，而不是同步阻塞整个渲染。

```tsx
// app/profile/[id]/page.tsx —— Next 15 写法
import { cookies, headers } from 'next/headers';

type Props = { params: Promise<{ id: string }>; searchParams: Promise<{ tab?: string }> };

export default async function Profile({ params, searchParams }: Props) {
  const { id } = await params;            // params 现在是 Promise
  const { tab = 'posts' } = await searchParams;
  const session = (await cookies()).get('session'); // cookies() 也要 await
  const ua = (await headers()).get('user-agent');

  return <ProfileView id={id} tab={tab} />;
}
```

```tsx
// 渐进迁移：codemod npx @next/codemod upgrade latest
// 旧写法（Next 14）：
// export default function Page({ params }: { params: { id: string } }) {
//   const { id } = params;                 // 同步读取
//   const theme = cookies().get('theme');  // 同步 API
// }
```
