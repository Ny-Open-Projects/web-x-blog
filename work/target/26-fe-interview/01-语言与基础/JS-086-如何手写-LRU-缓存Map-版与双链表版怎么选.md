---
title: [JS-086] 如何手写 LRU 缓存？Map 版与双链表版怎么选？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-086：如何手写 LRU 缓存？Map 版与双链表版怎么选？

**答**：
- LRU：容量满时淘汰“最久未使用”的条目，get/put 都要把 key 移到最新位置。
- Map 版：利用 Map 保持插入序的特性，get 时 delete 再 set 即移到末尾，淘汰时删第一个 key，全部 O(1)。
- 双链表版：同样 O(1) 且语义更直白（头部最新、尾部最旧），但代码量大、要小心指针。
- 实际工程优先 Map 版；面试常要求手写双链表版以考察指针操作与哨兵节点技巧。

```javascript
// 版本一：Map 插入序版（生产推荐）
class LRUCacheMap {
  constructor(capacity) { this.capacity = capacity; this.map = new Map(); }
  get(key) {
    if (!this.map.has(key)) return -1;
    const val = this.map.get(key);
    this.map.delete(key);
    this.map.set(key, val); // 重新插入 = 移动到最新位置
    return val;
  }
  put(key, value) {
    if (this.map.has(key)) this.map.delete(key);
    else if (this.map.size >= this.capacity) {
      this.map.delete(this.map.keys().next().value); // 第一个插入的最旧
    }
    this.map.set(key, value);
  }
}

// 版本二：哈希表 + 双向链表（哨兵节点）
class Node {
  constructor(k, v) { this.k = k; this.v = v; this.prev = null; this.next = null; }
}
class LRUCacheList {
  constructor(capacity) {
    this.capacity = capacity;
    this.map = new Map();
    this.head = new Node(); this.tail = new Node(); // 哨兵：免去边界判空
    this.head.next = this.tail; this.tail.prev = this.head;
  }
  _remove(n) { n.prev.next = n.next; n.next.prev = n.prev; }
  _toFront(n) {
    n.next = this.head.next; n.prev = this.head;
    this.head.next.prev = n; this.head.next = n;
  }
  get(key) {
    const n = this.map.get(key);
    if (!n) return -1;
    this._remove(n); this._toFront(n);
    return n.v;
  }
  put(key, value) {
    let n = this.map.get(key);
    if (n) { n.v = value; this._remove(n); this._toFront(n); return; }
    if (this.map.size >= this.capacity) {
      const last = this.tail.prev;      // 尾部即最旧
      this._remove(last); this.map.delete(last.k);
    }
    n = new Node(key, value);
    this.map.set(key, n); this._toFront(n);
  }
}

const c = new LRUCacheList(2);
c.put(1, 'a'); c.put(2, 'b');
console.log(c.get(1)); // 'a' → 1 变最新
c.put(3, 'c');         // 淘汰 2
console.log(c.get(2), c.get(3)); // -1 'c'
```
