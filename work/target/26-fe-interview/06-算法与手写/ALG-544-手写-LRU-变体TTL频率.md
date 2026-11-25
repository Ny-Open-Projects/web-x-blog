---
title: [ALG-544] 手写 LRU 变体（TTL+频率）：缓存策略对比
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-544：手写 LRU 变体（TTL+频率）：缓存策略对比

**答**：
- 题目：缓存淘汰策略对比与实现——LRU（最近）、LFU（频率）、TTL（过期）三策略统一接口，按场景选型（ALG-404 关联）。给出 LRU+TTL 复合实现（Map 迭代序）。
- 思路：LRU：Map get 后 delete+set（挪尾），淘汰取首项；TTL：每项存 expire，get 时惰性过期；LFU：频次桶数组。
- 评分点：Map 迭代序实现 LRU；惰性 TTL；三策略的场景对照。

```javascript
class LRUTTLCache {
  constructor(cap, { ttlMs = 60000 } = {}) {
    this.cap = cap; this.ttl = ttlMs; this.map = new Map();   // 迭代序 = 访问序
  }
  get(k) {
    const v = this.map.get(k);
    if (!v) return undefined;
    if (Date.now() > v.expire) { this.map.delete(k); return undefined; }   // 惰性过期
    this.map.delete(k); this.map.set(k, v);                // 挪尾（最近使用）
    return v.value;
  }
  set(k, value) {
    if (this.map.has(k)) this.map.delete(k);
    this.map.set(k, { value, expire: Date.now() + this.ttl });
    while (this.map.size > this.cap) {                     // 超容淘汰首项（最旧）
      this.map.delete(this.map.keys().next().value);
    }
  }
}
// 策略对照：LRU（访问局部性强）/ LFU（稳定热点）/ TTL（时效数据）
// 生产缓存常用复合：LRU + TTL + 容量（ALG-319 多级缓存引擎）
```
