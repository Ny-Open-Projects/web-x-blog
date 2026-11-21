---
title: [NODE-322] Node 服务的接口幂等框架？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-322：Node 服务的接口幂等框架？
**答**:
- 框架化：幂等作为中间件——按 Idempotency-Key 头拦截：首次执行记录（key→结果 hash+存储），重复请求直接回放结果。
- 存储：Redis（短 TTL）存结果快照 + DB 唯一键兜底（关键业务）。
- 范围声明：路由元数据声明幂等窗口（如 24h）与范围（全响应 vs 状态）。
- 与重试配合：客户端指数退避重试（NODE-300）依赖服务端幂等——两端协议成对出现。

```javascript
// 幂等中间件
function idempotency({ ttl = 86400 } = {}) {
  return async (ctx, next) => {
    const key = ctx.get('Idempotency-Key');
    if (!key) return next();
    const saved = await redis.get(`idem:${key}`);
    if (saved) { const r = JSON.parse(saved); ctx.status = r.status; ctx.body = r.body; ctx.set('X-Idempotent-Replay', '1'); return; }
    await next();
    if (ctx.status < 500) await redis.set(`idem:${key}`, JSON.stringify({ status: ctx.status, body: ctx.body }), { ex: ttl });
  };
}
// 路由声明：router.post('/orders', idempotency({ ttl: 86400 }), handler)
```
