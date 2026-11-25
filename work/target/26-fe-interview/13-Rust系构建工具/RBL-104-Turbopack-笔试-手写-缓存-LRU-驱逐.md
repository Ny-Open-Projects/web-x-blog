---
title: [RBL-104] 笔试：手写任务缓存 LRU 驱逐器（容量 + 冷任务驱逐）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-104：笔试：手写任务缓存 LRU 驱逐器（容量 + 冷任务驱逐）
**答**：实现 TaskCache(maxEntries)：1) get/set 基本语义，set 超容量时驱逐最久未使用；2) 记录命中统计（hits/misses/evictions）；3) pinned 集合：被下游依赖的任务不驱逐（依赖完整性）；4) 驱逐时若任务是 pinned 则跳过找下一个；5) get 命中要更新"最近使用"位置。

```javascript
class TaskCache {
  constructor(maxEntries = 100) {
    this.max = maxEntries;
    this.map = new Map();      // Map 保插入序：最新在最后
    this.pinned = new Set();
    this.stats = { hits: 0, misses: 0, evictions: 0 };
  }
  get(key) {
    if (!this.map.has(key)) { this.stats.misses++; return undefined; }
    const v = this.map.get(key);
    this.map.delete(key); this.map.set(key, v);  // 移到末尾 = 最近使用
    this.stats.hits++;
    return v;
  }
  set(key, value) {
    if (this.map.has(key)) this.map.delete(key);
    this.map.set(key, value);
    while (this.map.size > this.max) {
      const oldest = this.map.keys().next().value;
      if (this.pinned.has(oldest)) {
        // pinned：跳过，找下一个可驱逐的
        let victim = null;
        for (const k of this.map.keys())
          if (!this.pinned.has(k)) { victim = k; break; }
        if (!victim) break;               // 全 pinned：宁可超容也不破坏依赖
        this.map.delete(victim); this.stats.evictions++;
        continue;
      }
      this.map.delete(oldest); this.stats.evictions++;
    }
    return this;
  }
  pin(key) { this.pinned.add(key); return this; }
}
module.exports = { TaskCache };

// 命中率监控：stats.hits / (hits+misses) < 0.5 → 缓存配置有问题
```
**评分点**：
- LRU 用 Map 有序性实现（get 移尾 + 头部驱逐）。
- pinned 跳过驱逐（依赖完整性优先于容量）。
- 全 pinned 时的策略（允许超容，讲清取舍）。
- 命中/驱逐统计（可观测性）。
- 能联系构建缓存：被下游引用的任务结果被驱逐会导致重算不完整，pinned 正为此设计。
