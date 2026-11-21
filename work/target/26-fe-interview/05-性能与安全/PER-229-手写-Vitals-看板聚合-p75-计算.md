---
title: [PER-229] 笔试题：手写前端看板的 p75 分位数计算（近端分桶近似 + 精确版），说明为什么不能用平均值
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-229：手写前端看板的 p75 分位数计算（近端分桶近似 + 精确版），说明为什么不能用平均值

**题目**：实现：① `percentile(sorted, p)` 精确计算（线性插值法）；② `bucketP75(buckets)` 基于直方图分桶（如 [0,100,200,400,800,1600,∞) 的计数数组）的近似 p75，说明分桶粒度对误差的影响；③ 解释为什么性能指标用 p75 而不是平均值，以及桶边界为什么取 2 的幂次。

**答**：上报端常只发分桶计数（省带宽、防明细泄漏），服务端用直方图近似分位数。桶按 2 的幂次划分是 Web Vitals 官方做法：相对误差均匀，跨量级指标（几十 ms 到几秒）都适用。

```javascript
// 精确版：线性插值
function percentile(sorted, p) {
  if (!sorted.length) return 0;
  const idx = (sorted.length - 1) * p;
  const lo = Math.floor(idx), hi = Math.ceil(idx);
  return sorted[lo] + (sorted[hi] - sorted[lo]) * (idx - lo);
}

// 分桶近似版：buckets = [{ upper: 100, count: 120 }, { upper: 200, count: 80 }, ...]
function bucketP75(buckets, total) {
  const target = total * 0.75;
  let cum = 0, loBound = 0, hiBound = 0, cntInBucket = 0;
  for (const b of buckets) {
    cum += b.count;
    if (cum >= target) { hiBound = b.upper; cntInBucket = b.count; break; }
    loBound = b.upper;
  }
  if (!cntInBucket) return hiBound || Infinity;    // 落在最后一个开放桶
  // 桶内均匀假设线性插值
  const prevCum = cum - cntInBucket;
  return loBound + (hiBound - loBound) * ((target - prevCum) / cntInBucket);
}

const buckets = [{upper:100,count:400},{upper:200,count:300},{upper:400,count:200},{upper:800,count:100}];
// bucketP75(buckets, 1000) ≈ 200 + 200 * (750-700)/300 ≈ 233ms
// 为什么不用平均值：延迟长尾分布下，均值会被海量快样本稀释，
// p75 直接对应"最慢的 25% 用户"——这正是 Core Web Vitals 的验收口径
```

**评分点**：
- 精确版用线性插值而非直接取下标（避免阶跃误差）。
- 分桶版处理"累计越过目标桶 + 桶内线性插值"，并处理末位开放桶。
- 能说清 p75 vs 平均值的选择理由（长尾、口径对齐 CWV）。
- 桶边界用 2 的幂次（100/200/400/800/1600），相对误差均匀。
