---
title: [NODE-326] Node 服务的多级缓存体系？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-326: Node 服务的多级缓存体系？
**答**:
- 层级：进程内 LRU（NODE-283，微秒级）→ Redis（毫秒级，跨实例共享）→ DB（源）。
- 一致性策略：L1 短 TTL（5~30s，容忍短暂陈旧换性能）+ L2 长 TTL + 主动失效（变更事件广播 pub/sub 让各实例清 L1）。
- 防击穿/穿透：单飞（同 key 并发只回源一次 NODE-269）、空值缓存（防穿透）、布隆过滤器（key 存在性预筛）。
- 指标：各级命中率——L1 命中率低（TTL 太短/容量小）优先调 L1。

```javascript
// 多级缓存读取
async function cachedGet(key, loader, { l1Ttl = 15_000, l2Ttl = 300_000 } = {}) {
  const l1 = lru.get(key);
  if (l1) return l1;
  const inflightKey = `if:${key}`;
  if (inflight.has(inflightKey)) return inflight.get(inflightKey);   // 单飞
  const p = (async () => {
    const l2 = await redis.get(`c:${key}`);
    if (l2) { const v = JSON.parse(l2); lru.set(key, v, l1Ttl); return v; }
    const v = await loader();
    await Promise.all([
      redis.set(`c:${key}`, JSON.stringify(v), { px: l2Ttl }),
      redis.publish('cache-invalidate', key),        // 通知其他实例清 L1（写路径）
    ]);
    lru.set(key, v, l1Ttl);
    return v;
  })();
  inflight.set(inflightKey, p); p.finally(() => inflight.delete(inflightKey));
  return p;
}
```
