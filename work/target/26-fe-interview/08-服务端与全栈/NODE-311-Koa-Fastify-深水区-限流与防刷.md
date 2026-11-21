---
title: [NODE-311] Koa/Fastify 深水区：限流与防刷？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-311：Koa/Fastify 深水区：限流与防刷？
**答**:
- 限流三层：网关层（Nginx limit_req，粗粒度 IP）→ 应用层（业务维度：uid/接口分级）→ 下游保护（客户端限流器防放大）。
- 应用层算法：固定窗口（简单有边界突刺）、滑动窗口（平滑）、令牌桶（允许突发）——Redis + Lua 原子实现（NODE-243 分布式一致性）。
- 防刷增值：设备指纹+行为验证（验证码）在限流触发后升级——限流是第一道不是唯一道。
- 返回语义：429 + Retry-After 头——客户端按退避重试（NODE-45x 分级超时配合）。

```javascript
// Redis + Lua 滑动窗口限流
const SCRIPT = `
local key = KEYS[1]
local now = tonumber(ARGV[1]) local window = tonumber(ARGV[2]) local limit = tonumber(ARGV[3])
redis.call('ZREMRANGEBYSCORE', key, 0, now - window)
local n = redis.call('ZCARD', key)
if n < limit then redis.call('ZADD', key, now, now .. '-' .. math.random()) redis.call('EXPIRE', key, window/1000) return 1 end
return 0
`;
async function rateLimit(uid, route) {
  const ok = await redis.eval(SCRIPT, 1, `rl:${route}:${uid}`, Date.now(), 60000, limits[route]);
  if (!ok) { ctx.status = 429; ctx.set('Retry-After', '60'); throw new RateLimitError(); }
}
```
