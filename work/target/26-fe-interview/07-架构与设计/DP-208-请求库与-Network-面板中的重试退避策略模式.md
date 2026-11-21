---
title: [DP-208] 源码识别：请求重试与退避中的策略与状态模式？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-208：源码识别：请求重试与退避中的策略与状态模式？
**答**：
- 策略模式：退避算法（固定/线性/指数/抖动 AIMD）实现同一 `nextDelay(attempt) → ms` 接口，可注入替换（弱网策略/大促策略不同）。
- 状态模式：请求生命周期 idle → pending → retry-wait → done/failed，每个状态决定"收到错误该做什么"——把 if(retries) 散落逻辑收进状态转移。
- 模板方法：retry 包一层骨架（执行 → 失败 → 策略算延迟 → 等待 → 再执行），算法骨架固定、每步细节（延迟/终止条件）子类注入。
- 识别要点：源码里看到 `retryDelay: attempt => min(2 ** attempt * 100, 30_000) + jitter` 就是策略注入点。

```typescript
type Backoff = (attempt: number) => number;      // 策略接口
const fixed: Backoff = () => 1000;
const exponential: Backoff = a => Math.min(2 ** a * 100, 30_000);
const withJitter = (s: Backoff): Backoff => a => s(a) * (0.5 + Math.random());   // 策略组合

async function retryRequest(fn, { retries = 3, backoff = exponential, onRetry } = {}) {
  for (let attempt = 0; ; attempt++) {
    try { return await fn(); }
    catch (e) {
      if (attempt >= retries || !isRetryable(e)) throw e;   // 终止条件也是策略的一部分
      const delay = backoff(attempt);
      onRetry?.(attempt, delay);
      await new Promise(r => setTimeout(r, delay));         // 模板方法骨架中的"等待步"
    }
  }
}
// 使用：retryRequest(() => api.get('/order'), { backoff: withJitter(exponential), retries: 4 })
```
