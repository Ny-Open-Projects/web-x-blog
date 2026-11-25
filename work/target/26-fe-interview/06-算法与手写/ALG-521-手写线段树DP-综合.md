---
title: [ALG-521] 手写线段树+DP 综合：分段最优投入
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-521：手写线段树+DP 综合：分段最优投入

**答**：
- 题目：n 天连续运营，每天有不同收益系数，运营动作「连续投入一段天数」收益 = 段和 × 段长系数；求总预算 P 内的最优投入分配。线段树维护区间和 + DP 状态（预算维度）。
- 思路：简化模型——投入只选互不重叠的段，dp[budget][pos] = 前 pos 天用 budget 的最大收益；段收益用线段树区间和 O(log) 取，转移枚举段终点。
- 评分点：DP 状态设计（预算 × 位置）；区间和查询加速；复杂度 O(P × n² / 优化)。

```javascript
function optimalInvestment(daily, budget) {
  const n = daily.length;
  const tree = buildSumTree(daily);                        // 线段树：区间和 O(log)
  const dp = Array.from({ length: budget + 1 }, () => new Array(n + 1).fill(0));
  for (let b = 1; b <= budget; b++)
    for (let i = 1; i <= n; i++) {
      dp[b][i] = dp[b][i - 1];                             // 第 i 天不投入
      for (let j = i; j >= 1; j--) {                       // 投入段 [j, i]
        const segSum = tree.query(j - 1, i - 1);           // 段收益（区间和）
        const cost = i - j + 1;                            // 段长 = 预算消耗
        if (cost <= b)
          dp[b][i] = Math.max(dp[b][i], dp[b - cost][j - 1] + segSum * (i - j + 1));
      }
    }
  return dp[budget][n];
}
function buildSumTree(a) {                                 // 复用 ALG-351 线段树
  const n = a.length; const t = new Array(4 * n);
  (function build(node, l, r) {
    if (l === r) return void (t[node] = a[l]);
    const m = (l + r) >> 1;
    build(node * 2, l, m); build(node * 2 + 1, m + 1, r);
    t[node] = t[node * 2] + t[node * 2 + 1];
  })(1, 0, n - 1);
  return { query: (ql, qr) => q(1, 0, n - 1, ql, qr) };
  function q(node, l, r, ql, qr) {
    if (qr < l || r < ql) return 0;
    if (ql <= l && r <= qr) return t[node];
    const m = (l + r) >> 1;
    return q(node * 2, l, m, ql, qr) + q(node * 2 + 1, m + 1, r, ql, qr);
  }
}
```
