---
title: [MFW-095] 笔试：手写一个 Nitro API 限流中间件（令牌桶 + 分用户）
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-095：笔试：手写一个 Nitro API 限流中间件（令牌桶 + 分用户）
**题目**：为 `server/api/**` 实现限流中间件：① 按 API key（header `x-api-key`）区分用户，每用户独立配额（如 100 次/分钟）；② 用令牌桶算法平滑限流（允许短时突发）；③ 超限返回 429 且带 `Retry-After`；④ 多实例部署时能指出内存实现的局限与 Redis 方案的改造点。

```ts
// server/middleware/rate-limit.ts
import { Store } from './token-bucket';

// 令牌桶：capacity 容量 / refillRate 每秒补充数
class TokenBucket {
  tokens: number;
  last: number;
  constructor(public capacity: number, public refillRate: number) {
    this.tokens = capacity;
    this.last = Date.now();
  }
  tryTake(): boolean {
    const now = Date.now();
    // 先按流逝时间补充令牌（不超过容量）
    this.tokens = Math.min(this.capacity, this.tokens + ((now - this.last) / 1000) * this.refillRate);
    this.last = now;
    if (this.tokens >= 1) { this.tokens -= 1; return true; }
    return false;
  }
  retryAfterMs(): number {
    return Math.ceil(((1 - this.tokens) / this.refillRate) * 1000);
  }
}

const store = new Map<string, TokenBucket>(); // 单实例内存版

export default defineEventHandler((event) => {
  const path = event.path;
  if (!path.startsWith('/api/')) return; // 只限流 API

  const apiKey = getHeader(event, 'x-api-key') ?? 'anonymous';
  const bucket = store.get(apiKey) ?? new TokenBucket(100, 100 / 60); // 100 次/60s
  store.set(apiKey, bucket);

  if (!bucket.tryTake()) {
    const retrySec = Math.ceil(bucket.retryAfterMs() / 1000);
    throw createError({
      statusCode: 429,
      statusMessage: 'Too Many Requests',
      headers: { 'Retry-After': String(retrySec) },
    });
  }
  // 响应头反馈余量，方便客户端自适应
  setHeader(event, 'X-RateLimit-Remaining', String(Math.floor(bucket.tokens)));
});
```

```ts
// Redis 改造点（口头阐述即可，写入代码注释）：
// 1. Map 换 Redis：KEY = rl:{apiKey}，value 用 INCR + EXPIRE 60（固定窗口）
//    或 Lua 脚本实现真令牌桶（tokens/last 两个字段原子更新）。
// 2. 多实例一致性：所有实例读写同一 Redis，配额全局准确。
// 3. 防用户级 DoS：匿名 key 也要限（更低配额），命中黑名单直接 403。
```

**评分点**：
1. 令牌桶实现正确：按流逝时间补充且封顶容量，取令牌失败计算 Retry-After。
2. 分用户维度隔离（API key 维度桶），配额语义「每分钟 100 次」正确换算 refillRate。
3. 429 响应带 Retry-After 头，语义规范。
4. 主动指出单实例 Map 的局限（多实例配额不共享、重启丢失）并给出 Redis 方案——这是本题区分度。
5. 只对 /api/ 生效，不误伤静态资源与页面渲染。
