---
title: [NODE-051] BFF 的多层缓存策略如何设计？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-051：BFF 的多层缓存策略如何设计？
**答**：
- 从近到远四级：① **进程内缓存**（lru-cache，微秒级，存热点配置/会话，TTL 短防不一致）；② **Redis 集中缓存**（跨实例共享，毫秒级，存聚合结果与下游数据）；③ **HTTP 缓存**（`Cache-Control`/`ETag` 让 CDN 与浏览器缓存 GET 响应，BFF 接口要谨慎——带 cookie 的个性化响应必须 `private`）；④ **下游缓存**（复用下游自身缓存，BFF 加 `If-None-Match` 透传）。
- 关键原则：**缓存键必须包含所有影响结果的变量**（uid、版本、语言、AB 分桶），否则串数据；用户态数据慎缓存；写后失效用主动 `DEL` + 短 TTL 双保险。
- 命中率观测：每层打 `hit/miss` 指标，用 `Server-Timing` 头暴露给前端调试。

```javascript
const LRU = require('lru-cache');

// 一级：进程内 LRU
const localCache = new LRU({ max: 500, ttl: 1000 * 30 });          // 30s
// 二级：Redis
const redisTTL = 300;

async function cached(ctx, key, loader, opts = {}) {
  const fullKey = `${opts.namespace ?? 'bff'}:${key}`;              // 命名空间隔离

  // L1 进程内
  const local = localCache.get(fullKey);
  if (local !== undefined) { ctx.state.cache = 'L1'; return local; }

  // L2 Redis
  const remote = await redis.get(fullKey);
  if (remote) {
    const data = JSON.parse(remote);
    localCache.set(fullKey, data);                                   // 回填 L1
    ctx.state.cache = 'L2';
    return data;
  }

  // 回源
  const data = await loader();
  const ttl = (opts.ttl ?? redisTTL) + Math.floor(Math.random() * 60); // 抖动防雪崩
  await redis.setex(fullKey, ttl, JSON.stringify(data));
  localCache.set(fullKey, data);
  ctx.state.cache = 'MISS';
  return data;
}

// 使用：商品详情聚合结果缓存（key 含版本号与语言）
router.get('/product/:id', async (ctx) => {
  const lang = ctx.get('accept-language') || 'zh';
  const product = await cached(ctx, `product:${ctx.params.id}:${lang}:${PRODUCT_VER}`, () =>
    fetchProduct(ctx.params.id));
  ctx.set('server-timing', `cache;desc="${ctx.state.cache}"`);
  ctx.body = product;
});

// 写操作主动失效
router.post('/product/:id', async (ctx) => {
  await updateProduct(ctx.params.id, ctx.request.body);
  const keys = [`bff:product:${ctx.params.id}:*:${PRODUCT_VER}`];
  // Redis 不支持通配删除，SCAN + DEL 或维护 key 集合
  for await (const key of redis.scanStream({ match: `bff:product:${ctx.params.id}:*` })) {
    await redis.del(...key);
  }
  ctx.body = { ok: true };
});
```
