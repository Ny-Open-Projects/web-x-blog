---
title: [ALG-470] 手写数位 DP 打表预处理：高频查询优化
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-470：手写数位 DP 打表预处理：高频查询优化

**答**：
- 题目：同规则的高频查询（不同区间）——预处理「前缀计数表」：cnt[0..1e6] 每个数的合法计数前缀和（只对 ≤ 1e6 的小范围打表），大区间 = 打表部分 + 数位 DP 尾巴。
- 思路：小范围（< 1e6）打表 O(1e6) 一次；查询 > 1e6 部分走数位 DP；混合计算。
- 评分点：打表与 DP 的分段组合；空间预算（1e6 × 8B = 8MB）；线上场景的预计算意识。

```javascript
class PrecomputedCounter {
  constructor({ tableLimit = 1e6, rule = (x) => !String(x).includes('4') } = {}) {
    this.limit = tableLimit; this.rule = rule;
    this.table = new Float64Array(tableLimit + 1);          // 前缀计数表
    let c = 0;
    for (let i = 1; i <= tableLimit; i++) {
      if (rule(i)) c++;
      this.table[i] = c;
    }
  }
  count(N) {                                                // [1, N]
    const n = typeof N === 'string' ? BigInt(N) : BigInt(N);
    if (n <= BigInt(this.limit)) return this.table[Number(n)];   // 表内 O(1)
    const dpPart = countWithDP(N, this.limit);              // 大于表的部分走数位 DP
    return this.table[this.limit] + dpPart;
  }
}
function countWithDP(N, base) {                             // (base, N] 的计数
  const digits = String(N).split('').map(Number);
  const memo = new Map();
  function dfs(pos, tight, started) {
    if (pos === digits.length) return started ? 1 : 0;
    const key = pos * 4 + (tight ? 2 : 0) + (started ? 1 : 0);
    if (!tight && memo.has(key)) return memo.get(key);
    const maxD = tight ? digits[pos] : 9;
    let total = 0;
    for (let d = 0; d <= maxD; d++) {
      if (d === 4) continue;
      total += dfs(pos + 1, tight && d === maxD, started || d > 0);
    }
    if (!tight) memo.set(key, total);
    return total;
  }
  const total = dfs(0, true, false);
  return total - base;                                      // 减去表内已计
}
```
