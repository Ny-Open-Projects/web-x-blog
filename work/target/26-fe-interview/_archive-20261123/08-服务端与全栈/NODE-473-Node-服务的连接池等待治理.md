---
title: [NODE-473] Node 服务的连接池等待治理（排队/熔断/扩池决策）如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-473：连接池等待治理
**答**:
- 池等待是容量瓶颈最常见形态：池小 → 请求排队（延迟涨）；池大 → DB 连接耗尽（NODE-332）。治理核心：等待可观测 + 等待有上限 + 扩池有依据。
- 可观测：等待队列长度/等待时长 P95（进依赖画像 NODE-467）、等待超时数（acquire timeout 打满）——"池在等"要先于"用户在等"被发现。
- 治理手段：acquire timeout（快速失败优于无限排队——失败触发降级而不是挂着）、单飞合并（NODE-378：同 key 请求合并减少池占用）、查询分级（核心查询专用小池——隔离慢查询饿死 ARC-418）、慢查询治理联动（等待暴涨多数是慢查询引起——归因到具体查询 NODE-416）。
- 扩池决策树：等待高 + DB 连接余量足 → 扩池；等待高 + DB 连接满 → 加 PgBouncer/分库（NODE-386）/降查询量——扩池不是万能药。
- 容量联动：池参数进容量模型（实例数 × 池 max ≤ DB 上限，HPA 扩容时自动检查 NODE-375/405）。
```javascript
// 池等待监控与快速失败
pool.on('acquire', () => poolWait.start());
pool.on('connect', () => poolWait.end());
setInterval(() => {
  const w = poolWait.p95();
  metrics.gauge('pool.wait.p95', w);
  if (w > 200 && dbConn.headroom() > 0.3) suggestResize(pool.max + 5);  // 有余量 → 建议扩
  else if (w > 200) suggestPgBouncer();                                 // 没余量 → 另谋
}, 30e3);
```
