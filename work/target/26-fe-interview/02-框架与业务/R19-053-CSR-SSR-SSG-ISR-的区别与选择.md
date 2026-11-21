---
title: [R19-053] CSR、SSR、SSG、ISR 的区别与选择？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-053：CSR、SSR、SSG、ISR 的区别与选择？
**答**：
- CSR 在浏览器渲染，首屏慢、SEO 弱，但交互后体验好、服务器压力小。
- SSR 每次请求在服务端渲染 HTML，首屏快、SEO 好，服务器成本高。
- SSG 构建时生成静态 HTML，CDN 分发最快，适合内容不常变的页面。
- ISR 是 SSG 的增量更新：设置 revalidate，过期后请求触发重新生成，兼顾新鲜度与速度。

```javascript
// Next.js App Router 示例
// 默认静态渲染 SSG，构建时生成 HTML
export const revalidate = 3600; // 开启 ISR：每小时重新生成

export default async function Page() {
  const res = await fetch('https://api.example.com/posts', {
    next: { revalidate: 3600 },
  });
  const posts = await res.json();

  return <ul>{posts.map((p) => <li key={p.id}>{p.title}</li>)}</ul>;
}
```
