---
title: [ALG-081] 文件 diff 工具要把两个版本按行比较，找出最长公共行序列（LCS），再据此标记新增/删除行。如何实现 LCS？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-081：文件 diff 工具要把两个版本按行比较，找出最长公共行序列（LCS），再据此标记新增/删除行。如何实现 LCS？
**答**：`dp[i][j]`：行相等则 `dp[i-1][j-1] + 1`，否则取"跳过 a 行或跳过 b 行"的较大者。求出长度后按 dp 表回溯即可还原公共序列，diff 工具再对非公共部分标注增删（Myers diff 的思想基础）。时间 O(m × n)，空间 O(m × n)。

```javascript
function lcs(a, b) {
  const m = a.length, n = b.length;
  const dp = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      dp[i][j] = a[i - 1] === b[j - 1]
        ? dp[i - 1][j - 1] + 1
        : Math.max(dp[i - 1][j], dp[i][j - 1]);
    }
  }
  return dp[m][n]; // 回溯 dp 表可还原具体公共行序列
}
```
