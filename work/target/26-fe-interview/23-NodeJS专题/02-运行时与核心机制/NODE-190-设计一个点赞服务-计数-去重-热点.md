---
title: [NODE-190] 设计一个点赞服务（计数/去重/热点）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-190：设计一个点赞服务（计数/去重/热点）？
**答**：
- 写路径全 Redis：`SADD` 判重（返回 0 = 已点过，天然幂等）+ `HINCRBY` 计数；DB 落库异步化，秒级最终一致。
- 落库防回退：定时任务把 Redis 计数合并进 DB 时用 `WHERE count < redis值` 方向保护。
- 超大去重（百万级点赞）：Set 内存爆炸 → BloomFilter 判重 + 纯计数器，接受极小误判换取内存。
- 取消点赞：`SREM` + 计数 -1；计数展示允许±1 误差时可直接读 Redis。

```javascript
async function like(uid, targetType, targetId) {
  const dedupKey = `liked:${targetType}:${targetId}`;
  const first = await redis.sadd(dedupKey, uid);      // 返回 1 = 新增
  if (first) await redis.pexpire(dedupKey, 7 * 86_400_000);
  if (first) await redis.hincrby('likes:count', `${targetType}:${targetId}`, 1);
  return { first, count: Number(await redis.hget('likes:count', `${targetType}:${targetId}`)) };
}

async function unlike(uid, targetType, targetId) {
  if (await redis.srem(`liked:${targetType}:${targetId}`, uid)) {
    await redis.hincrby('likes:count', `${targetType}:${targetId}`, -1);
  }
}

// 定时落库（方向保护防回退）
setInterval(async () => {
  const all = await redis.hgetall('likes:count');
  for (const [k, v] of Object.entries(all)) {
    await db.query(
      'UPDATE like_counter SET count = ? WHERE target = ? AND count < ?',
      [Number(v), k, Number(v)]);
  }
}, 60_000).unref();
```
