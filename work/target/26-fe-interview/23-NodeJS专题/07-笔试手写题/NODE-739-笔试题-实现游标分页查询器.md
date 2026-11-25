---
title: [NODE-739] 笔试题——实现游标分页查询器（双键游标 + 不透明编码）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-739：手写游标分页

**需求与边界**：
- 需求：游标分页（SCN-NODE-696）——① ts+id 双键游标（同秒不丢不重——SCN-FIN-503）；② 不透明游标（base64+签名——客户端不可构造）；③ 协议统一（items/nextCursor/hasMore）；④ offset 混合模式（管理后台跳页——SCN-NODE-696 混合策略）。
- 边界：① 游标解码校验（签名失败 400——防构造越权）；② 排序方向参数化（asc/desc——游标方向随排序）；③ 批量查询的 IN 预取（关联数据——SCN-NODE-662 dataloader）。

**答**：
```javascript
const sign = (s) => hmac(SECRET, s).slice(0, 16);
const encodeCursor = (row) => Buffer.from(
  JSON.stringify({ t: +row.ts, i: row.id, s: sign(`${row.ts}|${row.id}`) })).toString('base64');
function decodeCursor(cur) {
  const { t, i, s } = JSON.parse(Buffer.from(cur, 'base64'));
  if (sign(`${t}|${i}`) !== s) throw new BadCursor();   // 签名校验（防构造——SCN-NODE-696）
  return { ts: t, id: i };
}
async function list(cursor, { limit = 20, dir = 'desc', offset = null } = {}) {
  if (cursor) {                                        // 游标模式
    const c = decodeCursor(cursor);
    const cmp = dir === 'desc' ? '<' : '>';
    const rows = await db.query(`SELECT * FROM t WHERE (ts, id) ${cmp} ($1, $2)
      ORDER BY ts ${dir.toUpperCase()}, id ${dir.toUpperCase()} LIMIT $3`, [c.ts, c.id, limit + 1]);
    return { items: rows.slice(0, limit), hasMore: rows.length > limit,
      nextCursor: rows.length > limit ? encodeCursor(rows[limit - 1]) : null };
  }
  const rows = await db.query('SELECT * FROM t ORDER BY ts DESC LIMIT $1 OFFSET $2',
    [limit, offset ?? 0]);                             // offset 模式（管理后台跳页）
  return { items: rows, hasMore: rows.length === limit };
}
```

**评分点**:
- 双键游标（ts+id——同秒不丢不重）+ 方向参数化。
- 不透明游标签名校验（客户端不可构造——越权防御）。
- 游标/offset 混合（按交互形态——SCN-NODE-696）。
- 协议统一（items/nextCursor/hasMore）。
