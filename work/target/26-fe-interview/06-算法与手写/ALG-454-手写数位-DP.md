---
title: [ALG-454] 手写数位 DP：数字 1 出现次数（报表统计）
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-454：手写数位 DP：数字 1 出现次数（报表统计）

**答**：
- 题目：统计 [1, N] 所有数字中「字符 1 出现的总次数」（如 11 贡献 2 次）。每位独立贡献计数。
- 思路：dp(pos, tight, started) 返回「后缀中 1 的总次数」——复杂点：每一位的贡献 = 该位取 1 时后缀自由组合数 × 1。用「计数 DP + 幂次」组合：cnt = Σ (每位取 1 的方案数)。更简洁的公式法：对第 i 位，贡献 = 高位取值 × 10^低位 + (高位贴上界时的修正)。
- 评分点：每位贡献的分解；公式法与 DFS 法对比；started 处理前导零。

```javascript
function countOnes(N) {                                    // [1, N] 中 1 的总次数
  const digits = String(N).split('').map(Number);
  const memo = new Map();
  // started: 是否已开始（前导零不算数字位）；返回该后缀中 1 的出现总次数
  function dfs(pos, tight, started) {
    if (pos === digits.length) return 0;
    const key = pos * 4 + (tight ? 2 : 0) + (started ? 1 : 0);
    if (!tight && memo.has(key)) return memo.get(key);
    const maxD = tight ? digits[pos] : 9;
    let total = 0;
    for (let d = 0; d <= maxD; d++) {
      const nStarted = started || d > 0;
      total += dfs(pos + 1, tight && d === maxD, nStarted)
        + ((nStarted && d === 1) ? suffixCount(pos + 1, tight && d === maxD) : 0);   // 当前位取 1 的贡献
    }
    if (!tight) memo.set(key, total);
    return total;
  }
  function suffixCount(pos, tight) {                       // 后缀自由组合数
    if (!tight) return Math.pow(10, digits.length - pos);
    let v = 0;
    for (let p = pos; p < digits.length; p++) v = v * 10 + digits[p] + 1;
    return v;
  }
  return dfs(0, true, false);
}
// 简化公式法：第 i 位（从高到低）贡献 = 高位值 × 10^低位数 + min(当前位>1 ? 10^低 : 当前位==1 ? 低位+1 : 0)
```
