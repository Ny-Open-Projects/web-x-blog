---
title: [OPT-159] 大数组/Map 缓存的清理时机怎么设计（上限 + 惰性清理）？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-159：大数组/Map 缓存的清理时机怎么设计（上限 + 惰性清理）？

**答**：
- 缓存清理两个时机点：**写入时**（超上限立即驱逐，内存增长有界，推荐默认）和**惰性清理**（GC 时机未知，所以不能依赖"标记后等 GC"，要自己删引用）。
- 惰性清理的正确用法：TTL 不在写入时检查（写多读少场景浪费），而是在 **get 命中时**校验过期才删——读不到的脏数据不占访问成本，但内存仍受 max 上限兜底。
- 大数组分片清理：10 万条日志数组不能一次 splice（造成长任务），按片淘汰（每写 1000 条清最老 1000 条），清理由 idle 回调执行。
- WeakMap/WeakRef 的适用场景：以对象为 key 的附加数据（DOM 节点元信息），靠 GC 自动回收，无需手动清理。

```javascript
// 一一对应：TTL + 上限双约束的缓存（写入驱逐 + 读取惰性过期）
class TTLCache {
  constructor({ max = 200, ttl = 10 * 60_000 } = {}) {
    this.max = max; this.ttl = ttl; this.map = new Map(); // Map 保序
  }
  get(key) {
    const hit = this.map.get(key);
    if (!hit) return undefined;
    if (Date.now() - hit.t > this.ttl) {
      this.map.delete(key);          // 惰性过期：读时才删，避免定时器扫描全表
      return undefined;
    }
    this.map.delete(key); this.map.set(key, hit); // 触碰移到最新（LRU）
    return hit.v;
  }
  set(key, value) {
    if (this.map.has(key)) this.map.delete(key);
    this.map.set(key, { v: value, t: Date.now() });
    while (this.map.size > this.max) {                  // 写入时驱逐，内存增长有硬上限
      const oldest = this.map.keys().next().value;
      this.map.delete(oldest);
    }
  }
}

// 大数组分片淘汰：避免一次清 10 万条造成长任务
class ShardedList {
  constructor(shardSize = 1000) { this.shardSize = shardSize; this.shards = []; }
  push(...items) {
    this.shards.push(items);
    if (this.shards.length > 100) {                     // 超 10 万条触发异步淘汰
      (window.requestIdleCallback || setTimeout)(() => {
        this.shards.splice(0, 10);                      // idle 时一次只清 1 万条，分帧消化
      });
    }
  }
}
```
