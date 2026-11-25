---
title: [NODE-069] 设计一个网关限流中间件（令牌桶的分布式实现）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-069：设计一个网关限流中间件（令牌桶的分布式实现）？
**答**：
- 令牌桶：恒定速率往桶里放令牌（桶容量即突发上限），请求取令牌，无令牌则 429。相比固定窗口计数，**平滑**且允许突发；相比滑动窗口实现更简单。
- 分布式实现用 **Redis + Lua 原子计算**：`tokens = min(capacity, tokens + (now - last) * rate)`，取到则扣减，否则拒绝——两步计算必须在 Lua 里原子完成（读-改-写分开会有竞态）。
- 维度：按 IP（防爬虫）、按 uid（防单用户滥用）、按接口（保护脆弱下游）、全局（容量保护）。返回头带 `retry-after` 与剩余额度（`x-ratelimit-remaining`）。

```javascript
const Redis = require('ioredis');
const redis = new Redis();

// Lua：原子令牌桶
const TOKEN_BUCKET_LUA = `
  local key      = KEYS[1]
  local rate     = tonumber(ARGV[1])        -- 每秒生成令牌数
  local capacity = tonumber(ARGV[2])        -- 桶容量（突发上限）
  local now      = tonumber(ARGV[3])        -- 当前毫秒时间戳
  local cost     = tonumber(ARGV[4])        -- 本次消耗令牌数

  local data = redis.call('HMGET', key, 'tokens', 'ts')
  local tokens = tonumber(data[1]) or capacity
  local ts     = tonumber(data[2]) or now

  -- 按时间差补充令牌
  tokens = math.min(capacity, tokens + (now - ts) / 1000 * rate)
  local allowed = 0
  if tokens >= cost then
    tokens = tokens - cost
    allowed = 1
  end
  redis.call('HMSET', key, 'tokens', tokens, 'ts', now)
  redis.call('PEXPIRE', key, math.ceil(capacity / rate * 2000))  -- 冷却后自动清理
  return { allowed, tostring(math.floor(tokens)) }
`;

async function tryAcquire(dimension, key, cost = 1) {
  const rule = { ip: { rate: 20, capacity: 100 }, uid: { rate: 5, capacity: 30 } }[dimension];
  const [allowed, remaining] = await redis.eval(
    TOKEN_BUCKET_LUA, 1, `rl:${dimension}:${key}`,
    rule.rate, rule.capacity, Date.now(), cost,
  );
  return { allowed: allowed === 1, remaining: Number(remaining), retryAfter: Math.ceil(cost / rule.rate) };
}

// Koa 网关中间件：uid 优先（登录用户更精准），fallback 到 IP
function rateLimiter() {
  return async (ctx, next) => {
    const { allowed, remaining, retryAfter } = await tryAcquire(
      ctx.state.user ? 'uid' : 'ip', ctx.state.user?.uid ?? ctx.ip);
    ctx.set('x-ratelimit-remaining', String(remaining));
    if (!allowed) {
      ctx.set('retry-after', String(retryAfter));
      ctx.status = 429;
      ctx.body = { code: 'RATE_LIMITED', message: '请求过于频繁，请稍后重试' };
      return;
    }
    await next();
  };
}
```
