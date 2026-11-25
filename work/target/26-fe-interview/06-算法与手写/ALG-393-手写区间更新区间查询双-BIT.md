---
title: [ALG-393] 手写区间更新+区间查询（双 BIT）：区间累计奖励
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-393：手写区间更新+区间查询（双 BIT）：区间累计奖励

**答**：
- 题目：运营活动给 [l, r] 用户每人发 v 奖励，查任意区间的奖励总额（区间加 + 区间和）。双 BIT：b1 维护差分、b2 维护 i×d 的修正。
- 思路：区间 [l,r] 加 v：b1.add(l,v)、b1.add(r+1,-v)；b2.add(l, v*(l-1))、b2.add(r+1, -v*r)。前缀和 = b1.sum(i)*i - b2.sum(i)。
- 评分点：双 BIT 公式推导（Σd×i - Σi×d 修正）；四个 add 端点；公式记忆结构。

```javascript
class DoubleBIT {
  constructor(n) { this.n = n; this.b1 = new BIT(n); this.b2 = new BIT(n); }
  add(l, r, v) {
    this.b1.add(l, v); this.b1.add(r + 1, -v);
    this.b2.add(l, v * (l - 1)); this.b2.add(r + 1, -v * r);   // 修正项
  }
  prefix(i) { return this.b1.sum(i) * i - this.b2.sum(i); }
  range(l, r) { return this.prefix(r) - this.prefix(l - 1); }
}
// 推导：Σ_{j<=i} a[j] = Σ d[j]×(i-j+1) = i×Σd[j] - Σd[j]×(j-1) —— b2 就是后者
```
