---
title: [NODE-684] 积分/营销账户系统怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-684：积分账户怎么做？
**答**：
- 账户模型：余额 + 流水（append-only——流水不可改，余额由流水推导——审计与可回放，SCN-FIN-503 流水组件同源）；流水幂等键防重复发放。
- 过期机制：积分有效期（批次化——每笔发放带过期时间，过期任务批次清理；FEFO 先过期先扣——扣减时按批次顺序）。
- 并发扣减：原子扣减（条件更新 WHERE balance >= n——SCN-FIN-656 同构）；分批次扣减的事务（多批次扣减在一个事务——部分扣失败回滚）。
- 防刷：发放规则的服务端校验（规则引擎——SCN-OPS-616 条件路由）、发放限流、异常模式监控（发放突增告警）。
- 追问钩子：为什么积分扣减要「FEFO 按批次」而不能只记总额——只记总额时过期无法精确执行（过期哪部分？）；批次化（每笔发放独立批次带过期日）让过期清理精确、退款冲正可定位原批次——账本设计的「批次粒度」决定了过期/冲正等复杂业务的可实现性。

```javascript
// FEFO 扣减（先过期先扣）
await db.transaction(async (tx) => {
  const batches = await tx.query(`SELECT * FROM point_batches
    WHERE user_id=$1 AND expire_at > now() AND remain > 0 ORDER BY expire_at`, [uid]);
  let need = amount;
  for (const b of batches) {
    const use = Math.min(b.remain, need);
    await tx.query('UPDATE point_batches SET remain = remain - $1 WHERE id = $2', [use, b.id]);
    await tx.insert('point_ledger', { batchId: b.id, delta: -use, idemKey });   // 流水幂等
    need -= use; if (need === 0) break;
  }
  if (need > 0) throw new Error('INSUFFICIENT');        // 整体回滚
});
```
