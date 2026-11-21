---
title: [NODE-353] Node 服务的进程内缓存与失效（多实例一致性）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-353：进程内缓存与失效（多实例一致性）
**答**:
- 两级缓存结构：L1 进程内（LRU + TTL，微秒级访问）→ L2 Redis（毫秒级、跨实例共享）→ DB。读路径 L1 miss 查 L2 回填；写路径同时失效 L1（广播）+ L2。
- 多实例失效：写实例如何让其他实例的 L1 失效？——Pub/Sub 失效广播（写后 publish invalidate:key，各实例删本地）或短 TTL 兜底（L1 TTL 设 1~5s，接受秒级陈旧，简单可靠）。
- 一致性等级选择：配置/字典类（变更少）用广播强失效；热点数据（商品）用短 TTL 最终一致；强一致数据（余额）不进 L1。
- 防护：L1 容量上限（防内存泄漏 ARC-349）、击穿保护（单飞 singleflight：同 key 并发回源合并为一个请求）、预热（实例启动时加载热 key，防冷启动打 DB）。
- 可观测：两级命中率、失效广播延迟、singleflight 合并率。
```javascript
const l1 = new LRU({ max: 5000, ttl: 3000 });
async function get(key) {
  if (l1.has(key)) return l1.get(key);
  return singleflight(key, async () => {
    let v = await redis.get(key);
    if (!v) { v = await db.load(key); redis.set(key, v, 'EX', 300); }
    l1.set(key, v); return v;
  });
}
sub.on('message', (c, key) => l1.del(key));                       // 失效广播
```
