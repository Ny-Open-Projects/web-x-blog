---
title: [ALG-472] 手写数位 DP 的分治视角（减法原理）：区间差
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-472：手写数位 DP 的分治视角（减法原理）：区间差

**答**：
- 题目：任何 [L, R] 计数 = f(R) - f(L-1)——这就是减法原理。扩展：「同时满足规则 A 或规则 B」的计数 = fA + fB - f(A 且 B)，容斥在数位 DP 上的应用。
- 思路：规则并集计数用容斥；规则交集直接合并状态。面试考察「多规则组合时的计数策略」。
- 评分点：减法原理是数位 DP 基石；容斥组合；交集合并状态 vs 容斥的取舍（状态数对比）。

```javascript
function countUnion(L, R, ruleA, ruleB) {                  // 满足 A 或 B 的计数
  const fA = countWithRule(L, R, ruleA);                    // f(R) - f(L-1) 封装
  const fB = countWithRule(L, R, ruleB);
  const fBoth = countWithRule(L, R, {                       // 交集：合并状态
    filter: x => ruleA.filter(x) && ruleB.filter(x),
    state: s => ({ ...ruleA.state(s), ...ruleB.state(s) }),   // 状态合并
  });
  return fA + fB - fBoth;                                   // 容斥
}
function countWithRule(L, R, rule) {
  // 通用数位 DP 封装：规则注入（过滤 + 状态），同 ALG-451 框架
  const f = (N) => {
    const digits = String(N).split('').map(Number);
    const memo = new Map();
    function dfs(pos, state, tight, started) {
      if (pos === digits.length) return started && rule.accept(state) ? 1 : 0;
      const key = `${pos}|${JSON.stringify(state)}|${tight}|${started}`;
      if (!tight && memo.has(key)) return memo.get(key);
      const maxD = tight ? digits[pos] : 9;
      let total = 0;
      for (let d = 0; d <= maxD; d++) {
        if (!rule.canTake(state, d, started)) continue;
        total += dfs(pos + 1, rule.transition(state, d, started),
          tight && d === maxD, started || d > 0);
      }
      if (!tight) memo.set(key, total);
      return total;
    }
    return dfs(0, rule.init(), true, false);
  };
  return f(R) - f(BigInt(L) - 1n + '');
}
```
