---
title: [NODE-401] Node 服务的计费与用量统计（计量计费链路）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-401：Node 服务的计费与用量统计
**答**:
- 链路：计量（调用/流量/存储事件打点）→ 聚合（按周期/维度预聚合）→ 计费（价格引擎：套餐/阶梯/超量）→ 出账与对账（与内部记录互证）。
- 计量采集：埋点事件到 MQ（不阻塞主链路）、幂等（计量事件 ID 去重——重复计量就是多收钱）、粒度设计（原始明细保留 + 小时/天预聚合表）。
- 计费正确性：金额计算整数分（ARC-482）、价格变更只影响新周期（历史账单锁定）、争议以"明细可追溯"为原则（每笔费用能回溯到计量事件）。
- 防套利：免费额度防刷（配额 + 风控）、计量口径变更走公告与版本（NODE-359 思想）。
- 对账：计量总量 vs 业务总量（API 调用数 vs 网关日志数）偏差告警（ARC-382 思想）；出账前试算校验（同比波动异常告警）。
```javascript
// 计量事件（幂等）+ 预聚合
consumer.on('usage', async (e) => {
  const ok = await db.query(`insert into usage_event(id, app_key, metric, qty, ts)
    values($1,$2,$3,$4,$5) on conflict (id) do nothing`, [e.id, e.appKey, e.metric, e.qty, e.ts]);
  if (ok.rowCount) await redis.hincrby(`usage:h:${hour(e.ts)}`, `${e.appKey}:${e.metric}`, e.qty);
});
// 出账：select sum(qty) from usage_event where app_key=$1 and ts between $2 and $3 → 价格引擎
```
