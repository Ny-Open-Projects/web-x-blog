---
title: [NODE-731] 笔试题——实现分布式限流中间件（Lua 令牌桶 + 限流头）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-731：手写分布式限流

**需求与边界**：
- 需求：Redis Lua 令牌桶（SCN-NODE-641）——① 多维度（ip/user/api——键组合）；② 限流头（Remaining/Retry-After——客户端友好）；③ 超限响应 429（可重试语义——Retry-After）；④ 降级（Redis 挂 → 本地限流兜底——fail-open 有界）。
- 边界：① Lua 原子（读-判-写——SCN-NODE-641）；② key 过期（计数器 TTL——无限增长防御）；③ Redis 故障降级（本地桶——有界的 fail-open，声明降级）。

**答**：
```javascript
const LUA = `
  local tokens = tonumber(redis.call('hget', KEYS[1], 't') or ARGV[2])
  local ts = tonumber(redis.call('hget', KEYS[1], 'ts') or ARGV[1])
  tokens = math.min(ARGV[2], tokens + (ARGV[1] - ts) * tonumber(ARGV[3]) / 1000)
  if tokens < 1 then redis.call('hset', KEYS[1], 't', tokens, 'ts', ARGV[1])
    return {0, math.floor(tokens)} end
  redis.call('hset', KEYS[1], 't', tokens - 1, 'ts', ARGV[1])
  redis.call('expire', KEYS[1], ARGV[4])
  return {1, math.floor(tokens - 1)}`;
function rateLimit(dims) {
  return async (req, res, next) => {
    const key = `rl:${dims.map(d => d.value(req)).join(':')}`;   // ip:user:api 组合
    let allowed;
    try { [allowed, remain] = await redis.eval(LUA, 1, key, Date.now(), cap, refill, ttl); }
    catch { allowed = localBucket.tryTake() ? 1 : 0; }   // Redis 挂：本地兜底（fail-open 有界）
    res.setHeader('X-RateLimit-Remaining', remain ?? 0);
    if (!allowed) {
      res.setHeader('Retry-After', Math.ceil(1 / refill));
      return res.status(429).json({ code: 'RATE_LIMITED', retryable: true });
    }
    next();
  };
}
```

**评分点**:
- Lua 令牌桶原子（读-判-写——SCN-NODE-641）。
- 多维度键组合 + TTL（计数器过期——无限增长防御）。
- 限流头三件套（Remaining/Retry-After/429 retryable——SCN-OPS-585 协同）。
- Redis 故障本地兜底（有界 fail-open + 降级声明）。

## 变体与延伸（补充）

**变体与延伸**：

1. 要求多点部署下总配额精确不超发，Lua 令牌桶够吗 → 够，前提是同 key 落同一分片且读判写全在一个 Lua 里，跨分片求和必然有误差，要在答案里点明这个前提。
2. Redis 整体故障时降级到本地桶，会不会反而把下游打挂 → 本地配额按实例数均摊（全局 QPS 除以实例数）并设 10s fail-open 上限，超时转 fail-close 保下游。
3. 多维度限流时 Remaining 头返回哪个维度 → 返回最严格维度的剩余量并附 X-RateLimit-Policy 指明命中维度，否则客户端会按宽松维度重试。
