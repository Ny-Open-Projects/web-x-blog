---
title: [MFW-618] Data Cache 的存储治理：LRU 与上限
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-618：Data Cache 存储治理

**答**:
- Data Cache 的存储增长：每 tag/fetch 结果的缓存条目——高基数 key（product:{id} × 100 万商品 = 100 万条目）——「缓存的存储上限」（磁盘/Redis 容量——无限增长的 OOM）；治理：LRU 淘汰（最近未用——长尾商品条目淘汰）+ TTL 兜底（revalidate 是逻辑过期——LRU 是物理上限）。
- 高基数 key 的设计：key 里带用户 id = 每用户一条（100 万用户 = 100 万条——个性化缓存容量规划）；「缓存的基数 × 条目大小 = 存储需求」的预算。
- 外置存储：Data Cache 落 Redis/KV（Next 的 cache handler 接口——自定义存储）；「cache handler 的接口」（get/set/revalidate——自建存储后端）；LRU 的实现责任转移到 handler。
- 追问钩子：为什么「高基数缓存」需要显式容量规划而「低基数」不用？——低基数（路由级 <1000 条）增长有界；高基数（per-entity/per-user）随数据线性增长（用户/商品数增长 = 缓存增长）；「缓存的基数 = 数据基数」时：缓存容量规划 = 数据规模规划（每条目 2KB × 100 万 = 2GB）；LRU + TTL 的双层过期：逻辑过期（revalidate——新鲜度）+ 物理上限（LRU——容量）——两层缺一：只有 TTL = 冷门条目永驻（占容量）；只有 LRU = 热门条目被误删（TTL 内被 LRU 淘汰 → 回源）。

```typescript
// Data Cache handler（自定义存储）
import { lru } from 'tiny-lru';
const store = lru(100_000, 3600_000);                    // 10 万条 + 1h 物理 TTL
export default class CacheHandler {
  async get(key) {
    const entry = store.get(key);
    if (!entry) return null;
    if (entry.revalidate && Date.now() > entry.timestamp + entry.revalidate * 1000)
      return { value: entry.value, revalidateAfter: 0 };   // 逻辑过期 → 后台重取
    return { value: entry.value, revalidateAfter: entry.timestamp + 3600_000 };
  }
  async set(key, value, ctx) {
    store.set(key, { value, revalidate: ctx.revalidate, timestamp: Date.now() });   // LRU 自动淘汰
  }
  async revalidateTag(tags) {
    // 反向索引：tag → keys
    for (const t of tags) for (const key of tagIndex.get(t) ?? []) store.delete(key);
  }
}
// 容量预算：基数 × 条目大小
const capacity = { entityCount: 1_000_000, entryKB: 2, totalGB: 2, lruCap: 100_000 };
// LRU 上限 < 数据基数：冷门条目自动淘汰（容量受控）
```
