---
title: [NODE-679] 数据库迁移（migration）怎么安全执行？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-679：迁移怎么安全执行？
**答**：
- expand-contract 三步（SCN-OPS-331 同源）：加列（可空/带默认——不锁表）→ 回填（分批——避免长事务与大事务锁）→ 切换读写 → 删旧列（观察期后）。
- 与代码发布协同：迁移先于代码（新列先加，代码后发——旧代码忽略新列）；回滚兼容（新代码读新列——回滚后旧代码忽略——向前兼容）。
- 大表变更的约束：避免长事务（锁表风险）——分批 batch + 间隔；大索引 online DDL（MySQL online/PG CONCURRENTLY——不阻塞读写）；变更窗口（低峰）与预估时长。
- 迁移的幂等与审计：迁移版本表（已执行不再跑——幂等）、迁移前后校验（行数/抽样——SCN-OPS-331 对账）、失败中断与回滚脚本（就绪的回滚 DDL）。
- 追问钩子：为什么「回填要分批」而不是一条 UPDATE 全表——全表 UPDATE 是一个大事务：锁全表行（读写全阻塞）+ 主从延迟暴涨 + undo log 巨大（回滚也慢）；分批（每批 1k 行 + sleep）让每批是小事务——线上大表变更的铁律是「控制单事务时长」。

```javascript
// 分批回填
let cursor = 0;
while (true) {
  const rows = await db.query('SELECT id FROM t WHERE new_col IS NULL AND id > $1 LIMIT 1000', [cursor]);
  if (!rows.length) break;
  await db.query('UPDATE t SET new_col = expr(old_col) WHERE id IN ($1)', [rows.ids]);   // 小事务
  cursor = rows.at(-1).id;
  await sleep(100);                                    // 限速
}
// 迁移版本表（幂等）
await db.query('INSERT INTO migrations (name) VALUES ($1)', [name]);   // 唯一约束幂等
```
