---
title: [NODE-774] 笔试题——实现多级请求合并（本地单飞 + 跨实例锁）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-774：手写跨实例合并

**需求与边界**：
- 需求：跨实例请求合并（SCN-NODE-691）——① 本地 in-flight map（同实例——SCN-FIN-541）；② 跨实例 Redis NX 锁（锁持有者回源、等待者轮询结果——SCN-NODE-652）；③ 结果共享（回源结果写 Redis 短 TTL——等待者从缓存拿）；④ 锁持有者失败 → 等待者降级重试（抢锁接力）。
- 边界：① 等待者轮询的成本（短间隔指数退避——SCN-NODE-641）；② 锁 TTL 与回源时长匹配（回源超时锁自动过期——下一实例接力）；③ 抖动重试（SCN-NODE-691 防风暴）。

**答**：
```javascript
async function coalesce(key, loader) {
  const local = inflight.get(key);
  if (local) return local;                             // 本地单飞（SCN-FIN-541）
  return withRetry(async (attempt) => {
    const got = await redis.set(`fly:${key}`, instanceId, 'PX', 5000, 'NX');   // 跨实例锁
    if (got) {
      const p = loader(key).finally(() => inflight.delete(key));
      inflight.set(key, p);
      const result = await p;
      await redis.setex(`fly-result:${key}`, 3, JSON.stringify(result));   // 结果共享 3s
      return result;
    }
    // 非持有者：轮询结果（指数退避——SCN-NODE-641）
    const result = await pollResult(key, attempt);     // Redis 取共享结果
    if (result) return result;
    throw new RetryAfter(50 + Math.random() * 200);    // 抖动重试（接力抢锁——SCN-NODE-691）
  }, 3);
}
```

**评分点**:
- 两级单飞（本地 map + 跨实例 NX 锁——SCN-NODE-652/691）。
- 结果共享短 TTL（等待者从缓存拿——不重复回源）。
- 接力抢锁（锁持有者失败 → 等待者抖动重试——SCN-NODE-691 防风暴）。
- 锁 TTL 与回源匹配（5s 过期接力——不死锁）。
