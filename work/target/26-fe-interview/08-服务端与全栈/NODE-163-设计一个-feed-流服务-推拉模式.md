---
title: [NODE-163] 设计一个 feed 流服务（推拉模式）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-163：设计一个 feed 流服务（推拉模式）？
**答**：
- 推模式（写扩散）：发博时写进每个粉丝收件箱（Redis ZSET），读时 O(1)——普通用户适用；大 V 百万粉丝写扩散爆炸。
- 拉模式（读扩散）：读时实时归并关注者最新内容——大 V 适用；粉丝读延迟高。
- **推拉结合**：普通用户发博推，大 V 发博只标记；读时 = 收件箱 + 实时拉大 V 最新 → 归并去重排序。
- 工程细节：收件箱只留最近 3000 条（ZSET REMRANGEBYRANK 裁剪），冷数据回源 DB 分页；去重按 post.id 集合。

```javascript
async function onPost(post) {
  const followers = await db.follow.count({ where: { followeeId: post.authorId } });
  if (followers > 10_000) return;                 // 大 V 不推，读时拉
  const fans = await db.follow.findMany({
    where: { followeeId: post.authorId }, select: { followerId: true },
  });
  await redis.pipeline(                           // 批量写粉丝收件箱
    fans.map((f) => ['zadd', `feed:${f.followerId}`, post.score, post.id])
  ).exec();
}

async function getFeed(userId, cursor = 0) {
  const bigVIds = await followedBigVIds(userId);
  const [inbox, bigV] = await Promise.all([
    redis.zrevrange(`feed:${userId}`, cursor, cursor + 20, 'WITHSCORES'),
    fetchBigVLatest(bigVIds, 20),                 // 实时拉大 V
  ]);
  const merged = [...inbox, ...bigV]
    .sort((a, b) => b.score - a.score);           // 归并排序
  const seen = new Set();
  return merged.filter((p) => !seen.has(p.id) && seen.add(p.id)).slice(0, 20); // 去重
}
```
