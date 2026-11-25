---
title: [DP-508] 笔试：手写 LRU（带 TTL 与权重）
date: 2026-11-21
categories: [设计模式]
tags: [前端面试, 笔试题, 设计模式]
type: 笔试题
---

## DP-508：笔试：手写 LRU

**答**：实现带权重的 LRU 缓存：① 权重容量：按 value 的「估算大小」累计（maxWeight 5MB——不按条数）；② get 提升（Map 删除重插——O(1) LRU）；③ set 超权重：先过期淘汰再按最旧淘汰（惰性过期优先——TTL 到期的先清）；④ peek（不提升——纯读）；⑤ 统计（hits/misses/evictions）。写出实现。

```javascript
class WeightedLRU {
  #map = new Map(); #weight = 0;
  constructor({ maxWeight = 5 * 1024 * 1024, ttl = Infinity, estimate = (v) => JSON.stringify(v).length } = {}) {
    Object.assign(this, { maxWeight, ttl, estimate });
    this.stats = { hits: 0, misses: 0, evictions: 0 };
  }
  get(key) {
    const e = this.#map.get(key);
    if (!e) { this.stats.misses++; return undefined; }
    if (Date.now() - e.at > this.ttl) { this.#delete(key); this.stats.misses++; return undefined; }   // 惰性过期
    this.#map.delete(key); this.#map.set(key, e);     // 提升为最新
    this.stats.hits++;
    return e.v;
  }
  set(key, v) {
    const size = this.estimate(v);
    if (size > this.maxWeight) throw new Error('value exceeds cache capacity');
    if (this.#map.has(key)) this.#weight -= this.#map.get(key).size;
    // 先清过期, 再按最旧淘汰直到装得下
    const now = Date.now();
    for (const [k, e] of this.#map) if (now - e.at > this.ttl) this.#delete(k);
    while (this.#weight + size > this.maxWeight) this.#delete(this.#map.keys().next().value);
    this.#map.set(key, { v, at: now, size });
    this.#weight += size;
  }
  #delete(key) {
    const e = this.#map.get(key);
    if (e) { this.#weight -= e.size; this.#map.delete(key); this.stats.evictions++; }
  }
  peek(key) { return this.#map.get(key)?.v; }
}
```

**评分点**：
- 权重容量（estimate 函数——按大小不按条数）
- 惰性过期优先于 LRU 淘汰（过期先清——更公平）
- Map 删除重插实现 O(1) 提升
- peek 不提升 + 统计可观测
