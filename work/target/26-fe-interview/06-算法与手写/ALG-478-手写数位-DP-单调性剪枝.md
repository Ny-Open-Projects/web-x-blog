---
title: [ALG-478] 手写数位 DP 单调性剪枝：前缀确定后剪枝
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-478：手写数位 DP 单调性剪枝：前缀确定后剪枝

**答**：
- 题目：规则「编号必须大于某阈值 T」——数位 DP 时前缀一旦小于 T 的前缀即整支剪掉。单调性剪枝与 tight 的组合（增加 lowTight 维度）。
- 思路：增加 lowTight（前缀是否贴下界 T）：lowTight=true 时当前位 d 必须 >= T[pos]；两 tight 同时控制可行数字范围 [T[pos], N[pos]]。
- 评分点：双 tight（上界+下界）；可行数字范围收缩；状态数翻倍的代价评估。

```javascript
function countInRange(L, R) {                              // [L, R] 区间内计数（双 tight）
  const lo = String(L).split('').map(Number);
  const hi = String(R).split('').map(Number);
  const memo = new Map();
  function dfs(pos, mod, hiTight, loTight) {                // 双 tight
    if (pos === hi.length) return mod === 0 ? 1 : 0;
    const key = pos * 26 + mod * 2 + (hiTight ? 1 : 0) + (loTight ? 1 : 0) * 13;
    if (!hiTight && !loTight && memo.has(key)) return memo.get(key);   // 双不贴才缓存
    const minD = loTight ? lo[pos] : 0;                    // 下界约束
    const maxD = hiTight ? hi[pos] : 9;                    // 上界约束
    let total = 0;
    for (let d = minD; d <= maxD; d++)                     // 可行范围收缩
      total += dfs(pos + 1, (mod * 10 + d) % 7,
        hiTight && d === maxD, loTight && d === minD);
    if (!hiTight && !loTight) memo.set(key, total);
    return total;
  }
  return dfs(0, 0, true, true);
}
```
