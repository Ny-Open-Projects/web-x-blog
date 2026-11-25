---
title: [ALG-436] 手写字符串 DP 编辑距离：搜索纠错
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-436：手写字符串 DP 编辑距离：搜索纠错

**答**：
- 题目：搜索框纠错——用户输入与词库词的编辑距离（插入/删除/替换代价 1）≤ 2 时给出建议。DP 经典：dp[i][j] = a 前 i 与 b 前 j 的最小编辑距离。
- 思路：转移：相等 dp[i-1][j-1]；否则 1 + min(删/插/换)。空间优化滚动数组 O(min(m,n))。词库量大时用「带编辑距离的 Trie 剪枝」（限界：当前距离 + 剩余长度差 > 预算即剪）。
- 评分点：三种转移；滚动数组空间优化；词库规模大时 Trie 剪枝意识。

```javascript
function editDistance(a, b) {
  const m = a.length, n = b.length;
  let prev = Array.from({ length: n + 1 }, (_, j) => j);   // 滚动数组 O(n) 空间
  for (let i = 1; i <= m; i++) {
    const cur = [i];
    for (let j = 1; j <= n; j++) {
      cur[j] = a[i - 1] === b[j - 1] ? prev[j - 1]
        : 1 + Math.min(prev[j], cur[j - 1], prev[j - 1]);  // 删/插/换
    }
    prev = cur;
  }
  return prev[n];
}
function suggest(input, dict, { maxDist = 2 } = {}) {      // 搜索纠错
  return dict
    .map(w => ({ w, d: editDistance(input, w) }))
    .filter(x => x.d <= maxDist)
    .sort((a, b) => a.d - b.d)
    .slice(0, 5);
}
// 词库大时：Trie DFS 带距离限界剪枝，复杂度从 O(词库×m×n) 降到近似 O(词库前缀数)
```
