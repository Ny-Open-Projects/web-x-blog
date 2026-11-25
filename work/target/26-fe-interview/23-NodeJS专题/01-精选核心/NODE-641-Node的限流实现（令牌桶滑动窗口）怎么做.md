---
title: [NODE-641] Node 的限流实现（令牌桶/滑动窗口）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## NODE-641：限流怎么做？
**答**：
- 算法选择：固定窗口（简单但边界突刺 ×2）、滑动窗口（精确、计数器实现略重）、令牌桶（允许突发 + 平均速率——最常用）、漏桶（整形输出恒速）。
- 分布式限流：多实例共享计数——Redis Lua（原子：读-判-写一个脚本，集群下 hash tag 保证同 key 同 slot）；本地令牌桶只适合单实例。
- 维度设计：按 IP/用户/API/租户多级（全局总限流 + 租户配额 + 接口限流——漏斗式）；响应携带限流头（X-RateLimit-Remaining/Retry-After——客户端友好，SCN-OPS-585 限流协同）。
- 降级语义：429 + Retry-After 而非静默丢；限流前的优先级队列（核心接口让路）。
- 追问钩子：为什么令牌桶比固定窗口更适合 API 限流——固定窗口在窗口边界允许 2× 突刺（两个窗口交界各满额）；令牌桶以恒定速率补充令牌，突发上限 = 桶容量、平均速率 = 补充速率——「平均可控 + 突发可控」两个维度都精确，边界突刺问题天然不存在。

```javascript
// Redis Lua 令牌桶（原子）
const script = `
  local tokens = tonumber(redis.call('hget', KEYS[1], 'tokens') or ARGV[2])
  local last = tonumber(redis.call('hget', KEYS[1], 'ts') or 0)
  local now = tonumber(ARGV[1])
  tokens = math.min(ARGV[2], tokens + (now - last) * tonumber(ARGV[3]) / 1000)
  if tokens < 1 then return 0 end
  redis.call('hset', KEYS[1], 'tokens', tokens - 1, 'ts', now)
  return 1`;
const allowed = await redis.eval(script, 1, key, Date.now(), capacity, refillRate);
```
