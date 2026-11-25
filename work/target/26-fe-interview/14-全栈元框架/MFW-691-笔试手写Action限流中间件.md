---
title: [MFW-691] 笔试：手写 Action 限流中间件
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-691：笔试：手写 Action 限流

**答**：实现 `createActionRateLimit({ limiter, { now } })`。limiter: `(key, limit, windowMs) => Promise<{ allowed, remaining, reset }>`。配置：`Record<actionId, { limit, windowMs }>`（per-action 配置）。规则：1) 请求限流：actionId 在配置中 → limiter(actionId + ':' + userId, limit, windowMs)；未配置 actionId → 默认限流（10/min——通用桶）；2) 429 响应带 Retry-After（reset − now 秒数）；3) **burst 容忍**：token bucket 的语义——burst = limit（首突发可用完 tokens；平均速率 = limit/windowMs）；4) 限流的降级：limiter 失败（Redis down）→ 放行（fail-open——限流器故障不能阻塞业务 RBL-679 fail-open 哲学）。返回 middleware(req) 函数。边界：actionId 缺失（非 Action 请求——放行）；limiter 抛错（fail-open 放行 + 告警计数）。

```javascript
function createActionRateLimit({ limiter, configs = {}, defaultLimit = { limit: 10, windowMs: 60000 }, now = Date.now } = {}) {
  const stats = { limited: 0, degraded: 0 };
  return async function middleware(req) {
    const actionId = req.headers.get('next-action');
    if (!actionId) return { status: 200, headers: {} };   // 非 Action 放行
    const cfg = configs[actionId] ?? defaultLimit;
    const userId = req.headers.get('x-session') ?? 'anon';
    const key = `${actionId}:${userId}`;
    let result;
    try {
      result = await limiter(key, cfg.limit, cfg.windowMs);
    } catch (e) {
      stats.degraded++;                                  // limiter 故障：fail-open
      return { status: 200, headers: { 'x-rl-degraded': '1' } };
    }
    if (!result.allowed) {
      stats.limited++;
      return { status: 429,
        headers: { 'retry-after': Math.max(1, Math.ceil((result.reset - now()) / 1000)).toString() } };
    }
    return { status: 200, headers: { 'x-ratelimit-remaining': String(result.remaining) } };
  };
}

// 自测
const tokens = new Map(); let t = 1000000;
const limiter = async (key, limit, windowMs) => {
  const cur = tokens.get(key) ?? { tokens: limit, reset: t + windowMs };
  if (t >= cur.reset) { cur.tokens = limit; cur.reset = t + windowMs; }
  if (cur.tokens <= 0) return { allowed: false, remaining: 0, reset: cur.reset };
  cur.tokens--;
  tokens.set(key, cur);
  return { allowed: true, remaining: cur.tokens, reset: cur.reset };
};
const rl = createActionRateLimit({ limiter,
  configs: { 'order_abc': { limit: 2, windowMs: 60000 } }, now: () => t });
const req = { headers: new Map([['next-action', 'order_abc'], ['x-session', 'u1']]) };
const h = (k) => req.headers.get(k);

// 前 2 次通过
let r1 = await rl({ headers: { get: (k) => h(k) } });
console.log(r1.status === 200);
let r2 = await rl({ headers: { get: (k) => h(k) } });
console.log(r2.status === 200 && r2.headers['x-ratelimit-remaining'] === '0');
// 第 3 次 429
let r3 = await rl({ headers: { get: (k) => h(k) } });
console.log(r3.status === 429 && +r3.headers['retry-after'] > 0);

// 不同 user 独立桶
const req2 = { headers: { get: (k) => k === 'next-action' ? 'order_abc' : k === 'x-session' ? 'u2' : null } };
const r4 = await rl({ headers: { get: (k) => req2.headers.get(k) } });
console.log(r4.status === 200);

// 非 Action 放行
r = await rl({ headers: { get: () => null } });
console.log(r.status === 200);

// limiter 故障 fail-open
const broken = createActionRateLimit({ limiter: async () => { throw new Error('redis'); } });
r = await broken({ headers: { get: () => 'action_x' } });
console.log(r.status === 200 && r.headers['x-rl-degraded'] === '1');
```

**评分点**：
- per-action 复合键（actionId × userId——维度组合 RBL-690）；默认桶（未配置 actionId）
- fail-open（limiter 故障放行 + degraded 标记——限流器不阻塞业务）；429 + Retry-After
- token bucket 的 burst 语义；边界（非 Action/故障/独立桶）
- 能说清「Action 限流的维度是 actionId × userId——middleware 层统一限流是框架级防线」属于加分
