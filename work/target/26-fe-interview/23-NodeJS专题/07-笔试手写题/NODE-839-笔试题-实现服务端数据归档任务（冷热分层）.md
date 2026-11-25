---
title: [NODE-839] 笔试题——实现数据归档任务（冷热分层 + 断点 + 校验）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-839：手写归档任务

**需求与边界**：
- 需求：数据归档（SCN-FIN-529/682）——① 冷热分层（热表保留 N 月——冷数据迁归档库/对象存储）；② 分批迁移（小事务——SCN-OPS-331）；③ 归档校验（迁移前后行数/抽样——SCN-OPS-331 对账）；④ 归档检索（冷数据可查——延迟查询接口）。
- 边界：① 归档不可变（归档后只读——SCN-FIN-625）；② 归档期间的写入（归档窗口边界——写入绕过）；③ 保留期倒计时（SCN-FIN-625 保留策略）。

**答**：
```javascript
async function archiveTask(table, { olderThan = 90 } = {}) {
  const cutoff = daysAgo(olderThan);
  let cursor = 0, archived = 0;
  while (true) {
    const rows = await db.query(`SELECT * FROM ${table} WHERE ts < $1 AND id > $2 LIMIT 1000`, [cutoff, cursor]);
    if (!rows.length) break;
    await archiveDb.insert(table, rows);               // 写归档库（不可变——SCN-FIN-625）
    await db.query(`DELETE FROM ${table} WHERE id IN ($1)`, [rows.ids]);   // 删热表
    archived += rows.length; cursor = rows.at(-1).id;
    await sleep(100);                                  // 限速（SCN-OPS-331）
  }
  const verify = await archiveDb.count(table) === archived;   // 行数对账（SCN-OPS-331）
  if (!verify) alert({ type: 'ARCHIVE_VERIFY_FAIL', table });
  markArchived(table, cutoff, archived);               // 保留期倒计时起点（SCN-FIN-625）
  return { archived, verify };
}
// 冷数据检索（延迟查询——SCN-FIN-625 检索）
app.get('/archive/search', auditRole(), async (req, res) => res.json(await archiveDb.search(req.query)));
```

**评分点**:
- 分批迁移限速（SCN-OPS-331 小事务）。
- 行数对账（迁移校验——SCN-OPS-331）。
- 归档不可变 + 保留期（SCN-FIN-625）。
- 冷数据检索接口（归档可查）。
