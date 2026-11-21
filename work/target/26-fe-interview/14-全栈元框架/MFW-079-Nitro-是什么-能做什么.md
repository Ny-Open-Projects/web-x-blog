---
title: [MFW-079] Nuxt 的 Nitro 是什么，它承担了哪些职责？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-079：Nuxt 的 Nitro 是什么，它承担了哪些职责？
**答**：
- Nitro 是 Nuxt 的**服务端引擎**（也可独立用于非 Nuxt 项目）：把服务端代码构建成可部署的 server bundle，屏蔽部署目标差异（Node/Serverless/Edge）。
- 四大职责：① `server/api`、`server/routes` 的 API 服务；② routeRules 路由级缓存/重写/代理的执行层；③ 存储抽象（`useStorage`，统一内存/FS/Redis/S3）；④ 产出多目标 preset 产物（vercel、cloudflare、node-server、static 等）。
- 对前端的意义：BFF 不用另起 Node 项目——`server/api/*.ts` 就是类型化 API 层，`$fetch('/api/...')` 前后端类型贯通（h3 + nitro 自动类型生成）。
- 类比：Nitro 之于 Nuxt ≈ Next 的 server 运行时 + next.config 部署适配层合体，但目标适配面更广（unjs 生态）。

```ts
// server/api/products/[id].get.ts —— 文件即路由，类型自动贯通
export default defineEventHandler(async (event) => {
  const id = getRouterParam(event, 'id');
  const query = getQuery(event);
  const product = await db.product.findUnique({
    where: { id },
    select: { id: true, name: true, price: true },
  });
  if (!product) throw createError({ statusCode: 404, statusMessage: 'Not Found' });
  return product; // 前端 useFetch('/api/products/xx') 拿到的类型与这里返回一致
});
```

```ts
// server/middleware/auth.ts —— Nitro 中间件：API 请求先过这里
export default defineEventHandler((event) => {
  const token = getHeader(event, 'authorization');
  if (event.path.startsWith('/api/admin') && token !== `Bearer ${process.env.ADMIN_TOKEN}`) {
    throw createError({ statusCode: 401, statusMessage: 'Unauthorized' });
  }
});
```

```ts
// useStorage：统一 KV 抽象（本地 FS / Redis / S3 由配置切换）
export default defineEventHandler(async () => {
  const storage = useStorage('cache');
  const hit = await storage.getItem('hot:list');
  if (hit) return hit;
  const fresh = await computeHotList();
  await storage.setItem('hot:list', fresh, { ttl: 300 });
  return fresh;
});
```
