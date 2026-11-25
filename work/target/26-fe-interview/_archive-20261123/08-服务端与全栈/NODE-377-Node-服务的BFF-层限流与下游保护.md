---
title: [NODE-377] Node 服务的 BFF 层限流与下游保护如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-377：BFF 层限流与下游保护
**答**:
- 双向限流：对进（用户级限流，NODE-360）+ 对出（BFF 对下游的调用限流——一次页面请求放大成 N 个下游调用，下游按自己的容量定配额，BFF 超额时熔断排队而不是打挂下游）。
- 放大系数治理：BFF 聚合一次页面 → 下游 5 个接口 × 用户并发，放大系数 = 下游 QPS / BFF QPS；监控这个系数（聚合变更时突增告警——新页面偷偷加了重接口）。
- 下游保护三件套：调用方配额（下游给 BFF 分配 QPS 配额，超了 429）、熔断器（下游错误率超阈值 BFF 熔断走降级数据，ARC-447 分级依赖）、批量接口优先（N 次单查 → 1 次批量，降低放大）。
- 依赖声明：BFF 对每个下游声明"关键/非关键 + 预算超时 + 降级策略"（配置化，改超时不发版）。
- 传播保护：请求携带超时预算向下传递（上游剩 200ms，下游调用只给 150ms，避免总超时后下游还在白白计算——deadline propagation）。
```javascript
// 带预算的下游调用
async function callWithDeadline(url, budgetMs) {
  const remaining = ctx.budget.remaining();                     // 剩余预算
  const t = Math.min(budgetMs, remaining - 50);                 // 留 50ms 给响应
  if (t <= 0) return FALLBACK;                                  // 预算耗尽直接降级
  return fetch(url, { signal: AbortSignal.timeout(t) });
}
```
