---
title: [NODE-564] Node 服务的会员服务（等级/权益/成长值）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-564：会员服务
**答**:
- 模型：会员等级（成长值累计 → 等级——升级/降级规则版本化）、权益（等级权益矩阵 ARC-627：折扣/免邮/次数权益）、权益实例（次数型权益的领取/使用记录）。
- 成长值链路：行为加分（消费/活跃——事件驱动加分幂等 NODE-488）、等级计算（快照式：成长值变更 → 重算等级——升级通知）、降级保护（规则：年末统一降级 vs 即时——产品规则显式）。
- 权益核销：次数权益扣减（条件更新——防超用）、权益与订单联动（会员价——价格服务引用会员身份 NODE-558）、跨系统权益（外部合作权益——权益码核销）。
- 一致性：权益使用幂等（权益实例唯一使用）、会员身份缓存（请求级快照——变更失效广播 NODE-507）。
- 观测：等级分布/权益使用率/升级转化（会员业务指标）、成长值对账（加分流水累计 vs 等级快照）。
```javascript
// 成长值与升级
async function addGrowth(uid, points, src) {
  await db.tx(t => {                                             // 流水幂等
    await t.query(`insert into growth_flow(uid, points, src, idem) values(...) on conflict do nothing`, ...);
    const total = await t.query(`update growth set value = value + $1 where uid=$2 returning value`, ...);
    const lvl = levelOf(total.value);                            // 规则版本化
    if (lvl !== await currentLevel(uid)) await upgrade(uid, lvl);// 升级通知/权益刷新
  });
}
```
