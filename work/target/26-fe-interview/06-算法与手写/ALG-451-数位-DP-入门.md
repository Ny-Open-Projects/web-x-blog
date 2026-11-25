---
title: [ALG-451] 数位 DP 入门：统计区间内含 7 的数字（号码池筛选）
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-451：数位 DP 入门：统计区间内含 7 的数字（号码池筛选）

**答**：
- 题目：号段池 [1, 1e9] 中含数字 7 的号码需要隔离，统计总数。数位 DP：逐位决策 + 状态记忆化。
- 思路：dp(pos, hasSeven, tight)：从高位往低位填数，hasSeven 记是否已出现 7，tight 表示当前前缀是否贴着上界。记忆化时 tight=false 的状态可缓存（tight=true 只有一条路径）。
- 评分点：tight 语义；记忆化只存 tight=false；区间 [L,R] 答案 = f(R) - f(L-1)。

```javascript
function countWithSeven(N) {                               // [1, N] 含 7 的个数
  const digits = String(N).split('').map(Number);
  const memo = new Map();
  // pos: 当前填第几位；hasSeven: 已含 7；tight: 前缀贴上界
  function dfs(pos, hasSeven, tight) {
    if (pos === digits.length) return hasSeven ? 1 : 0;    // 终止：含 7 计 1
    if (!tight && memo.has(pos * 2 + hasSeven))
      return memo.get(pos * 2 + hasSeven);                 // 记忆化（非 tight 才缓存）
    const maxD = tight ? digits[pos] : 9;
    let total = 0;
    for (let d = 0; d <= maxD; d++)
      total += dfs(pos + 1, hasSeven || d === 7, tight && d === maxD);
    if (!tight) memo.set(pos * 2 + hasSeven, total);
    return total;
  }
  return dfs(0, false, true);
}
// 区间 [L, R]：countWithSeven(R) - countWithSeven(L - 1)
// 复杂度：O(位数 × 状态数 × 10) ≈ O(10 × 2 × 10)
```
