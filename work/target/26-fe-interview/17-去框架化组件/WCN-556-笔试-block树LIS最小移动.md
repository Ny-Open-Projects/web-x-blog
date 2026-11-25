---
title: [WCN-556] 笔试：实现 block 树锚点重排算法（基于 key 的最长递增子序列 LIS 最小移动）。
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-556：笔试：实现 block 树锚点重排算法（基于 key 的最长递增子序列 LIS 最小移动）。

**答**：
- 结论：先按 key 建立旧位置索引，把新顺序映射为旧索引序列，求 LIS 得到无需移动的节点集合，其余按序插入。
- 用锚点标记插入位置，移动用 insertBefore 参照锚点，保证稳定。
- 新增节点无旧索引（-1），删除节点不在新序列中，分别处理。
- 追问：如何度量「最小移动」是否正确？（答：移动次数 = n - LIS 长度，可作为断言）

```javascript
function getLIS(seq) {
  const tails = [], prev = Array(seq.length).fill(-1);
  seq.forEach((v, i) => {
    if (v < 0) return;                              // 新增节点不参与
    let lo = 0, hi = tails.length;
    while (lo < hi) { const m = (lo + hi) >> 1; seq[tails[m]] < v ? lo = m + 1 : hi = m; }
    if (lo > 0) prev[i] = tails[lo - 1]; tails[lo] = i;
  });
  const set = new Set(); let k = tails.at(-1);
  while (k != null) { set.add(k); k = prev[k]; }
  return set;
}
function minimalMoves(oldKeys, newKeys, anchor) {
  const idx = new Map(oldKeys.map((k, i) => [k, i]));
  const seq = newKeys.map(k => idx.get(k) ?? -1);
  const keep = getLIS(seq);
  let ref = anchor;
  const ops = [];
  for (let i = newKeys.length - 1; i >= 0; i--) {
    if (keep.has(i)) { ref = newKeys[i]; continue; }       // 不动，作为后续参照
    ops.push({ type: 'insertBefore', key: newKeys[i], ref });
  }
  return ops;                                             // 移动次数 = n - keep.size
}
```

**评分点**：
- key→旧位置索引映射
- LIS 求不动集合 O(n log n)
- 锚点 insertBefore 稳定插入
- 移动次数可断言
