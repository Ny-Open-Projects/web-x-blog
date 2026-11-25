---
title: [WCN-555] Vue Vapor 的「block 树 + 稳定锚点」在列表重排时如何做到最小 DOM 移动？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-555：Vue Vapor 的「block 树 + 稳定锚点」在列表重排时如何做到最小 DOM 移动？

**答**：
- 结论：用 key 映射旧节点位置，求出新顺序对应的「最长递增子序列（LIS）」，LIS 内的节点不动，只移动其余。
- 稳定锚点（anchor 注释节点）标记 block 边界，插入/删除以锚点为参照，避免整体重排。
- LIS 用二分 + 前驱数组 O(n log n) 求解，是大列表 diff 的关键优化。
- 追问：无 key 的列表为什么退化？（答：只能按下标就地 patch，无法识别移动，DOM 操作增多且状态错位）

```javascript
function lis(indices) {
  const tails = [], prev = [];
  indices.forEach((v, i) => {
    let lo = 0, hi = tails.length;
    while (lo < hi) { const m = (lo + hi) >> 1; indices[tails[m]] < v ? lo = m + 1 : hi = m; }
    if (lo) prev[i] = tails[lo - 1]; tails[lo] = i;
  });
  let k = tails.at(-1), res = [];
  while (k != null) { res.unshift(indices[k]); k = prev[k]; }
  return res;
}
function reorder(oldKeys, newKeys) {
  const pos = new Map(oldKeys.map((k, i) => [k, i]));
  const keep = new Set(lis(newKeys.map(k => pos.get(k) ?? -1)));
  return newKeys.map((k, i) => ({ key: k, move: !keep.has(i) })); // move=false 即不动
}
```
