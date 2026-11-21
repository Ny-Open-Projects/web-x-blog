---
title: [HW-076] 手写 LFU 缓存——访问次数淘汰 + 同频次内 LRU（O(1) 两级结构）
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：LFU 难点在 O(1)：需要两级结构——`freqMap: freq -> 双向链表（该频次的键，链头最旧）`，外加 `key -> {value, freq, node}` 索引。get/set 都把 key 从 freq 链挪到 freq+1 链头（链尾最旧先淘汰）；容量满时从最小频次链的尾端淘汰；最低频次指针随淘汰上移、随新增复位为 1。

```javascript
class LFUCache {
  constructor(capacity) {
    this.cap = capacity;
    this.keyNode = new Map();     // key -> node {key, val, freq, prev, next}
    this.freqList = new Map();    // freq -> {head, tail} 双向链表哨兵
    this.minFreq = 0;
  }
  #detach(node) {
    node.prev.next = node.next; node.next.prev = node.prev;
  }
  #pushFront(freq, node) {        // 插到该频次链头（最新）
    let list = this.freqList.get(freq);
    if (!list) { const head = { prev: null, next: null }, tail = { prev: head, next: null };
      head.next = tail; tail.prev = head; list = { head, tail };
      this.freqList.set(freq, list); }
    node.next = list.head.next; node.prev = list.head;
    list.head.next.prev = node; list.head.next = node;
  }
  #popLeast() {                   // 淘汰 minFreq 链尾（最旧）
    const list = this.freqList.get(this.minFreq);
    const node = list.tail.prev;
    this.#detach(node);
    this.keyNode.delete(node.key);
    if (list.head.next === list.tail) this.freqList.delete(this.minFreq); // 空链清理
  }
  #bump(node) {                   // node.freq -> freq+1，并维护 minFreq
    this.#detach(node);
    if (this.freqList.get(node.freq).head.next === this.freqList.get(node.freq).tail)
      this.freqList.delete(node.freq);
    if (this.minFreq === node.freq && !this.freqList.has(node.freq)) this.minFreq++;
    node.freq++;
    this.#pushFront(node.freq, node);
  }
  get(key) {
    const node = this.keyNode.get(key);
    if (!node) return undefined;
    this.#bump(node);
    return node.val;
  }
  set(key, val) {
    if (this.cap <= 0) return;
    const node = this.keyNode.get(key);
    if (node) { node.val = val; this.#bump(node); return; }
    if (this.keyNode.size >= this.cap) this.#popLeast();
    const nn = { key, val, freq: 1, prev: null, next: null };
    this.keyNode.set(key, nn);
    this.#pushFront(1, nn);
    this.minFreq = 1;              // 新增 1 频次项，最低频复位
  }
}
// set(a) set(b) set(c) get(a) → 满后 set(d)：c（freq=1 且最旧）被淘汰；a 因被访问过存活
```

**评分点**：
- 两级结构（freq 桶 + 桶内双向链表）保证 O(1) get/set，这是核心考点。
- 同频次内按 LRU 淘汰（链尾最旧），get 重插链头。
- minFreq 维护正确：淘汰空链上移、新增 key 复位 1。
- 满容量插入前先淘汰；cap<=0 边界。
