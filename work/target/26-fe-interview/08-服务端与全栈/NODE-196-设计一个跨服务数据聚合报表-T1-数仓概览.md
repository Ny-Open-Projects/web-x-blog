---
title: [NODE-196] 设计一个跨服务数据聚合报表（T+1 数仓概览）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-196：设计一个跨服务数据聚合报表（T+1 数仓概览）？
**答**：
- 定位：报表服务只做**读预聚合结果**的 API，绝不直连业务库跑复杂 SQL——数仓链路负责加工。
- 链路：业务库 binlog → Kafka → Flink/离线任务 → `dw_order_agg` 预聚合宽表（按天/渠道/品类）→ 报表 API 秒出。
- 口径治理：指标口径唯一来源（metric.yaml 定义 GMV/活跃等），大盘与报表共用计算逻辑，禁止各写各的 SQL。
- 性能：T+1 数据可长缓存（`cache-control: max-age=300`）；维度筛选走预聚合表分组，明细下钻走明细表分页。

```javascript
const SAFE_DIMS = { channel: 'channel', category: 'category', city: 'city' }; // 白名单防注入

app.get('/api/report/daily', auth('report:read'), async (ctx) => {
  const date = ctx.query.date ?? yesterday();
  const dim = SAFE_DIMS[ctx.query.dim] ?? 'channel';  // 维度白名单
  const rows = await reportDb.query(
    `SELECT ${dim}, SUM(gmv) AS gmv, COUNT(DISTINCT uid) AS buyers
     FROM dw_order_agg WHERE dt = ? GROUP BY ${dim}`, [date]);
  ctx.set('cache-control', 'public, max-age=300');    // T+1 数据可缓存
  ctx.body = rows;
});
// metric.yaml：gmv = SUM(paid_amount)（唯一口径定义，大盘报表共用）
```
