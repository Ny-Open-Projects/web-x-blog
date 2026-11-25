---
title: [JS-390] 笔试：手写 LRU 缓存（O(1) 读写）
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 笔试题, 语言基础]
type: 笔试题
---

## JS-390：笔试：手写 LRU 缓存

**答**：实现 `LRUCache(capacity)`：① get/put 均 O(1)（Map 迭代顺序性质实现，不用手写双向链表也能 O(1)）；② put 超容量淘汰「最久未使用」；③ get 命中后提升为最新；④ 提供 peek（访问不提升）、delete、size；⑤ 支持迭代（按最新→最旧顺序）。写出实现与复杂度说明。

```javascript
class LRUCache {
  #map = new Map();
  constructor(capacity) {
    if (capacity <= 0) throw new Error('capacity must > 0');
    this.capacity = capacity;
  }
  get(key) {
    if (!this.#map.has(key)) return undefined;
    const v = this.#map.get(key);
    this.#map.delete(key);                 // 删掉重插 = 移到末尾(最新)
    this.#map.set(key, v);
    return v;
  }
  put(key, value) {
    if (this.#map.has(key)) this.#map.delete(key);
    else if (this.#map.size >= this.capacity)
      this.#map.delete(this.#map.keys().next().value);   // Map 首项 = 最旧
    this.#map.set(key, value);
  }
  peek(key) { return this.#map.get(key); }              // 不提升
  delete(key) { return this.#map.delete(key); }
  get size() { return this.#map.size; }
  *[Symbol.iterator]() { for (const [k, v] of [...this.#map].reverse()) yield [k, v]; } // 最新在前
}
```

**评分点**：
- 利用 Map 迭代顺序（插入序）实现 O(1) LRU：删除重插即提升、首项即最旧
- get 命中提升、peek 不提升的语义区分
- 淘汰时机：新增超容量才淘汰（更新已有 key 不淘汰）
- 迭代顺序按最新到最旧
