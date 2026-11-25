---
title: [NODE-042] 缓存穿透、击穿、雪崩的服务端对策？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-042：缓存穿透、击穿、雪崩的服务端对策？
**答**：
- **穿透**（查不存在的 key，每次都打 DB）：空值缓存（短 TTL）、布隆过滤器前置（先判断"可能存在"）、参数校验（非法 id 直接拒绝）。
- **击穿**（热点 key 过期瞬间大量回源）：互斥回源（分布式锁，只放一个请求去查 DB，其余等待读缓存）、singleflight（进程内合并同 key 并发请求）、逻辑过期（物理永不过期 + 后台异步刷新）。
- **雪崩**（大量 key 同时过期/Redis 宕机）：过期时间加随机抖动（`base + random`）、多级缓存（本地 LRU + Redis）、Redis 高可用（哨兵/集群）、熔断降级兜底（DB 限流，宁可返回旧数据/默认数据）。

```javascript
const pLimit = require('p-limit');

// singleflight：进程内合并对同一 key 的并发回源
const inflight = new Map();
async function singleflight(key, loader) {
  if (inflight.has(key)) return inflight.get(key);   // 后到的请求共享第一个的 Promise
  const p = loader().finally(() => inflight.delete(key));
  inflight.set(key, p);
  return p;
}

async function getHotData(id) {
  const key = `hot:${id}`;
  // 1. 布隆过滤器前置（防穿透）：不存在直接返回 null，不碰 DB
  if (!(await redis.bf?.exists('bloom:ids', id))) return null;

  const cached = await redis.get(key);
  if (cached) return JSON.parse(cached);

  // 2. 互斥回源（防击穿）：进程内 singleflight + Redis 锁
  return singleflight(key, async () => {
    const data = await db.query('SELECT * FROM items WHERE id = ?', [id]);
    // 3. TTL 加随机抖动（防雪崩）+ 空值短缓存（防穿透）
    const ttl = 600 + Math.floor(Math.random() * 120); // 600~720s
    await redis.setex(key, ttl, JSON.stringify(data));
    return data;
  });
}

// 4. 兜底：DB 层限流 + 降级（Redis 全挂时返回静态默认数据）
async function getWithFallback(id) {
  try { return await getHotData(id); }
  catch (e) {
    console.error('cache/db 失败，降级:', e.message);
    return DEFAULT_ITEM_MAP[id] ?? null; // 返回兜底数据而非 500
  }
}
```
