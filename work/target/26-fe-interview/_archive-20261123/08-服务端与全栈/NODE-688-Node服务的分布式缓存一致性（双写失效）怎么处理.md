---
title: [NODE-688] 分布式缓存一致性（双写/失效）怎么处理？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-688：缓存一致性怎么处理？
**答**：
- 写路径选型：cache-aside（先写源后删缓存——主流，简单且并发竞态窗口小）vs 双写（同时更新——写失败缓存脏，需补偿）vs 订阅 binlog（Canal 监听 DB 变更失效缓存——解耦但延迟）。
- 删除失败的兜底：删缓存失败 → 重试队列/订阅 binlog 二次删除（补偿路径）——「删失败不丢一致性的最终保证」。
- 一致性窗口：cache-aside 的不一致窗口 = 写后到下次删除/过期——短 TTL 兜底（SCN-NODE-640）；强一致需求不走缓存（直读源）。
- 缓存与主从延迟：读副本场景下 cache-aside 的「读旧写新」——读己之写 bypass（SCN-NODE-654 读主库 bypass 缓存）。
- 追问钩子：为什么 cache-aside 是「删缓存」而不是「更新缓存」——并发写 A（先到）与 B（后到）：更新缓存的顺序不定（B 的旧计算可能后写——缓存脏且无自愈）；删除缓存让下次读回源（新数据必然正确）——「删除是幂等且并发安全的，更新不是」。

```javascript
async function write(key, data) {
  await db.update(key, data);                          // 1. 先写源
  await redis.del(key).catch(() => retryQueue.push(key));   // 2. 删缓存（失败补偿）
  // 读路径 cache-aside：miss 回源 + 回填（SCN-NODE-640）
}
```
