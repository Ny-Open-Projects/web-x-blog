---
title: [NODE-669] 下游故障隔离（熔断器 hystrix 模式）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-669：熔断器怎么做？
**答**：
- 三态机：closed（正常——统计失败率）→ open（失败率超阈——直接快速失败不再调用）→ half-open（试探——少量请求探测恢复）；熔断是「快速失败保护上游」+「给下游恢复窗口」。
- 关键参数：滑动窗口统计（失败率/慢调用率——慢也算失败）、最小请求数（样本少不熔断）、半开探测并发（1~3 个——恢复验证不风暴）。
- 熔断的降级配合：open 状态走降级值（缓存/默认/裁剪——SCN-NODE-644 部分成功），熔断无降级就是纯失败（更糟）。
- 隔离舱：每个下游独立熔断器（互不影响——舱壁模式）+ 并发信号量隔离（某下游占用过多并发时隔离）。
- 追问钩子：为什么熔断器必须配「降级值」才有意义——open 状态的调用直接失败，若上游没有降级处理，熔断只是把「慢失败」变成「快失败」（用户体验没改善）；熔断器 + 降级值 = 「下游挂了服务还能用」（核心链路保活）——熔断是开关，降级是开关后的电路，缺一不可。

```javascript
const breaker = new CircuitBreaker(callDownstream, {
  errorThresholdPercentage: 50, volumeThreshold: 20,   // 最小样本 20
  allowWarmUp: 25_000,
});
breaker.fallback(() => cache.get(lastGoodResult) ?? DEFAULT_VALUE);   // 熔断降级
// half-open 探测
breaker.on('halfOpen', () => probeWithLimitedConcurrency(2));
```
