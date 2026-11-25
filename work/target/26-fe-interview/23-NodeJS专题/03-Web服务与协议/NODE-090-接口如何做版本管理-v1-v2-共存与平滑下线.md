---
title: [NODE-090] 接口如何做版本管理（v1/v2 共存与平滑下线）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-090：接口如何做版本管理（v1/v2 共存与平滑下线）？
**答**：
- 版本策略三选一：**URL 路径**（`/v2/orders`，最直白、CDN 友好，主流）、Header（`Accept: application/vnd.app.v2+json`，URL 干净但调试难）、域名（`api2.example.com`，成本高）。
- 共存实现：路由前缀隔离 + 共享 service 层（Controller 不同、逻辑复用）；版本差异大才拆模块。
- 平滑下线：旧版本标记 deprecated（响应头 `Deprecation` + `Sunset` + 埋点统计调用量）→ 通知调用方迁移 → 调用归零后下线；**先摘流量后删代码**。

```javascript
// 路由级版本管理：Controller 分版本，Service 复用
const v1 = new Router({ prefix: '/v1' });
const v2 = new Router({ prefix: '/v2' });

// service 层完全复用
async function listOrders({ uid, page, includeTotal }) {
  const rows = await orderService.listByUser(uid, page);
  const body = { data: rows.map(orderService.toBrief) };
  if (includeTotal) body.total = await orderService.countByUser(uid);
  return body;
}

v1.get('/orders', async (ctx) => {          // 旧版：offset 分页
  ctx.body = await listOrders({ uid: ctx.state.user.uid,
    page: { offset: Number(ctx.query.offset ?? 0), limit: 20 }, includeTotal: true });
});

v2.get('/orders', async (ctx) => {          // 新版：游标分页 + 新字段
  ctx.body = await listOrders({ uid: ctx.state.user.uid,
    page: { cursor: ctx.query.cursor, limit: Math.min(Number(ctx.query.size ?? 20), 50) },
    includeTotal: false });                  // v2 不再返回 total（性能优化）
});

app.use(v1.routes()).use(v2.routes());

// deprecation 中间件：统计 v1 调用量，通知调用方
app.use(async (ctx, next) => {
  await next();
  if (ctx.path.startsWith('/v1/')) {
    metrics.increment('api_deprecated_calls', { version: 'v1', path: ctx.path });
    ctx.set('deprecation', 'true');
    ctx.set('sunset', 'Wed, 31 Dec 2026 23:59:59 GMT');    // 计划下线时间
    ctx.set('link', '</v2/orders>; rel="successor-version"');
  }
});
```
