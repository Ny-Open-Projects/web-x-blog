---
title: [NODE-766] 笔试题——实现迁移版本管理与回滚（幂等 + 分批 + 回滚脚本）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-766：手写迁移管理

**需求与边界**：
- 需求：迁移管理器（SCN-NODE-679）——① 版本表幂等（已执行不重跑）；② 大表变更分批（batch + sleep——SCN-OPS-331）；③ 回滚脚本就绪（每迁移配套 down——失败回滚）；④ 校验（行数/抽样——迁移前后对账）。
- 边界：① online DDL 语义（PG CONCURRENTLY/MySQL online——不锁表）；② 迁移锁（多实例不并发迁移——SCN-NODE-652 锁）；③ 中断恢复（batch 进度断点）。

**答**：
```javascript
async function migrate(migration, { batch = 1000 } = {}) {
  await withLock(`migration:${migration.name}`, async () => {   // 迁移锁（SCN-NODE-652）
    const done = await db.query('SELECT 1 FROM migrations WHERE name=$1', [migration.name]);
    if (done.rowCount) return { skipped: true };       // 幂等（SCN-NODE-655）
    await migration.up(db);                            // DDL（online）
    let cursor = migration.backfillStart ?? 0;         // 分批回填（断点）
    while (true) {
      const rows = await db.query(migration.backfillQuery, [cursor, batch]);
      if (!rows.length) break;
      cursor = rows.at(-1).id;
      await saveProgress(migration.name, cursor);      // 断点
      await sleep(100);                                // 限速（小事务）
    }
    const ok = await migration.verify(db);             // 校验（行数/抽样——SCN-OPS-331）
    if (!ok) throw new Error('VERIFY_FAIL');
    await db.query('INSERT INTO migrations (name) VALUES ($1)', [migration.name]);   // 版本表
    return { done: true };
  });
}
// 回滚脚本就绪（迁移定义强制带 down）
migration.down = async (db) => db.query('ALTER TABLE t DROP COLUMN new_col');
```

**评分点**:
- 迁移锁 + 版本表幂等（多实例/重跑防御——SCN-NODE-652/655）。
- 分批回填断点（大表变更铁律——SCN-OPS-331 小事务）。
- verify 校验 + 回滚脚本强制（down 就绪——失败回滚）。
- online DDL 语义（CONCURRENTLY——不锁表）。
