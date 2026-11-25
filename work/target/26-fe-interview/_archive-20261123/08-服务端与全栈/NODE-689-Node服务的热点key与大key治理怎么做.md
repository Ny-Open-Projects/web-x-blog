---
title: [NODE-689] Redis 热点 key 与大 key 治理怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-689：热点/大 key 怎么治理？
**答**：
- 热点 key：单 key QPS 极高打满单分片——本地缓存兜底（L1——SCN-NODE-640）、key 打散（key#1~N 随机后缀读，写时全写）、读写分离副本。
- 大 key：单 key 值过大（百 MB list/hash——删除阻塞/迁移卡顿）——拆分（hash 分桶）、删除用 unlink（异步删——不阻塞）、渐进式清理（hscan 分批删）。
- 检测：redis-cli --hotkeys/--bigkeys + 客户端埋点（慢命令监控）；大 key 删除排程（低峰）。
- 预防：写入大小约束（单值上限 schema 化——应用层拒绝）、集合 TTL 策略（避免无限增长）。
- 追问钩子：为什么「删除大 key 要用 unlink 而不是 del」——DEL 同步释放内存（百 MB 对象释放阻塞主线程几十至几百毫秒——Redis 单线程期间所有命令排队）；UNLINK 异步释放（后台线程）——Redis 单线程模型的资源操作纪律：阻塞操作必须异步化。

```javascript
// 热点 key 打散
const shard = Math.floor(Math.random() * 10);
await redis.get(`hot:${id}:${shard}`);                 // 读打散
await Promise.all(range(10).map(s => redis.set(`hot:${id}:${s}`, v)));   // 写全写
// 大 key 渐进删除
const cursor = 0; await redis.hscan(key, cursor, { COUNT: 100 });   // 分批
await redis.unlink(key);                               // 异步删
```
