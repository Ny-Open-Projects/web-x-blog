---
title: [ALG-392] 手写区间更新（差分）+单点查询 BIT：多批次调价后的当前价
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-392：手写区间更新（差分）+单点查询 BIT：多批次调价后的当前价

**答**：
- 题目：商品价格被多批次区间调价（如「第 3~7 批次每批 +5 元」），查某批次最终价格。BIT 维护差分数组：区间加 = 两端单点改，单点查 = 前缀和。
- 思路：差分 d[i] = a[i] - a[i-1]；区间 [l,r] 加 v → d[l] += v, d[r+1] -= v；前缀和即原值。BIT 恰好擅长「单点改+前缀查」。
- 评分点：差分转化思想；两次单点改实现区间加；前缀和还原原值。

```javascript
class RangeAddPointQuery {
  constructor(n) { this.n = n; this.bit = new BIT(n); }
  add(l, r, v) {                                            // 区间加 → 差分两端改
    this.bit.add(l, v);
    this.bit.add(r + 1, -v);
  }
  query(i) { return this.bit.sum(i); }                      // 单点查 = 差分前缀和
}
// 调价：price.add(3, 7, 5) 表示第 3~7 批次各 +5；price.query(5) = 第 5 批次累计调价
```
