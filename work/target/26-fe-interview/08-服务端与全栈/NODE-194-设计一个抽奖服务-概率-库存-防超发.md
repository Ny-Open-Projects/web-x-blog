---
title: [NODE-194] 设计一个抽奖服务（概率/库存/防超发）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-194：设计一个抽奖服务（概率/库存/防超发）？
**答**：
- 抽奖三关：**资格校验**（一人一次/消耗积分）→ **概率抽取**（权重随机，种子服务端持有防篡改）→ **库存防超发**（Lua 原子扣，扣不到降级谢谢参与）。
- 概率与库存解耦：先按权重抽中"iPhone"，库存没了降级"优惠券"——大奖概率真实、库存真实。
- 防作弊：概率逻辑不出服务端、请求频率限制、一人一次（Set 记录）、大奖异步发奖 + 人工复核。
- 审计：每次抽奖落流水（uid/种子/结果/时间），可回放验证公平性。

```javascript
const PRIZES = [
  { id: 'iphone', weight: 1 },
  { id: 'coupon50', weight: 30 },
  { id: 'thanks', weight: 969 },
];
function drawOnce() {                                  // 权重随机：随机数落区间
  const total = PRIZES.reduce((s, p) => s + p.weight, 0);
  let r = Math.random() * total;
  for (const p of PRIZES) { if ((r -= p.weight) < 0) return p.id; }
  return 'thanks';
}

app.post('/lucky/draw', limiter({ per: '1s' }), async (ctx) => {
  const uid = ctx.state.uid;
  if (!(await redis.set(`lucky:once:${ROUND}:${uid}`, 1, 'PX', 86_400_000, 'NX'))) {
    ctx.throw(409, '已参与');                          // 一人一次
  }
  const picked = drawOnce();
  const left = await redis.eval(DECR_LUA, 1, `lucky:stock:${picked}`); // 原子扣库存
  const finalId = left < 0 ? 'thanks' : picked;        // 售罄降级
  await db.luckyRecord.create({ data: { uid, prizeId: finalId, roundId: ROUND, ts: Date.now() } });
  if (finalId === 'iphone') await auditQueue.add('review', { uid }); // 大奖人工复核
  ctx.body = { prizeId: finalId };
});
```
