---
title: [NODE-041] Redis 在 BFF 中的三大经典场景：缓存、分布式锁、排行榜如何实现？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-041：Redis 在 BFF 中的三大经典场景：缓存、分布式锁、排行榜如何实现？
**答**：
- **缓存**：`GET` 未命中回源 DB 再 `SETEX`，注意 key 设计（`biz:实体:id`）、TTL、序列化与空值缓存（防穿透）。
- **分布式锁**：`SET key token NX EX 10`（原子加锁 + 过期防死锁），解锁用 **Lua 脚本判断持有者再删**（防误删他人锁）；续期用看门狗。高可用场景用 Redlock 或改用 ZooKeeper。
- **排行榜**：`ZADD`/`ZREVRANGE`/`ZINCRBY`，有序集合天然按分数排序，O(logN) 更新。
- 这三个场景是大厂高频压轴：要求能写出正确代码并说出错误写法的坑（如 `SETNX` + `EXPIRE` 两步非原子）。

```javascript
const Redis = require('ioredis');
const redis = new Redis();

// 1. 缓存：带空值缓存与 TTL
async function getUserProfile(uid) {
  const key = `user:profile:${uid}`;
  const cached = await redis.get(key);
  if (cached) return cached === '__NULL__' ? null : JSON.parse(cached); // 空值缓存防穿透
  const profile = await db.query('SELECT * FROM profiles WHERE uid = ?', [uid]);
  await redis.setex(key, profile ? 300 : 60, profile ? JSON.stringify(profile) : '__NULL__');
  return profile;
}

// 2. 分布式锁：原子加锁 + Lua 安全解锁
async function withLock(key, ttlSec, fn) {
  const token = crypto.randomUUID();          // 唯一持有标识
  const ok = await redis.set(`lock:${key}`, token, 'EX', ttlSec, 'NX');
  if (!ok) throw new BizError('LOCK_CONFLICT', '操作进行中，请稍后重试', 409);
  try {
    return await fn();
  } finally {
    // Lua：只有持有者才能删锁，防止超时后误删别人的锁
    await redis.eval(
      `if redis.call("get", KEYS[1]) == ARGV[1] then
         return redis.call("del", KEYS[1])
       else return 0 end`, 1, `lock:${key}`, token);
  }
}
// 使用：防止定时任务多实例重复执行
await withLock('sync-orders', 60, () => syncOrders());

// 3. 排行榜：ZSET
async function addScore(uid, points) {
  await redis.zincrby('rank:weekly', points, uid);          // 加分
  const top10 = await redis.zrevrange('rank:weekly', 0, 9, 'WITHSCORES'); // 前 10 名
  const myRank = await redis.zrevrank('rank:weekly', uid);   // 我的名次（0 起）
  const total = await redis.zcard('rank:weekly');
  return { top10: chunk(top10), myRank: myRank === null ? null : myRank + 1, total };
}
```
