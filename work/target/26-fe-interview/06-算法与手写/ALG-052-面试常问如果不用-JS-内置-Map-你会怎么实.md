---
title: [ALG-052] 面试常问"如果不用 JS 内置 Map，你会怎么实现 HashMap？"请手写一个支持 set/get/delete 的简版 HashMap（拉链法解决冲突）。
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-052：面试常问"如果不用 JS 内置 Map，你会怎么实现 HashMap？"请手写一个支持 set/get/delete 的简版 HashMap（拉链法解决冲突）。
**答**：底层是桶数组，好哈希函数要求分布均匀且稳定：对 key 字符串用 31 进制滚动哈希，模桶数定位桶；冲突的键值对在同一桶的链（数组）里线性查找——这就是"拉链法"。工程上桶数随元素数扩容、桶内过长转红黑树是进阶话题。平均时间 O(1)，最坏 O(n)，空间 O(n)。

```javascript
class SimpleHashMap {
  constructor(size = 1024) {
    this.buckets = Array.from({ length: size }, () => []);
    this.size = size;
  }
  _hash(key) {
    const s = String(key);
    let h = 0;
    for (let i = 0; i < s.length; i++) {
      h = (h * 31 + s.charCodeAt(i)) >>> 0; // 31 进制滚动哈希
    }
    return h % this.size;
  }
  set(key, value) {
    const bucket = this.buckets[this._hash(key)];
    const item = bucket.find(it => it.key === key);
    if (item) item.value = value;
    else bucket.push({ key, value });       // 拉链：冲突挂同一条链
  }
  get(key) {
    return this.buckets[this._hash(key)].find(it => it.key === key)?.value;
  }
  delete(key) {
    const bucket = this.buckets[this._hash(key)];
    const idx = bucket.findIndex(it => it.key === key);
    if (idx !== -1) bucket.splice(idx, 1);
  }
}
```
