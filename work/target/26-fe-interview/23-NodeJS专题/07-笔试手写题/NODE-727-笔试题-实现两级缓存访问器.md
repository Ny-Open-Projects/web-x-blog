---
title: [NODE-727] 笔试题——实现两级缓存访问器（L1/L2 + 单飞 + 抖动）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-727：手写两级缓存

**需求与边界**：
- 需求：L1 进程 LRU + L2 Redis（SCN-NODE-640）——① miss 单飞回源（SCN-NODE-691 coalescing）；② TTL 抖动（雪崩防御——SCN-NODE-640）；③ L1 写透（L2 命中回填 L1）；④ 失效广播（pub/sub——写路径失效其他实例 L1，SCN-NODE-675）。
- 边界：① 单飞跨实例（Redis NX 锁——非本实例单飞）；② 序列化版本（L2 值 schema 变化——版本头）；③ pub/sub 失效的消息丢失容忍（TTL 兜底——SCN-NODE-640 一致性窗口）。

**答**：
```javascript
class TwoLevelCache {
  constructor() { this.l1 = new LRUCache({ max: 5000, ttl: 5_000 }); }
  async get(key, loader) {
    const l1 = this.l1.get(key); if (l1) return l1;
    const l2 = await redis.get(key); if (l2) { this.l1.set(key, l2); return l2; }
    return coalesceCrossInstance(key, async () => {              // 单飞（跨实例锁）
      const fresh = await loader(key);
      await redis.set(key, serialize(fresh), 'EX', 300 + jitter(60));   // TTL 抖动防雪崩
      this.l1.set(key, fresh);
      return fresh;
    });
  }
  async invalidate(key) {                              // 写路径失效
    await redis.del(key);
    redisPub.publish('cache:invalidate', key);         // 广播失效其他实例 L1
  }
}
redisSub.subscribe('cache:invalidate');
redisSub.on('message', (ch, key) => this.l1.delete(key));   // 其他实例 L1 失效
```

**评分点**:
- 三层读路径（L1→L2→loader）+ L1 回填。
- 跨实例单飞（Redis NX——SCN-NODE-691）。
- TTL 抖动（雪崩防御）+ pub/sub 失效广播（L1 一致性）。
- 失效消息丢失容忍（TTL 兜底——SCN-NODE-640 一致性窗口语义）。
