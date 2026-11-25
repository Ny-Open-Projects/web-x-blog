---
title: [ALG-365] 手写线段树维护 GCD：批次步长一致性检测
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-365：手写线段树维护 GCD：批次步长一致性检测

**答**：
- 题目：流水线批次间隔（毫秒）序列，质检要查任意区间内步长的 GCD（判断节奏是否一致）。线段树合并函数 gcd。
- 思路：合并 = gcd(左 gcd, 右 gcd)；单点更新用赋值。JS 无内建 gcd，手写欧几里得。
- 评分点：gcd 合并满足结合律（可用线段树的数学前提）；欧几里得实现；单点赋值。

```javascript
class GCDSegTree {
  constructor(a) { this.n = a.length; this.t = new Array(4 * this.n); this.build(a); }
  static gcd(a, b) { while (b) [a, b] = [b, a % b]; return a; }
  build(a, node = 1, l = 0, r = this.n - 1) {
    if (l === r) return this.t[node] = a[l];
    const m = (l + r) >> 1;
    this.build(a, node * 2, l, m); this.build(a, node * 2 + 1, m + 1, r);
    this.t[node] = GCDSegTree.gcd(this.t[node * 2], this.t[node * 2 + 1]);
  }
  set(i, v, node = 1, l = 0, r = this.n - 1) {
    if (l === r) return this.t[node] = v;
    const m = (l + r) >> 1;
    i <= m ? this.set(i, v, node * 2, l, m) : this.set(i, v, node * 2 + 1, m + 1, r);
    this.t[node] = GCDSegTree.gcd(this.t[node * 2], this.t[node * 2 + 1]);
  }
  query(ql, qr, node = 1, l = 0, r = this.n - 1) {
    if (qr < l || r < ql) return 0;                        // gcd 单位元
    if (ql <= l && r <= qr) return this.t[node];
    const m = (l + r) >> 1;
    return GCDSegTree.gcd(this.query(ql, qr, node * 2, l, m),
      this.query(ql, qr, node * 2 + 1, m + 1, r));
  }
}
```
