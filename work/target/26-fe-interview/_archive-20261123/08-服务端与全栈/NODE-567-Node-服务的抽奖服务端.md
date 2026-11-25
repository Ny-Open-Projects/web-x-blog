---
title: [NODE-567] Node 服务的抽奖服务（概率/库存/履约）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-567：抽奖服务
**答**:
- 抽奖流程：资格校验（次数/风控——NODE-456）→ 概率抽取（加权随机——概率配置版本化（合规公示 ARC-520））→ 库存检查（奖品库存原子扣——未中"谢谢参与"兜底）→ 履约（发放实物/券/积分——各履约通道幂等）。
- 概率与库存解耦：概率决定"抽中哪类"，库存决定"是否发得出"——库存空自动降级下一档（兜底奖品配置）；概率公平性（PRNG 服务端 crypto 随机 NODE-363——记录随机种子审计可复核）。
- 防刷：次数限制（按用户/设备——幂等扣次数）、抽奖风暴（限流排队 ARC-521）、重复中奖限制（大额奖品限中一次）。
- 履约一致性：中奖记录与发放（发放失败重试 + 补发对账——ARC-382）、中奖凭证（唯一券码——防伪造 ARC-520）。
- 合规：概率公示接口（页面展示概率——监管要求）、抽奖记录保留（审计期）。
```javascript
async function draw(uid, activityId) {
  await quota.take(`draw:${uid}:${activityId}`);                 // 次数扣减幂等
  const prize = weightedRandom(config.probabilities);            // 概率（版本化配置）
  const final = await stock.tryTake(prize) ?? fallbackPrize();   // 库存降级
  const rec = await record({ uid, prize: final, seed });         // 中奖记录（含种子审计）
  await fulfill.dispatch(rec);                                   // 履约分发（幂等）
}
```
