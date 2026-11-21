---
title: [NODE-551] Node 服务的钱包账户（余额/冻结/流水）服务端如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-551：钱包账户服务端
**答**:
- 账户模型：余额（可用/冻结）+ 流水（每笔变动：来源/去向/关联单号——ARC-460 涉账铁律）+ 复式记账（平台总账 = 用户余额和——总账对账基础）。
- 变动事务：条件更新（balance >= amount 才扣——NODE-412）+ 流水同事务（原子）；冻结两阶段（下单冻结 → 成功扣冻结 / 失败解冻——冻结流水独立记录）。
- 并发安全：同账户串行化（账户 id 分区 MQ 或 select for update——热点账户拆影子账户 NODE-520）、幂等（幂等键唯一索引 NODE-476）。
- 对账体系：日终对账（流水累计 vs 余额快照 + 总账核对——ARC-382/538 分级告警）、外部对账（支付渠道对账单）。
- 安全：账户操作审计哈希链（NODE-442）、提现/转账二次认证（NODE-455）、限额体系（单笔/日累计）。
```javascript
// 冻结两阶段
await db.tx(async (t) => {
  const r = await t.query(`update wallet set frozen = frozen + $1, balance = balance - $1
    where uid = $2 and balance >= $1`, [amt, uid]);              // 冻结：条件更新
  if (r.rowCount === 0) throw new InsufficientBalance();
  await t.query(`insert into wallet_flow(uid, type, delta, ref, idem_key)
    values($1,'freeze',$2,$3,$4) on conflict (idem_key) do nothing`, [uid, -amt, orderId, idemKey]);
});
// 解冻：freeze -= amt；扣减：balance 已扣（冻结即扣可用）——失败解冻回滚
```
