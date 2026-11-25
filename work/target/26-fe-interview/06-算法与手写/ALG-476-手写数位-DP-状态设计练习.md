---
title: [ALG-476] 手写数位 DP 状态设计练习：多维状态压缩
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-476：手写数位 DP 状态设计练习：多维状态压缩

**答**：
- 题目：设计「含至少 3 个连续相同数字 且 数位和 % 5 == 0」的状态——需要 (repeatRun, repeatDigit, sumMod)，run 达 3 后可合并为 done。
- 思路：run < 3 时记 (prev, runLen)，run >= 3 合并为终态标志（状态空间从 10×n×5 压到 10×3×5 + done）。
- 评分点：状态合并压缩（run>=3 归一）；状态数估算；key 的序列化。

```javascript
function countTripleRepeat(N) {                            // 含 ≥3 连续相同 且 和%5==0
  const digits = String(N).split('').map(Number);
  const memo = new Map();
  // state: {done: bool} 或 {prev, run} + sumMod
  function dfs(pos, st, sumMod, started, tight) {
    if (pos === digits.length)
      return started && st.done && sumMod === 0 ? 1 : 0;
    const key = `${pos}|${st.done ? 'D' : st.prev + ',' + st.run}|${sumMod}|${tight}|${started}`;
    if (!tight && memo.has(key)) return memo.get(key);
    const maxD = tight ? digits[pos] : 9;
    let total = 0;
    for (let d = 0; d <= maxD; d++) {
      let ns;
      if (!started) ns = d > 0 ? { prev: d, run: 1, done: false } : { done: false, prev: -1, run: 0 };
      else if (st.done) ns = st;                           // 已满足：状态冻结
      else if (d === st.prev) {
        const run = st.run + 1;
        ns = run >= 3 ? { done: true } : { prev: d, run, done: false };   // run>=3 合并
      } else ns = { prev: d, run: 1, done: false };
      total += dfs(pos + 1, ns, (sumMod + (started || d > 0 ? d : 0)) % 5,
        started || d > 0, tight && d === maxD);
    }
    if (!tight) memo.set(key, total);
    return total;
  }
  return dfs(0, { done: false, prev: -1, run: 0 }, 0, false, true);
}
```
