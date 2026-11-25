---
title: [ALG-418] 手写 BIT 前缀 K 大近似：分位数监控
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-418：手写 BIT 前缀 K 大近似：分位数监控

**答**：
- 题目：接口延迟样本流，实时查「P90 延迟」＝按延迟值域建 BIT（计数），P90 = 第 ceil(0.9n) 小的样本值。与 ALG-397/417 同构：BIT 值域计数 + 倍增 kth。
- 思路：样本量可能巨大（百万级）——值域离散到 1ms 粒度桶（0~10000ms = 1 万桶），BIT O(log 1万)；精度损失可接受。
- 评分点：粒度离散的精度权衡；倍增 kth 复用；在线分位数替代方案（t-digest）的意识。

```javascript
class LatencyQuantile {
  constructor(maxMs = 10000) { this.max = maxMs; this.bit = new BIT(maxMs); this.n = 0; }
  record(ms) { const bucket = Math.min(this.max, Math.ceil(ms));   // 1ms 粒度
    this.bit.add(bucket, 1); this.n++; }
  quantile(p) {                                             // P90/P99
    const k = Math.max(1, Math.ceil(this.n * p));
    let pos = 0;
    for (let pw = 1 << 14; pw > 0; pw >>= 1) {              // 倍增 kth
      const next = pos + pw;
      if (next <= this.max && this.bit.sum(next) < k) pos = next;
    }
    return pos + 1;                                         // 毫秒粒度近似
  }
  // 工程补充：精确分位数用 t-digest/HdrHistogram（空间 O(几百)），BIT 版适合教学与小规模
```
