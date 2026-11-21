---
title: [NODE-052] BFF 的容错设计：熔断、降级、隔离舱如何实现？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-052：BFF 的容错设计：熔断、降级、隔离舱如何实现？
**答**：
- **熔断**（circuit breaker）：下游错误率/慢调用超阈值后直接"跳闸"快速失败，不再打超时请求，半开状态探测恢复——保护自己，也保护下游喘息。用 `opossum` 库。
- **降级**：熔断/超时后返回兜底数据（缓存旧值、默认值、空结构），核心链路可用性优先于完整性。
- **隔离舱**（bulkhead）：把不同下游的并发额度隔开（每依赖独立并发上限/超时），一个下游被打挂不拖垮其他依赖。用 `p-limit` 每依赖一个 limit。
- 组合拳：限流（入口）→ 隔离（下游并发）→ 超时（每次调用）→ 熔断（连续失败）→ 降级（兜底响应）→ 告警（观测闭环）。

```javascript
const CircuitBreaker = require('opossum');
const pLimit = require('p-limit');

// 每个下游独立配置：隔离舱（并发上限）+ 熔断器
function makeDependency(name, { concurrency, timeout, errorThreshold, resetTimeout, loader, fallback }) {
  const limit = pLimit(concurrency);                       // 隔离舱：该下游最多 N 个并发
  const breaker = new CircuitBreaker(loader, {
    timeout,                                              // 单次调用超时
    errorThresholdPercentage: errorThreshold,             // 错误率 50% 跳闸
    resetTimeout,                                         // 半开恢复探测间隔
    volumeThreshold: 10,                                  // 至少 10 次调用才统计错误率
  });
  breaker.fallback(() => fallback());                     // 熔断/超时后的降级值
  breaker.on('open', () => console.warn(JSON.stringify({ event: 'breaker_open', dep: name })));
  return async () => limit(() => breaker.fire());         // 限并发 + 熔断 双层包裹
}

const deps = {
  reco:   makeDependency('reco', { concurrency: 20, timeout: 300, errorThreshold: 50,
            resetTimeout: 10000, loader: () => fetchReco(), fallback: () => [] }),
  stock:  makeDependency('stock', { concurrency: 10, timeout: 500, errorThreshold: 60,
            resetTimeout: 5000, loader: () => fetchStock(), fallback: () => ({ count: 0, unknown: true }) }),
};

// 使用：任何下游故障都不阻塞整页
router.get('/page/detail/:id', async (ctx) => {
  const [reco, stock] = await Promise.all([deps.reco(), deps.stock()]);
  ctx.body = { reco, stock };   // reco 失败给 []，stock 失败给 unknown 标记
});
```

---

## 八、SSR 服务端
