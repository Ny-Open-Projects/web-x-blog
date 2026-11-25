---
title: [NODE-192] 设计一个排行榜服务（ZSET/并列名次/分页）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-192：设计一个排行榜服务（ZSET/并列名次/分页）？
**答**：
- 实时榜 Redis ZSET：`ZINCRBY` 更新积分、`ZREVRANGE WITHSCORES` 取榜、`ZREVRANK` 取个人名次（O(logN)）。
- 并列名次：ZSET 同分按成员字典序，业务要求"同分同名次"需应用层归并（分数变化才推进名次）。
- 亿级成员：单 key ZSET 撑不住 → **分桶榜单**（今日/本周/总分各一个 key + 时间片轮转）+ 只维护 TopN。
- 榜单重置：新周期建新榜 + 原子改名切换 + 旧榜归档；读走缓存 1s。

```javascript
async function topN(board, page = 1, size = 20) {
  const start = (page - 1) * size;
  const rows = await redis.zrevrange(`board:${board}`, start, start + size - 1, 'WITHSCORES');
  let rank = start, prev = null;
  return rows.reduce((acc, [member, score], i) => {
    if (score !== prev) rank = start + i + 1;         // 同分并列同名次
    prev = score;
    return [...acc, { rank, member, score: Number(score) }];
  }, []);
}

async function addScore(board, member, delta) {
  await redis.zincrby(`board:${board}`, delta, member);
  return redis.zrevrank(`board:${board}`, member);    // 我的实时名次
}

// 周期轮转：0 点执行
// RENAME board:daily board:daily:20261107 然后 ZADD 建新榜；旧榜 EXPIRE 7d 归档
```
