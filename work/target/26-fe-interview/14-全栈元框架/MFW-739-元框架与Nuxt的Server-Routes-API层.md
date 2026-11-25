---
title: [MFW-739] Nuxt Server Routes 的 API 层
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-739：Nuxt Server Routes 的 API 层

**答**:
- Nuxt 的 server 目录：1) **server/api/**（文件路由 API——`server/api/user.get.ts` → GET /api/user；`user.post.ts` → POST——文件名即方法 RBL-524 的 Nuxt 版）；2) **Nitro 引擎**（独立于 Vue 层的 server 引擎 RBL-530——api 层跑在 Nitro；3) **defineEventHandler**（统一事件处理——`getRouterParam/readBody/createError`——Web 标准 Request/Response 的 Nuxt 包装。
- 与 Next Route Handlers 的对比：Next：app/api/*/route.ts（导出 HTTP 方法函数）；Nuxt：server/api/*.get.ts（文件名 = 方法）；「文件名的语义」：Nuxt 的 .get.ts/.post.ts 后缀 = 方法的文件级声明（比 Next 的导出函数更显式）；「目录即路由」的共同哲学。
- server middleware（Nitro 中间件）：server/middleware/*.ts——API 层的全局中间件（auth/cors/log——Nuxt 版 middleware）。
- 追问钩子：为什么「文件名 = HTTP 方法」比「导出 = HTTP 方法」更适合 API 层？——文件名的显式性：`user.get.ts` 看文件名即知方法（不用打开文件看导出）；一个方法一个文件（`user.get.ts` + `user.post.ts`——分离而非同文件多导出）；「文件的单一职责」：每个文件一个 handler（可测/可维护）——vs Next 的 route.ts 多导出（一个文件多方法——内聚但文件大）——两种约定的权衡：显式分离 vs 内聚紧凑。

```typescript
// server/api/user.get.ts
export default defineEventHandler(async (event) => {
  const id = getRouterParam(event, 'id');
  const query = getQuery(event);
  return await db.users.find(id ?? query.id);
});
// server/api/user.post.ts
export default defineEventHandler(async (event) => {
  const body = await readBody(event);
  const parsed = UserSchema.safeParse(body);
  if (!parsed.success)
    throw createError({ statusCode: 422, data: parsed.error.flatten() });
  return await db.users.create(parsed.data);
});
// server/middleware/auth.ts（Nitro 中间件）
export default defineEventHandler((event) => {
  const token = getHeader(event, 'authorization');
  if (!token && event.path.startsWith('/api/protected'))
    throw createError({ statusCode: 401 });
});
// server/routes/（自定义路由——非 /api 前缀）
// server/routes/sitemap.xml.get.ts → GET /sitemap.xml
```
