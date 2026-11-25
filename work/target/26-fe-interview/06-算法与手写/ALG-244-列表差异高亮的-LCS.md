---
title: [ALG-244] 版本对比：两次接口数据列表 diff 高亮（LCS 最长公共子序列定位增删改，O(n·m) DP）
date: 2026-11-19
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---
## ALG-244：版本对比：两次接口数据列表 diff 高亮（LCS 最长公共子序列定位增删改，O(n·m) DP）
**答**：配置发布页要求 diff 视图：旧列表 vs 新列表，标出新增/删除/移动（顺序变化）的项。按 id 匹配是"同项"，但顺序变化需要 LCS 定位公共子序列——不在 LCS 里的就是移动/增删。

**思路**：以"顺序"为比较维度做 LCS DP（比较项相等 = 同 id 同位置语义或纯 id）；回溯产出操作序列：match/skip；未匹配的按新旧索引判增/删/移。

```javascript
function listDiff(oldList, newList) {
  const n = oldList.length, m = newList.length;
  // LCS DP（比较 id 相等）
  const dp = Array.from({ length: n + 1 }, () => new Uint16Array(m + 1));
  for (let i = n - 1; i >= 0; i--)
    for (let j = m - 1; j >= 0; j--)
      dp[i][j] = oldList[i].id === newList[j].id ? dp[i + 1][j + 1] + 1 : Math.max(dp[i + 1][j], dp[i][j + 1]);
  // 回溯产出操作
  const ops = [];
  let i = 0, j = 0;
  while (i < n && j < m) {
    if (oldList[i].id === newList[j].id) {
      ops.push({ type: i === j ? 'keep' : 'move', id: oldList[i].id, from: i, to: j });
      i++; j++;
    } else if (dp[i + 1][j] >= dp[i][j + 1]) { ops.push({ type: 'remove', id: oldList[i].id, at: i }); i++; }
    else { ops.push({ type: 'add', id: newList[j].id, at: j }); j++; }
  }
  for (; i < n; i++) ops.push({ type: 'remove', id: oldList[i].id, at: i });
  for (; j < m; j++) ops.push({ type: 'add', id: newList[j].id, at: j });
  return ops;
}
// old: [A,B,C,D]  new: [A,C,B,D]
// => keep A, move C(1→2)? 实际输出：keep A, move B(1→2 方向)/move C … 以回溯为准，move 标注 from/to
// 复杂度：O(n·m) 时间，空间可用滚动数组省到 O(min(n,m))（回溯需完整表，或 Hirschberg 分治）
// 大列表优化：按 id 先建 Map 做 O(n+m) 粗 diff（只关心增删），顺序变化再对"共有 id 序列"做 LCS
```

**评分点**：
- LCS DP 与回溯产操作序列（keep/move/add/remove）正确。
- move 判定语义（同 id 不同位置）。
- 复杂度 O(n·m) 与空间优化意识。
- 大列表的"先按 id 建 Map 粗 diff、共有序列再 LCS"两阶段优化。
