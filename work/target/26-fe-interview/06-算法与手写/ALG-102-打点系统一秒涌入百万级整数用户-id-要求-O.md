---
title: [ALG-102] 打点系统一秒涌入百万级整数用户 id，要求 O(1) 判断某 id 是否首次上报（去重），内存还不能爆。用什么数据结构？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-102：打点系统一秒涌入百万级整数用户 id，要求 O(1) 判断某 id 是否首次上报（去重），内存还不能爆。用什么数据结构？
**答**：位图（Bitmap）。用 `Uint32Array`，每个 32 位整数管 32 个 id：`id >> 5` 定位字、`id & 31` 定位位。一亿用户只需约 12.5MB，比 `Set<number>`（每 number 占 8 字节以上）省两个数量级。单次 add/has O(1)，统计总量需遍历 O(N/32)。

```javascript
class Bitmap {
  constructor(maxId) {
    this.bits = new Uint32Array((maxId >> 5) + 1); // 每个 uint32 管 32 个 id
  }
  has(id) { return (this.bits[id >> 5] & (1 << (id & 31))) !== 0; }
  add(id) {
    const w = id >> 5, m = 1 << (id & 31);
    if (this.bits[w] & m) return false; // 已存在 => 重复打点
    this.bits[w] |= m;
    return true; // 首次上报
  }
  count() { // 统计已标记人数：Brian Kernighan 逐字消 1
    let c = 0;
    for (const w of this.bits) { let x = w; while (x) { x &= x - 1; c++; } }
    return c;
  }
}
// 一亿用户 id 的去重位图：new Bitmap(1e8)，约 12.5MB
```
