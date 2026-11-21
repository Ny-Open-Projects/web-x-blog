---
title: [NODE-132] 接口限流四种算法的完整实现对比（计数器/滑动窗口/漏桶/令牌桶）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-132：接口限流四种算法的完整实现对比（计数器/滑动窗口/漏桶/令牌桶）？
**答**：
- 固定窗口：`INCR+EXPIRE` 最简，但窗口边界存在 **2 倍突刺**（两个窗口交界瞬间可放过 2 倍配额）。
- 滑动窗口：ZSET 记录时间戳，`ZREMRANGEBYSCORE` 清过期 + `ZCARD` 计数——精确无突刺，内存与请求量成正比。
- 漏桶：恒定速率"漏水"，强行整流削平突发——适合保护脆弱下游；令牌桶：恒速补币 + 允许积攒突发——网关首选。
- 实现要点：全部用 **Redis + Lua** 保证"读-判-写"原子；集群多实例共享计数才叫分布式限流（NODE-069 是令牌桶专题）。

```javascript
// ── 1. 固定窗口：最简，有边界突刺 ──
const FIXED_LUA = `local c = redis.call("incr", KEYS[1])
if c == 1 then redis.call("expire", KEYS[1], ARGV[1]) end
return c`;
const windowSec = Math.floor(Date.now() / 60000);
const fixed = await redis.eval(FIXED_LUA, 1, `rl:f:${key}:${windowSec}`, 60);

// ── 2. 滑动窗口（ZSET）：精确，内存随请求量增长 ──
const SLIDE_LUA = `redis.call("zremrangebyscore", KEYS[1], 0, ARGV[1])
local n = redis.call("zcard", KEYS[1])
if n < tonumber(ARGV[2]) then
  redis.call("zadd", KEYS[1], ARGV[1], ARGV[3])
  redis.call("pexpire", KEYS[1], tonumber(ARGV[4]))
  return 1
end
return 0`;
// ARGV：当前毫秒、上限、唯一成员、窗口毫秒
const slid = await redis.eval(SLIDE_LUA, 1, `rl:s:${key}`, Date.now(), 100, crypto.randomUUID(), 60000);

// ── 3. 漏桶：恒定速率放行，保护脆弱下游 ──
const LEAKY_LUA = `local d = redis.call("hmget", KEYS[1], "water", "ts")
local water = tonumber(d[1]) or 0
local leaked = math.max(0, water - (tonumber(ARGV[1]) - (tonumber(d[2]) or ARGV[1])) * tonumber(ARGV[2]))
local ok = 0
if leaked < tonumber(ARGV[3]) then water = math.min(leaked + 1, tonumber(ARGV[3])); ok = 1 end
redis.call("hmset", KEYS[1], "water", water, "ts", ARGV[1])
return ok`;
// ARGV：当前毫秒、每秒流出速率、桶容量
const leaky = await redis.eval(LEAKY_LUA, 1, `rl:l:${key}`, Date.now(), 50, 100);

// ── 4. 令牌桶：控平均速率又允许突发，网关首选 ──
const TOKEN_LUA = `local ts = tonumber(ARGV[1])
local d = redis.call("hmget", KEYS[1], "tokens", "ts")
local cap = tonumber(ARGV[3])
local tokens = math.min((tonumber(d[1]) or cap) + (ts - (tonumber(d[2]) or ts)) * tonumber(ARGV[2]), cap)
local ok = 0
if tokens >= 1 then tokens = tokens - 1; ok = 1 end
redis.call("hmset", KEYS[1], "tokens", tokens, "ts", ts)
return ok`;
// ARGV：当前毫秒、每秒补币速率、桶容量
const token = await redis.eval(TOKEN_LUA, 1, `rl:t:${key}`, Date.now(), 100, 200);
// 选型：统计防刷 → 固定窗口；精确配额 → 滑动窗口；保护下游 → 漏桶；网关通用 → 令牌桶
```

---

## 十六、可观测性深入
