---
title: [AIC-174] 笔试：实现一个 LLM 网关限流器：令牌桶 + 按团队配额 + 排队等待与快速失败双模式？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-174：笔试：实现一个 LLM 网关限流器：令牌桶 + 按团队配额 + 排队等待与快速失败双模式？
**需求**：实现 `RateLimiter`：
- 全局令牌桶：容量 capacity、速率 refillPerSec（平滑限流而非硬窗口）；
- 按团队日配额（超配额直接拒绝，独立于令牌桶）；
- `acquire(team, { waitMs })`：waitMs=0 快速失败返回 `{ok:false, retryAfter}`；waitMs>0 排队等待（最长 waitMs）；
- retryAfter 按桶补充速率计算，供客户端退避。

```javascript
class RateLimiter {
  #tokens; #last; #usedToday = new Map();
  constructor({ capacity, refillPerSec, dailyQuota, now = Date.now() }) {
    this.capacity = capacity; this.refillPerSec = refillPerSec;
    this.dailyQuota = dailyQuota;
    this.#tokens = capacity; this.#last = now;
    this.#now = () => now; // 测试注入
  }
  #now;
  #refill(now) {
    const elapsed = (now - this.#last) / 1000;
    this.#tokens = Math.min(this.capacity, this.#tokens + elapsed * this.refillPerSec);
    this.#last = now;
  }
  #quotaKey(now) { return new Date(now).toISOString().slice(0, 10); }

  acquire(team, { waitMs = 0, cost = 1 } = {}) {
    const start = this.#now();
    const deadline = start + waitMs;
    // 1. 团队日配额
    const key = this.#quotaKey(start);
    const used = this.#usedToday.get(team) ?? { day: key, n: 0 };
    if (used.day !== key) { used.day = key; used.n = 0; }
    if (used.n >= this.dailyQuota) {
      return { ok: false, reason: 'daily-quota', retryAfter: 86400 };
    }
    // 2. 令牌桶（等待循环）
    for (;;) {
      const now = this.#now();
      this.#refill(now);
      if (this.#tokens >= cost) {
        this.#tokens -= cost;
        used.n += 1;
        this.#usedToday.set(team, used);
        return { ok: true, waited: now - start };
      }
      if (now >= deadline) {
        const need = cost - this.#tokens;
        return { ok: false, reason: 'rate-limit', retryAfter: Math.ceil(need / this.refillPerSec) };
      }
      this.#sleep?.(50); // 生产用真实 sleep；测试注入
    }
  }
}

// 测试
let fakeNow = Date.now();
const rl = new RateLimiter({ capacity: 5, refillPerSec: 1, dailyQuota: 100 });
rl.#sleep = () => { fakeNow += 100; };
rl.#now = () => fakeNow;
const results = [];
for (let i = 0; i < 8; i++) results.push(rl.acquire('goods', { waitMs: 0 }).ok);
console.log(results); // 前 5 true，之后 false（桶空、快速失败）
```

**评分点**：
1. 令牌桶语义正确：桶有容量上限、按速率平滑补充、取用扣减——比固定窗口更平滑；
2. 配额与限流是两层独立策略（日配额硬顶 + 瞬时速率桶）；
3. 快速失败必须带 retryAfter（按缺口 ÷ 速率估算），客户端才能正确退避；
4. 等待模式有 deadline 上限，不会无限排队；
5. 时间依赖注入（#now 可替换）使限流器可测试——工程素养加分项。
