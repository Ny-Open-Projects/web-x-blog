---
title: [MFW-495] 笔试：手写 ISR 回源比例控制器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-495：ISR 回源比例（dogpile）控制器
**需求**：实现 `OriginGuard({ maxPerMin = 60 })`：1) 缓存过期瞬间大量并发回源（dogpile）要限流：`admit(key)` 按每分钟配额放行真实回源，超出的返回 `stale`（允许继续用旧值并延时重试——SWR 兜底）；2) 每 key 单飞已在上一层做，这里防的是"多 key 同时过期"的总量风暴（如整点批量过期）；3) 配额按令牌桶：容量 = maxPerMin，每秒匀速回填；4) 拒绝时带 `retryAfter` 建议（错峰到桶回填时刻）。

```javascript
export class OriginGuard {
  constructor({ maxPerMin = 60 } = {}) {
    this.capacity = maxPerMin
    this.tokens = maxPerMin
    this.rate = maxPerMin / 60 // 每秒回填
    this.last = Date.now()
  }

  refill() {
    const now = Date.now()
    const gain = (now - this.last) / 1000 * this.rate
    this.tokens = Math.min(this.capacity, this.tokens + gain)
    this.last = now
  }

  admit(key) {
    this.refill()
    if (this.tokens >= 1) {
      this.tokens -= 1
      return { allow: true }
    }
    const waitMs = Math.ceil((1 - this.tokens) / this.rate * 1000)
    return { allow: false, stale: true, retryAfter: waitMs } // 回源被限 → 继续用旧值
  }
}

// 用法：兜底语义 = 宁可旧不可倒（源站被 dogpile 打挂比多服务 30s 旧页严重得多）
```

**评分点**：
- 令牌桶匀速回填（防整点批量过期瞬时风暴——桶是正确模型）
- 拒绝时给 stale + retryAfter（调用方可继续服务旧值，不是拒绝用户）
- refill 惰性计算（无定时器，serverless 友好）
- 语义排序：宁可旧不可倒（回源限流的目的写明——面试官看价值判断）
