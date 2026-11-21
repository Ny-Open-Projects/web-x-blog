---
title: [NODE-040] 如何在 Node 中正确处理数据库事务？以转账为例？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-040：如何在 Node 中正确处理数据库事务？以转账为例？
**答**：
- mysql2 事务模板：`getConnection` → `beginTransaction` → 两条 UPDATE → `commit`，任一步失败 `rollback`。**必须用同一个 connection**（连接池下 pool.query 不保证同连接）。
- 高频细节：① 隔离级别（默认 REPEATABLE READ，余额扣减可用 `UPDATE ... SET balance = balance - x WHERE id = ? AND balance >= x` 的**条件更新 + affectedRows 判断**，天然防超卖）；② rollback 放 finally 保证连接释放（否则池被耗尽）；③ 跨服务事务用消息表/Saga，不用 2PC。
- Node 侧的坑：事务里不要 await 外部 HTTP 调用（长事务持锁拖垮 DB）。

```javascript
const mysql = require('mysql2/promise');

async function transfer(fromId, toId, amount) {
  const conn = await pool.getConnection(); // 事务必须独占一个连接
  try {
    await conn.beginTransaction();

    // 条件更新防超扣：余额不足时 affectedRows = 0
    const [deduct] = await conn.execute(
      'UPDATE accounts SET balance = balance - ? WHERE id = ? AND balance >= ?',
      [amount, fromId, amount],
    );
    if (deduct.affectedRows === 0) {
      throw Object.assign(new Error('余额不足'), { status: 400, code: 'INSUFFICIENT_BALANCE' });
    }
    await conn.execute('UPDATE accounts SET balance = balance + ? WHERE id = ?', [amount, toId]);

    // 流水表（对账依据）
    await conn.execute(
      'INSERT INTO transfer_log (from_id, to_id, amount, created_at) VALUES (?, ?, ?, NOW())',
      [fromId, toId, amount],
    );

    await conn.commit();
    return { ok: true };
  } catch (err) {
    await conn.rollback();      // 任一步失败整体回滚
    throw err;
  } finally {
    conn.release();             // 关键：无论成败归还连接
  }
}
```
