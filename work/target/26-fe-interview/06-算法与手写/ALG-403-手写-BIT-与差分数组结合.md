---
title: [ALG-403] 手写 BIT 与差分数组结合：批量区间标记
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-403：手写 BIT 与差分数组结合：批量区间标记

**答**：
- 题目：任务依赖图，给一批「版本号区间」打标记（发布范围），查「某版本是否被标记」及「标记总数」。差分 BIT：区间标 +1，单点查 = 前缀和 > 0。
- 思路：同 ALG-392 差分转化；标记总数 = 每次区间加时维护 counter（比 sum(r)-sum(l-1) 简单）。
- 评分点：差分复用；覆盖次数与前缀 > 0 的语义；总数直维护。

```javascript
class RangeMarkBIT {
  constructor(maxVersion) { this.max = maxVersion; this.bit = new BIT(maxVersion);
    this.markCount = 0; }
  mark(l, r) {                                              // 区间打标记
    this.bit.add(l, 1); this.bit.add(r + 1, -1);
    this.markCount += r - l + 1;
  }
  isMarked(v) { return this.bit.sum(v) > 0; }               // 单点查：覆盖次数 > 0
  coverage(v) { return this.bit.sum(v); }                   // 被几个区间覆盖
  total() { return this.markCount; }
}
```
