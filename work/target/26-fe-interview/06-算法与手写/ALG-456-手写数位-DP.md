---
title: [ALG-456] 手写数位 DP：无前导零限制修正（位数不限编号）
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-456：手写数位 DP：无前导零限制修正（位数不限编号）

**答**：
- 题目：编号允许任意位数（如 7、007 视为不同编号？业务上 007 就是 7）——统计时前导零不应产生新编号。started 状态处理。
- 思路：dp(pos, tight, started)：未开始（全前导零）时继续不 started；一旦 started，0 也是有效数字。终态只对 started 计数（全零串不算）。
- 评分点：started 语义（前导零隔离）；终态排除空串；与「固定位数」场景的区别。

```javascript
function countNonZero(N) {                                 // [1, N] 非零编号个数
  const digits = String(N).split('').map(Number);
  const memo = new Map();
  function dfs(pos, tight, started) {
    if (pos === digits.length) return started ? 1 : 0;     // 全前导零不计
    const key = pos * 4 + (tight ? 2 : 0) + (started ? 1 : 0);
    if (!tight && memo.has(key)) return memo.get(key);
    const maxD = tight ? digits[pos] : 9;
    let total = 0;
    for (let d = 0; d <= maxD; d++) {
      if (!started && d === 0)
        total += dfs(pos + 1, tight && d === maxD, false);   // 继续前导零
      else
        total += dfs(pos + 1, tight && d === maxD, true);    // 已开始
    }
    if (!tight) memo.set(key, total);
    return total;
  }
  return dfs(0, true, false);
}
```
