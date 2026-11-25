---
title: [ALG-508] 手写区间加权调度（DP+贪心排序）：广告排期收益
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-508：手写区间加权调度（DP+贪心排序）：广告排期收益

**答**：
- 题目：广告候选 [{start, end, profit}]，互不重叠地选，收益最大。加权版区间调度——贪心失效（收益不等），DP：按 end 排序 + p[i] = 最近不冲突的 j（二分）。
- 思路：dp[i] = max(dp[i-1], dp[p(i)] + profit[i])；p(i) = end <= start(i) 的最大 j（排序后二分）。
- 评分点：加权使贪心失效（反例）；p(i) 二分；DP 转移。

```javascript
function weightedIntervalScheduling(ads) {
  const sorted = [...ads].sort((a, b) => a.end - b.end);
  const ends = sorted.map(a => a.end);
  const dp = [0];                                          // dp[i]：前 i 个的最大收益
  const p = [0];                                           // p[i]：不冲突前驱
  for (let i = 1; i <= sorted.length; i++) {
    // 二分找 end <= start 的最大 j
    let lo = 0, hi = i - 1, j = 0;
    while (lo <= hi) { const m = (lo + hi) >> 1;
      ends[m] <= sorted[i - 1].start ? (j = m + 1, lo = m + 1) : hi = m - 1; }
    p[i] = j;
    dp[i] = Math.max(dp[i - 1], dp[p[i]] + sorted[i - 1].profit);
  }
  return dp[sorted.length];
}
// 贪心失效反例：[[0,10,100],[1,3,50],[4,6,50]] 按结束贪心选 [0,10] 得 100 < DP 100+... 
// 实际 DP 取 [1,3]+[4,6]=100 并列——构造 profit 更大即可反例
```
