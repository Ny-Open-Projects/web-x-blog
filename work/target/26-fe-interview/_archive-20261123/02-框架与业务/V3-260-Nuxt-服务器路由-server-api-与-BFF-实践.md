---
title: [V3-260] Nuxt 的 server routes（server/api）与 BFF 实践是怎样的？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-260：Nuxt 的 server routes（server/api）与 BFF 实践是怎样的？
**答**：
- 定义：`server/api/*.get.ts|post.ts`、`server/routes/**` 由 Nitro 注册为服务端路由（h3 框架），与前端代码同仓库部署。
- BFF 价值：聚合下游微服务、隐藏鉴权凭证、做 SSR 专用数据装配；`$fetch('/api/xxx')` 前端直接调，服务端内部用 `useRuntimeConfig` 拿密钥。
- 上下文能力：`defineEventHandler` 中可用 `getRouterParam/getQuery/readBody`、`setHeader`（缓存/CORS）、事件上下文（每请求 cookie/session）。
- 复用与分层：共享逻辑放 `server/utils`（auto-import）；大项目建议 server 层只做"聚合与协议转换"，业务规则仍在服务域。
- 部署注意：Nitro 的 serverless preset 下 server/api 与页面同函数部署，注意冷启动与数据库连接池（用 HTTP 连接或边缘 DB）。

```typescript
// server/api/products/[id].get.ts —— BFF 聚合
export default defineEventHandler(async (event) => {
  const id = getRouterParam(event, 'id');
  const config = useRuntimeConfig(event);          // 密钥只在服务端
  const [detail, inventory, reviews] = await Promise.all([
    $fetch(`${config.base}/product/${id}`, { headers: { key: config.key } }),
    $fetch(`${config.base}/stock/${id}`),
    $fetch(`${config.base}/review/${id}?top=3`),
  ]);
  setHeader(event, 'cache-control', 's-maxage=60, stale-while-revalidate=300');
  return { ...detail, stock: inventory.count, topReviews: reviews };
});
```
