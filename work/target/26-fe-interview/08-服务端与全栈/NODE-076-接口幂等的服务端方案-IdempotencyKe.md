---
title: [NODE-076] 接口幂等的服务端方案（Idempotency-Key）如何设计？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-076：接口幂等的服务端方案（Idempotency-Key）如何设计？
**答**：
- 问题：网络重试、用户双击导致同一请求多次到达，支付/下单类接口重复执行会造成资金损失。
- 方案：客户端生成唯一 **Idempotency-Key**（uuid）随请求携带 → 服务端以 key 为锁：首次请求执行业务并把**响应快照**存 Redis（`SET NX`，TTL 24h）；重复请求直接返回快照（status + body 原样回放）；正在执行中的相同 key 返回 409 或挂起等待。
- 细节：key 作用域按"接口 + 用户"隔离（不同接口同 key 不冲突）；响应快照含状态码；处理中标记 `:processing` 防并发穿透；超时/失败的 key 要允许清理重试。

```javascript
const IDEMPOTENT_TTL = 24 * 3600;

function idempotent() {
  return async (ctx, next) => {
    const key = ctx.get('idempotency-key');
    if (!key) return next();                       // 幂等头可选：GET/DELETE 天然幂等可不带

    const scope = `${ctx.method}:${ctx.path}:${ctx.state.user.uid}:${key}`;
    const snapshotKey = `idem:${scope}:result`;
    const processingKey = `idem:${scope}:processing`;

    // 1. 已有结果快照：直接回放
    const cached = await redis.get(snapshotKey);
    if (cached) {
      const { status, body } = JSON.parse(cached);
      ctx.status = status;
      ctx.set('idempotent-replayed', 'true');
      ctx.body = body;
      return;
    }
    // 2. 正在处理：拒绝并发重复（客户端稍后重试会拿到快照）
    const locked = await redis.set(processingKey, '1', 'EX', 60, 'NX');
    if (!locked) { ctx.status = 409; ctx.body = { code: 'PROCESSING', message: '请求处理中，请稍后重试' }; return; }

    try {
      await next();
      // 3. 成功响应存快照（失败不存，允许客户端修正后重试）
      if (ctx.status < 400) {
        await redis.setex(snapshotKey, IDEMPOTENT_TTL,
          JSON.stringify({ status: ctx.status, body: ctx.body }));
      }
    } finally {
      await redis.del(processingKey);
    }
  };
}

// 挂载：仅对写操作
router.post('/orders', idempotent(), createOrder);

// 客户端配合
// fetch('/api/orders', { method: 'POST',
//   headers: { 'idempotency-key': crypto.randomUUID() },   // 同一次用户意图复用同一 key
//   body: JSON.stringify({ sku: 'A001', count: 1 }) });
```
