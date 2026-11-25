---
title: [ALG-522] 手写 BIT+贪心综合：库存分配
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-522：手写 BIT+贪心综合：库存分配

**答**：
- 题目：仓库按位置排布（位置 1..n 各有库存），订单按到达顺序从「最近的有货仓库」扣减——BIT 维护各位置库存，贪心找最近非零位（BIT 上二分前缀）。
- 思路：库存非零 = BIT 计数；找左边最近有货：倍增找第一个前缀计数差为 1 的位置（BIT 上二分）。同 ALG-397 结构。
- 评分点：BIT 计数语义；最近查找的倍增方向（左/右两棵或一棵翻转）；扣减同步。

```javascript
class StockAllocator {
  constructor(stocks) { this.n = stocks.length;
    this.bit = new BIT(this.n); this.left = [...stocks];
    stocks.forEach((v, i) => v && this.bit.add(i + 1, 1)); }   // 非零计数
  allocate(qty, fromPos) {                                  // 从 fromPos 向左找最近有货
    // 找 [1, fromPos] 内第一个非零位：倍增
    let pos = 0;
    for (let pw = 1 << 20; pw > 0; pw >>= 1) {
      const next = pos + pw;
      if (next <= fromPos && this.bit.sum(next) === 0) pos = next;   // 前缀全空则跳
    }
    const idx = pos + 1;
    if (idx > fromPos || this.left[idx - 1] === 0) return null;
    const d = Math.min(qty, this.left[idx - 1]);
    this.left[idx - 1] -= d;
    if (this.left[idx - 1] === 0) this.bit.add(idx, -1);   // 清零同步计数
    return { warehouse: idx, qty: d };
  }
}
```
