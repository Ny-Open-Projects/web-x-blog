---
title: [NODE-750] 笔试题——实现积分 FEFO 扣减引擎（批次 + 幂等 + 冲正）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-750：手写积分 FEFO

**需求与边界**：
- 需求：积分引擎（SCN-NODE-684）——① FEFO 扣减（先过期先扣——多批次事务）；② 幂等（idemKey 唯一——SCN-NODE-655）；③ 冲正（退款定位原批次——冲正流水引用原流水）；④ 过期任务（批次过期清理——幂等任务 SCN-NODE-667）。
- 边界：① 多批次不足整体回滚（部分扣失败——事务原子）；② 流水 append-only（余额可推导——审计）；③ 并发扣减（行锁——条件更新余额）。

**答**：
```javascript
async function deduct(uid, amount, idemKey) {
  try {
    await db.insert('point_ledger', { idemKey, uid, type: 'DEDUCT', amount });   // 幂等流水先行（唯一约束）
  } catch (e) { if (e.code === '23505') return { status: 'DUPLICATE' }; throw e; }
  await db.transaction(async (tx) => {
    const batches = await tx.query(`SELECT id, remain FROM point_batches
      WHERE user_id = $1 AND remain > 0 AND expire_at > now()
      ORDER BY expire_at FOR UPDATE`, [uid]);          // FEFO + FOR UPDATE（行锁）
    let need = amount;
    for (const b of batches) {
      const use = Math.min(b.remain, need);
      await tx.query('UPDATE point_batches SET remain = remain - $1 WHERE id = $2 AND remain >= $1',
        [use, b.id]);                                  // 条件更新（并发防御）
      await tx.insert('point_ledger', { uid, type: 'DEDUCT_DETAIL', batchId: b.id, delta: -use, refKey: idemKey });
      need -= use;
      if (need === 0) break;
    }
    if (need > 0) throw new Insufficient(need);        // 整体回滚（事务原子）
  });
  return { status: 'OK' };
}
// 冲正：引用原流水（定位原批次）
async function refund(idemKey) {
  const orig = await db.query('SELECT * FROM point_ledger WHERE ref_key = $1 AND type = $2',
    [idemKey, 'DEDUCT_DETAIL']);                       // 定位原批次流水
  orig.forEach(d => insertLedger({ batchId: d.batchId, delta: -d.delta, type: 'REFUND', refKey: idemKey }));   // 原批次冲正
}
```

**评分点**:
- FEFO 排序 + FOR UPDATE 行锁（并发扣减原子——SCN-NODE-684）。
- 幂等流水先行（唯一约束——SCN-NODE-655）。
- 条件更新（remain >= use——并发防御双保险）。
- 冲正定位原批次（流水引用链——退款精确回原批次）。
