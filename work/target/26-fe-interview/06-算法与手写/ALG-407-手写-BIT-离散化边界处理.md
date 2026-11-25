---
title: [ALG-407] 手写 BIT 离散化边界处理：同值与等值边界
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-407：手写 BIT 离散化边界处理：同值与等值边界

**答**：
- 题目：离散化+BIT 的经典坑——查询「<= x 的个数」时 x 可能不在离散化集合里，且集合内有重复值。给出正确边界处理。
- 思路：去重离散化后查 rank 用 upperBound（<= x 的最大 rank）而非 lowerBound；插入用精确 rank；「< x」用 lowerBound-1。
- 评分点：upper vs lower 的语义区分；重复值去重后计数不受影响（BIT 计数在 rank 上可重复）；off-by-one 是高频 bug 点。

```javascript
class DiscreteBIT {
  constructor(values) {
    this.sorted = [...new Set(values)].sort((a, b) => a - b);   // 去重离散化
    this.bit = new BIT(this.sorted.length);
  }
  addExact(v) {                                             // 精确值插入
    const r = this.rankEq(v);
    if (r) this.bit.add(r, 1);
  }
  rankEq(v) {                                               // 精确 rank（二分）
    let lo = 0, hi = this.sorted.length - 1;
    while (lo <= hi) { const m = (lo + hi) >> 1;
      if (this.sorted[m] === v) return m + 1;
      this.sorted[m] < v ? lo = m + 1 : hi = m - 1; }
    return 0;                                               // 不存在
  }
  countLE(x) {                                              // <= x 的个数
    let lo = 0, hi = this.sorted.length;                    // upperBound
    while (lo < hi) { const m = (lo + hi) >> 1;
      this.sorted[m] <= x ? lo = m + 1 : hi = m; }
    return this.bit.sum(lo);                                // <=x 的最大 rank
  }
  countLT(x) {                                              // < x
    let lo = 0, hi = this.sorted.length;                    // lowerBound
    while (lo < hi) { const m = (lo + hi) >> 1;
      this.sorted[m] < x ? lo = m + 1 : hi = m; }
    return this.bit.sum(lo);
  }
}
```
