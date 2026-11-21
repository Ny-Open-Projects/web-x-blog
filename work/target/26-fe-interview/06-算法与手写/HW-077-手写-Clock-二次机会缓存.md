---
title: [HW-077] 手写 Clock（二次机会/近Clock）缓存——低成本近似 LRU 的淘汰策略
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：Clock 算法：环形队列 + 指针 + 每项引用位 ref。命中置 ref=1；淘汰时指针扫过去，ref=1 的清零给"二次机会"继续走，ref=0 的直接淘汰。用 O(1) 操作近似 LRU，无双向链表开销，适合大容量缓存（如 OS 页缓存、前端大资源池）。

```javascript
class ClockCache {
  constructor(capacity) {
    this.cap = capacity;
    this.slots = [];      // [{key, val, ref}]
    this.map = new Map(); // key -> slot index
    this.hand = 0;        // 扫描指针
  }
  get(key) {
    const i = this.map.get(key);
    if (i == null) return undefined;
    this.slots[i].ref = 1;                 // 命中给"引用位"
    return this.slots[i].val;
  }
  set(key, val) {
    if (this.map.has(key)) { const s = this.slots[this.map.get(key)]; s.val = val; s.ref = 1; return; }
    if (this.slots.length >= this.cap) {   // 淘汰循环
      for (;;) {
        const s = this.slots[this.hand];
        if (s.ref === 1) { s.ref = 0; this.hand = (this.hand + 1) % this.cap; }  // 二次机会：清零
        else break;                                                               // ref=0 直接淘汰
      }
      const victim = this.slots[this.hand];
      this.map.delete(victim.key);
      this.slots[this.hand] = { key, val, ref: 0 };   // 复用槽位
      this.map.set(key, this.hand);
      this.hand = (this.hand + 1) % this.cap;
    } else {
      this.map.set(key, this.slots.length);
      this.slots.push({ key, val, ref: 0 });
    }
  }
}
// 对比 LRU：无需双向链表与频繁摘链，代价是淘汰精度略差（一次扫描近似）
```

**评分点**：
- 二次机会语义正确：ref=1 清零跳过，ref=0 淘汰，指针环形推进。
- 命中置 ref、插入复用槽位（数组环形复用而非无限增长）。
- 指针取模推进防越界；能说明与 LRU 的成本/精度权衡。
- map 索引与槽位一致性维护（淘汰时 delete）。
