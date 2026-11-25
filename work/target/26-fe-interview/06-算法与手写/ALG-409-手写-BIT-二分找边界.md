---
title: [ALG-409] 手写 BIT 二分找边界：预算累计扣减
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-409：手写 BIT 二分找边界：预算累计扣减

**答**：
- 题目：预算分桶（各渠道配额），扣款按渠道顺序，求「扣 X 后停在哪个渠道、扣多少」。BIT 前缀和 + 二分（或倍增，同 ALG-397）。
- 思路：倍增找第一个前缀和 >= X 的渠道 idx；该渠道扣余额 = X - sum(idx-1)；更新 BIT。
- 评分点：倍增与二分两种实现；部分扣减边界；BIT 更新同步。

```javascript
class BudgetDeductBIT {
  constructor(quotas) { this.n = quotas.length;
    this.bit = new BIT(this.n); this.left = [...quotas];
    quotas.forEach((q, i) => this.bit.add(i + 1, q)); }
  deduct(amount) {                                          // 顺序扣款
    // 倍增找第一个前缀和 >= amount 的渠道
    let pos = 0;
    for (let pw = 1 << 20; pw > 0; pw >>= 1) {
      const next = pos + pw;
      if (next <= this.n && this.bit.sum(next) < amount) pos = next;
    }
    const idx = pos + 1;
    if (idx > this.n) return { done: false, spent: 0 };     // 总额不足
    const before = this.bit.sum(idx - 1);
    const deduct = Math.min(amount - before, this.left[idx - 1]);
    this.bit.add(idx, -deduct); this.left[idx - 1] -= deduct;
    return { done: true, channel: idx, spent: deduct, remain: amount - deduct };
  }
}
```

## 追问（补充）

**追问**：

1. 倍增找边界为什么比「二分 + 前缀和」快？ → 二分每次要调 `sum()` 是 O(log n)，整体 O(log²n)；真正的倍增要直接在 BIT 树节点上取 `t[next]`、把命中节点的值累加到 acc，边累加边前进，才是 O(log n)——本例每步仍调 `sum()`，实际是 O(log²n)，与二分同阶。
2. `pw` 的初值 `1 << 20` 为什么是安全的？ → 它必须大于 n 的最高位；若 n 可能超过 2^20，应写成 `1 << (31 - Math.clz32(n))` 由 n 推出，否则大数组直接找不到边界。
3. 部分扣减时余额与 BIT 怎么保持一致？ → 先算出「这次实际扣了多少」（`min(amount-before, left[idx-1])`），再对 BIT 和 left 同步扣同一个数；只更新其中一个，后续查询全部错位。
4. 并发扣款需要加什么？ → 前端单线程但仍要与服务端对账：请求带幂等键（同一笔扣款重试不重复扣），本地余额只做乐观展示，最终以服务端返回的配额快照为准。
