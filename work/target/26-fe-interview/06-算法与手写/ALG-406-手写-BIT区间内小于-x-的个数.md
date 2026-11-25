---
title: [ALG-406] 手写 BIT「区间内小于 x 的个数」：分段定价
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-406：手写 BIT「区间内小于 x 的个数」：分段定价

**答**：
- 题目：商品按价格分档（每档区间定价不同），运营查「价格区间 [lo, hi] 内小于 x 的商品数」。BIT 按「值 → 桶内商品数」，配合区间容斥。
- 思路：设 BIT2[price] = 该价格商品数（插入时 +1）；countLess(lo, hi, x) = sum(min(x,hi)) - sum(min(x,lo-1))，注意 x 越界钳制。
- 评分点：值域 BIT 复用；区间与阈值的双重钳制；多 BIT 组合意识。

```javascript
class PriceBandCounter {
  constructor(maxPrice) { this.max = maxPrice; this.bit = new BIT(maxPrice); this.n = 0; }
  add(price) { this.bit.add(price, 1); this.n++; }
  countLess(x) { return this.bit.sum(Math.max(0, Math.min(x, this.max))); }   // 钳制
  countInLess(lo, hi, x) {                                  // [lo,hi] 内 < x
    const hiClamp = Math.min(hi, x - 1);
    if (hiClamp < lo) return 0;
    return this.bit.sum(hiClamp) - this.bit.sum(lo - 1);
  }
  quantile(p) {                                             // 分位数价格（附赠）
    const k = Math.ceil(this.n * p);
    return kthFree(this.bit, k, this.max);                  // 复用 ALG-397 倍增
  }
}
```
