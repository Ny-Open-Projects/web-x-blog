---
title: [ALG-473] 手写数位 DP 组合其他 DP：复合规则（交替序列）
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-473：手写数位 DP 组合其他 DP：复合规则（交替序列）

**答**：
- 题目：编号要求「相邻两位奇偶交替」（奇偶奇偶…），且「数位和为质数」。两个状态维度：(prevParity, sumMod)。
- 思路：状态组合 = prevParity(2) × sumMod(预置质数表模数或计数判断)；交替约束在转移时判断。
- 评分点：多维状态组合与转移；终态复合判定；状态数评估（2 × mod 值域）。

```javascript
function countAlternatingPrimeSum(N) {                     // 奇偶交替 + 数位和为质数
  const digits = String(N).split('').map(Number);
  const primes = new Set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]);
  const memo = new Map();
  function dfs(pos, prevParity, sum, tight, started) {
    if (pos === digits.length) return started && primes.has(sum) ? 1 : 0;
    const key = pos * 100 + prevParity * 50 + sum + (tight ? 100 : 0) + (started ? 200 : 0);
    if (!tight && memo.has(key)) return memo.get(key);
    const maxD = tight ? digits[pos] : 9;
    let total = 0;
    for (let d = 0; d <= maxD; d++) {
      if (started && d % 2 === prevParity) continue;       // 交替约束
      total += dfs(pos + 1, d % 2, sum + (started || d > 0 ? d : 0),
        tight && d === maxD, started || d > 0);
    }
    if (!tight) memo.set(key, total);
    return total;
  }
  return dfs(0, -1, 0, true, false);
}
```
