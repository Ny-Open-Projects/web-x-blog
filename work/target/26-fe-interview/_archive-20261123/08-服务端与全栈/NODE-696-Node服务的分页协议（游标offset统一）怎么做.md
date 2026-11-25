---
title: [NODE-696] 分页协议（游标/offset 统一）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-696：分页协议怎么做？
**答**：
- 游标分页：cursor = 末条排序键（ts+id 双游标——同秒多条不丢，SCN-FIN-503 双游标）；无 skip 成本（深分页 offset 的性能悬崖——offset 10 万 = 扫描 10 万行）。
- 协议统一：分页响应结构统一（items + nextCursor + hasMore——SCN-NODE-617 分页协议统一）；游标不透明（opaque cursor——编码+签名，客户端不可构造——防止跳页越权）。
- 混合策略：管理后台需要跳页（offset——页码导航）vs 信息流用游标（无限滚动）——按交互形态选，协议层统一封装。
- 一致性：游标分页的插入容忍（新数据插入不打乱当前页——offset 会重复/漏数据，SCN-FIN-501 分页一致性）。
- 追问钩子：为什么游标要「ts+id 双键」而不是单键——单 ts 游标时同一秒多条记录：下一页从 ts>cursor 开始会丢同秒记录、ts>=cursor 会重复；双键（ts,id）做字典序游标——排序键唯一化是游标分页正确性的前提，复合键是通用解。

```javascript
// 双键游标
async function page(after) {                           // after: { ts, id }
  const rows = await db.query(`SELECT * FROM t
    WHERE (ts, id) < ($1, $2) ORDER BY ts DESC, id DESC LIMIT 21`, [after.ts, after.id]);
  const hasMore = rows.length > 20;
  const next = hasMore ? encodeCursor(rows[19]) : null;   // 不透明游标
  return { items: rows.slice(0, 20), nextCursor: next, hasMore };
}
const encodeCursor = (row) => sign(base64(`${row.ts}|${row.id}`));   // 签名防构造
```
