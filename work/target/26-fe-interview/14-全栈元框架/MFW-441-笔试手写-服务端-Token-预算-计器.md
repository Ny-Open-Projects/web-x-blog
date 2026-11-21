---
title: [MFW-441] 笔试：手写页面服务端成本预算计（DB ms/出站次数账本）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-441：服务端成本预算计
**需求**：实现 `createSpendMeter(route, { dbMs: 200, calls: 8 } = {})`：1) 包装数据函数：每次 DB 查询/出站调用记账（耗时/次数/目标域——ALS 请求级账本）；2) 预算执行：超 dbMs → 后续查询改走缓存只读副本或拒绝（Error BUDGET——防单请求拖垮集群——与 392 限幅互补：租户级+请求级两维）；3) 账单随响应头/日志出口（x-cost-db-ms, x-cost-calls——可观测可分摊 MFW-461 数据源）；4) 违规路由榜单（P95 超预算 top10——优化队列自动生成）。

```javascript
export function withMeter(budget, fn) {
  return als.run({ dbMs: 0, calls: 0, items: [] }, async (...args) => {
    try {
      const r = await fn({
        db: guardedWrap(dbClient, (ms, target) => spend('db', ms, target)),
        http: guardedWrap(httpAgent, (ms, target) => spend('call', 1, target)),
      })
      return r
    } catch (e) {
      if (e.code === 'BUDGET') { metrics.inc('req.budget_hit', { route })); throw e }
      throw e
    }
  })
  function spend(kind, n, target) {
    const s = als.getStore()
    s[kind === 'db' ? 'dbMs' : 'calls'] += kind === 'db' ? n : 1
    s.items.push({ kind, target, at: now() - t0 })
    if (overBudget()) throw Object.assign(new Error('budget'), { code: 'BUDGET' })   // 熔该请求后续
  }
}
// 响应头：x-cost-db-ms=143; x-cost-calls=6 → 监控按路由聚合出违规榜
```
**评分点**：
- 请求级账本（ALS 隔离——并发请求不串账）
- 双资源计（CPU 型 DB ms / 次数型出站——不同维度不同阈值）
- 预算熔断（超限拒新查询——单请求自保不拖集群；配 392 租户级成二维）
- 账单出口双通道（头+日志——分摊与榜单同源）
