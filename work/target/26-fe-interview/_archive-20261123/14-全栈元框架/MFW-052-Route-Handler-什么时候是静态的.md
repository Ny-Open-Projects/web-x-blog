---
title: [MFW-052] Route Handler 什么时候是静态的，什么时候是动态的？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-052：Route Handler 什么时候是静态的，什么时候是动态的？
**答**：
- 默认判断：只使用 GET 方法、且不读请求动态数据（cookies/headers/searchParams）的 handler 会在**构建期执行一次**并把响应静态化；一旦读动态 API 就变成每请求执行。
- GET 之外（POST/PUT 等）永远是动态的——Server Actions 底层的 POST 不可能被缓存。
- 可用 `export const dynamic = 'force-static' | 'force-dynamic'` 显式覆盖；`revalidate` 控制静态响应的 ISR 周期。
- 常见坑：handler 里顺手读了一下 `request.headers.get('user-agent')`，静态化就悄悄失效，构建日志里能看到 `ƒ (Dynamic)` 标记，上线前要盯。

```ts
// app/api/recommend/route.ts

// 静态：构建期执行一次，CDN 可长缓存
export const revalidate = 600;
export async function GET() {
  const list = await getHotProducts(); // 不碰请求对象
  return Response.json(list);
}
```

```ts
// app/api/user-profile/route.ts

// 动态：读取 cookie，每请求执行
export const dynamic = 'force-dynamic';
export async function GET(request: Request) {
  const uid = (await cookies()).get('uid')?.value; // 碰了动态 API
  if (!uid) return Response.json({ error: 'unauthorized' }, { status: 401 });
  return Response.json(await getUserProfile(uid));
}
```
