---
title: [ALG-204] 结算页：优惠券组合凑出"恰好满减门槛"的最优组合（子集和 DP + 方案回溯）
date: 2026-11-19
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---
## ALG-204：结算页：优惠券组合凑出"恰好满减门槛"的最优组合（子集和 DP + 方案回溯）
**答**：购物车金额 X，可选优惠券 `[10, 20, 5, 30]`（每张最多用一次），要挑出和**恰好等于** X 的组合（凑单免运费），无解返回 null。

**思路**：0/1 子集和 DP：`dp[i][s] = 前 i 张能否凑出 s`。滚动一维 + parent 记录回溯方案。O(n·X)。

```javascript
function pickCoupons(coupons, target) {
  const n = coupons.length;
  // reach[s] = 凑出 s 的方案（记录最后使用的券索引链），用 Map 防大数组
  const reach = new Map([[0, []]]);              // 和 -> 使用的券索引列表
  for (let i = 0; i < n; i++) {
    const c = coupons[i];
    const additions = [];                        // 本轮新增（防同张券重复使用）
    for (const [s, idxs] of reach) {
      const ns = s + c;
      if (ns > target || reach.has(ns)) continue;
      additions.push([ns, [...idxs, i]]);
    }
    for (const [ns, idxs] of additions) {
      reach.set(ns, idxs);
      if (ns === target) return idxs.map((i) => coupons[i]);
    }
  }
  return null;
}
pickCoupons([10, 20, 5, 30], 35);  // => [10, 20, 5] 或 [5, 30]
// 复杂度：O(n·target) 时间、O(target) 空间（方案记录额外 O(解长)）
// 变体：允许每张券重复使用 => 完全背包（内层正序遍历）
```

**评分点**：
- 0/1 背包"每张最多一次"语义正确（快照本轮 additions，防止同券叠加）。
- 方案回溯（记录索引链）而不仅是可行性判定。
- 提前命中 target 即返回（剪枝）。
- 复杂度标注正确，能提"允许重复 = 完全背包"的变体。
