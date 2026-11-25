---
title: [ALG-399] 手写 BIT 维护后缀和：剩余库存查询
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-399：手写 BIT 维护后缀和：剩余库存查询

**答**：
- 题目：库存按仓库编号 1..n，出库扣减，查「编号 >= x 的仓库剩余总量」。BIT 倒着建（或总数减前缀）。
- 思路：后缀和 = 总和 - 前缀和；BIT 只需正向。维护 total 变量 + 前缀 BIT 即可，避免反向 BIT 的思维弯路。
- 评分点：后缀 = 总-前缀的转化；total 维护；反向 BIT 的可选写法。

```javascript
class SuffixStock {
  constructor(stocks) { this.n = stocks.length;
    this.bit = new BIT(this.n); this.total = 0;
    stocks.forEach((v, i) => { if (v) { this.bit.add(i + 1, v); this.total += v; } });
  }
  deduct(warehouse, qty) {                                  // 出库
    const cur = this.bit.sum(warehouse) - this.bit.sum(warehouse - 1);
    const d = Math.min(qty, cur);                           // 不超库存
    this.bit.add(warehouse, -d); this.total -= d;
    return d;
  }
  remainingFrom(x) { return this.total - this.bit.sum(x - 1); }   // >= x 的剩余
}
```
