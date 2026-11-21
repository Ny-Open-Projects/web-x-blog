---
title: [ALG-049] 内存缓存要淘汰"访问次数最少"的条目（LFU），次数相同时淘汰最久未访问的。请实现简版 LFU，并说明严格 O(1) 的做法？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-049：内存缓存要淘汰"访问次数最少"的条目（LFU），次数相同时淘汰最久未访问的。请实现简版 LFU，并说明严格 O(1) 的做法？
**答**：双 Map：`kv` 存值、`kf` 存频次；淘汰时线性扫描找最小频次，Map 的插入顺序天然保证同频次先淘汰先插入者。严格 O(1) 的 LFU 需要按频次分桶的双向链表（freq → 双向链表 + minFreq 指针），面试讲清思路即可。时间 get O(1)、put 淘汰时 O(n)（严格版 O(1)），空间 O(capacity)。

```javascript
class LFUCache {
  constructor(cap) {
    this.cap = cap;
    this.kv = new Map(); // key -> value（插入序即「最近访问序」）
    this.kf = new Map(); // key -> freq
  }
  _touch(key) {
    this.kf.set(key, this.kf.get(key) + 1);
    // 注意：Map.set 对已存在的 key 不会刷新插入序，
    // 必须显式 delete + set 才能把该 key 挪到「最近访问」位置，
    // 否则同频次淘汰会退化成按初始插入序而非访问序
    const v = this.kv.get(key);
    this.kv.delete(key);
    this.kv.set(key, v);
  }
  get(key) {
    if (!this.kv.has(key)) return -1;
    this._touch(key);
    return this.kv.get(key);
  }
  put(key, value) {
    if (this.kv.has(key)) { this._touch(key); this.kv.set(key, value); return; }
    if (this.kv.size >= this.cap) {
      let victim = null, minF = Infinity;
      for (const k of this.kv.keys()) {     // 按 kv 的访问序扫，同频次先遇到者更久未访问
        const f = this.kf.get(k);
        if (f < minF) { minF = f; victim = k; }
      }
      this.kv.delete(victim); this.kf.delete(victim);
    }
    this.kv.set(key, value);
    this.kf.set(key, 1);
  }
}
```
