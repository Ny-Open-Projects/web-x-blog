---
title: [JS-293] 笔试：手写 LRU 缓存（Map 实现）
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 数据结构]
type: 笔试题
---

## JS-293：笔试：手写 LRU 缓存

**题目**：实现 `LRUCache(capacity)`：get/put O(1)；get 与 put 都把键移到「最新」；超容量淘汰最旧；利用 Map 的插入顺序实现。

**答**：
```javascript
class LRUCache {
  #cap; #map = new Map(); // Map 保持插入顺序：头部最旧，尾部最新
  constructor(capacity) {
    if (capacity <= 0) throw new RangeError('capacity > 0');
    this.#cap = capacity;
  }
  get(key) {
    if (!this.#map.has(key)) return -1;
    const v = this.#map.get(key);
    this.#map.delete(key);     // 删除再插入 = 移到最新
    this.#map.set(key, v);
    return v;
  }
  put(key, value) {
    if (this.#map.has(key)) this.#map.delete(key);
    else if (this.#map.size >= this.#cap) {
      this.#map.delete(this.#map.keys().next().value); // 迭代器第一个 = 最旧
    }
    this.#map.set(key, value);
  }
  get size() { return this.#map.size; }
}

const lru = new LRUCache(2);
lru.put(1, 'a'); lru.put(2, 'b');
lru.get(1);        // 'a'（1 变最新）
lru.put(3, 'c');   // 淘汰 2（最旧）
lru.get(2);        // -1
```

**评分点**：
- Map 插入顺序 + delete/set 组合实现 O(1) 的「移到最新」——核心技巧
- 淘汰用 keys().next().value 取最旧
- put 已存在键时先删再插（顺序刷新）
- 对比双向链表实现的复杂度相同但代码量差异（加分）
