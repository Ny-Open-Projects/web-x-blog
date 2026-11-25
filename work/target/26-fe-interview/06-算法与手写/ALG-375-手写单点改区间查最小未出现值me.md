---
title: [ALG-375] 手写单点改+区间查最小未出现值（mex 简化）：分桶 ID 分配
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-375：手写单点改+区间查最小未出现值（mex 简化）：分桶 ID 分配

**答**：
- 题目：分桶系统持续分配 ID（0~k），回收后 ID 可复用，查「当前最小未使用 ID」。线段树维护每桶占用计数，mex = 树上找第一个计数为 0 的叶子。
- 思路：树上二分变体——左子树「满」(计数 == 区间长) 走右，否则走左；找到即最小未用 ID。
- 评分点：满判断（sum == len）；二分方向；与 ALG-356 的同构关系。

```javascript
class MexTree {
  constructor(capacity) { this.n = capacity;
    this.t = new Array(4 * this.n).fill(0); }              // 叶子 = 0/1 占用
  acquire(id) { this.update(id, 1); }
  release(id) { this.update(id, -1); }
  update(i, v, node = 1, l = 0, r = this.n - 1) {
    if (l === r) return this.t[node] += v;
    const m = (l + r) >> 1;
    i <= m ? this.update(i, v, node * 2, l, m) : this.update(i, v, node * 2 + 1, m + 1, r);
    this.t[node] = this.t[node * 2] + this.t[node * 2 + 1];
  }
  mex(node = 1, l = 0, r = this.n - 1) {                   // 最小未使用 ID
    if (l === r) return this.t[node] === 0 ? l : -1;       // 未占用即答案
    const m = (l + r) >> 1;
    if (this.t[node * 2] < m - l + 1) return this.mex(node * 2, l, m);   // 左不满走左
    return this.mex(node * 2 + 1, m + 1, r);
  }
}
```
