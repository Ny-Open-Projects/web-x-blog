---
title: [NODE-360] Node 服务的接口限流实现细节（算法与分布式）如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-360：接口限流的实现细节
**答**:
- 算法选型：固定窗口（实现简单，窗口边界突刺）、滑动窗口（精确，内存/计算略高）、令牌桶（允许突发、平滑，推荐默认）、漏桶（整形强制匀速）。BFF 按维度组合：用户级（令牌桶）+ 接口级（滑动窗口）+ 全局保护（固定窗口兜底）。
- 分布式实现：Redis + Lua 原子计数（窗口/桶状态在 Redis，Lua 保证原子）；热点场景预分配本地配额（每实例令牌配额，减少 Redis 往返）；取舍说明必须写清（本地配额总计 = 全局限额，实例数变化需再平衡）。
- 语义细节：429 响应带 Retry-After 与限流头（X-RateLimit-Remaining）；被限流的计费（按用户维度告警异常量——可能是攻击或 bug）；白名单（内部探活）。
- 分层限流：网关层（粗粒度 IP/UA）→ BFF 用户级 → 下游保护（对下游的调用限流防止打挂别人）。
- 观测：限流触发率按接口/用户分桶，突增自动告警。
```javascript
// Redis Lua 令牌桶
const LUA = `local r = redis.call('hmget', KEYS[1], 'tokens', 'ts')
local tokens = tonumber(r[1]) or tonumber(ARGV[1])
local ts = tonumber(r[2]) or tonumber(ARGV[2])
local now = tonumber(ARGV[2])
tokens = math.min(tonumber(ARGV[1]), tokens + (now - ts) * tonumber(ARGV[3]))
if tokens >= 1 then tokens = tokens - 1 allowed = 1 else allowed = 0 end
redis.call('hmset', KEYS[1], 'tokens', tokens, 'ts', now) return allowed`;
const allowed = await redis.eval(LUA, 1, `rl:${uid}`, CAPACITY, nowMs, REFILL_RATE);
if (!allowed) { ctx.status = 429; ctx.set('Retry-After', '1'); }
```

**追问**：

1. Lua 里为什么要先读再写，不能直接 INCR？→ INCR 只能表达固定窗口，令牌桶要按时间差补令牌，读改写在同一段脚本里才原子。
2. Redis Cluster 下多维度限流怎么落地？→ 同一请求限 uid 和接口两个 key 时用 hash tag 落同槽，否则拆成两次 eval 并接受非严格原子。
3. 本地预分配配额遇到实例扩容怎么办？→ 按新实例数重算每实例配额并允许一个窗口的过冲，否则滚动发布期间总限额被临时放大。
