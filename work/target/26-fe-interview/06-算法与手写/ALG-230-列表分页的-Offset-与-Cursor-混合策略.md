---
title: [ALG-230] 评论区分页：前 3 页用 offset（可跳页）、深层用 cursor（稳定不重）的混合分页策略？
date: 2026-11-19
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---
## ALG-230：评论区分页：前 3 页用 offset（可跳页）、深层用 cursor（稳定不重）的混合分页策略？
**答**：评论区：用户常看前几页（跳页体验好，offset 分页），数据可能新增导致 offset 漂移重/漏；深层翻页（第 50 页+）offset 性能差（数据库 skip 大）。混合策略：浅层 offset + 深层 cursor（keyset）。

**思路**：浅层（page ≤ 3）`LIMIT n OFFSET m`；越过阈值切 cursor（以当页最后一条的 id/ts 为游标 `WHERE ts < cursor ORDER BY ts DESC LIMIT n`）；切点把 cursor 传给前端继续。

```javascript
// 服务端伪码：混合分页
function listComments({ page, cursor, limit = 20 }) {
  if (!cursor && page <= 3) {
    const rows = db.query(`SELECT * FROM comments ORDER BY ts DESC LIMIT ? OFFSET ?`, [limit, (page - 1) * limit]);
    return { rows, nextPage: page + 1,
             cursor: page === 3 ? rows.at(-1).ts : null };   // 第 3 页末尾产出 cursor（切点）
  }
  const rows = db.query(
    `SELECT * FROM comments WHERE ts < ? ORDER BY ts DESC LIMIT ?`, [cursor, limit]);  // keyset：稳定不重
  return { rows, cursor: rows.at(-1)?.ts ?? null };
}
// 对比：
// offset：跳页友好；数据新增时第 2 页可能出现第 1 页已见的条目（漂移）；深层 skip O(n) 慢
// cursor：无漂移、O(logn) 索引直取；不能跳页
// 混合：浅层体验（跳页）+ 深层稳定与性能 —— 切点在第 3 页末尾
// 边界：cursor 语义用 ts+id 双键（同 ts 多条不重不漏）：WHERE (ts, id) < (?, ?)
```

**评分点**：
- 两种分页的本质差异（漂移 vs 跳页）说清——本题核心。
- 混合策略切点设计（浅层末页产出 cursor）。
- cursor 用 (ts, id) 复合键防同时间戳重/漏——细节加分。
- 性能差异：深层 offset 的 skip O(n) vs keyset 索引直取。
