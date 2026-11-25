---
title: [NODE-837] 笔试题——实现数据乐观锁（version 条件更新）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-837：手写乐观锁

**需求与边界**：
- 需求：乐观锁（SCN-NODE-655 延伸）——① version 条件更新（UPDATE ... WHERE version=?——SCN-FIN-508）；② 冲突处理（version 冲突 → 409 + 最新版本返回——客户端重试语义）；③ version 单调递增（version+1——SCN-FIN-548）；④ 批量更新的乐观锁（逐条条件更新——SCN-FIN-611 部分成功）。
- 边界：① 冲突响应带最新数据（客户端 diff 后决定重试——SCN-OPS-218 冲突提示）；② 高冲突场景的退避（抖动——SCN-NODE-691）；③ 乐观锁与悲观锁的选择（冲突率——低冲突乐观/高冲突悲观，SCN-NODE-652）。

**答**：
```javascript
async function updateWithVersion(id, patch, clientVersion) {
  const sets = Object.entries(patch).map(([k], i) => `${k} = $${i + 3}`).join(',');
  const r = await db.query(
    `UPDATE t SET ${sets}, version = version + 1 WHERE id = $1 AND version = $2 RETURNING version`,
    [id, clientVersion, ...Object.values(patch)]);     // 条件更新（SCN-FIN-508）
  if (r.rowCount === 0) {                              // 冲突：409 + 最新数据
    const latest = await db.query('SELECT * FROM t WHERE id = $1', [id]);
    return res.status(409).json({ code: 'VERSION_CONFLICT',
      latest: latest[0], retryable: true });           // 客户端 diff 决定（SCN-OPS-218）
  }
  return { version: r[0].version };
}
// 批量：逐条条件更新 + 部分成功（SCN-FIN-611）
for (const item of items) results.push(await updateWithVersion(item.id, item.patch, item.version).catch(e => e));
```

**评分点**:
- 条件更新（version=?——SCN-FIN-508）。
- 冲突 409 带最新数据（客户端可行动——SCN-OPS-218）。
- version 单调递增（SCN-FIN-548）。
- 批量部分成功（SCN-FIN-611）。
