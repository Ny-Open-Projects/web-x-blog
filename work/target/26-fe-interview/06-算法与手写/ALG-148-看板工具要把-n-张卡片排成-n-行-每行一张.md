---
title: [ALG-148] 看板工具要把 n 张卡片排成 n 行，每行一张，要求任意两张不同列、不同对角线（N 皇后约束），给出所有合法排布的思路与代码？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-148：看板工具要把 n 张卡片排成 n 行，每行一张，要求任意两张不同列、不同对角线（N 皇后约束），给出所有合法排布的思路与代码？
**答**：回溯 + 集合剪枝：逐行放置，用三个 Set 分别记录已占用的列、主对角线（row - col 为定值）、副对角线（row + col 为定值）；放置前 O(1) 查集合剪枝，递归返回时撤销（回溯模板）。最坏 O(n!)，剪枝后实际可行解极少。

```javascript
function solveNQueens(n) {
  const cols = new Set(), diag1 = new Set(), diag2 = new Set();
  const res = [], path = [];
  function backtrack(row) {
    if (row === n) return res.push([...path]); // n 行放满，收集解
    for (let col = 0; col < n; col++) {
      // O(1) 剪枝：列、两方向对角线任一冲突即跳过
      if (cols.has(col) || diag1.has(row - col) || diag2.has(row + col)) continue;
      cols.add(col); diag1.add(row - col); diag2.add(row + col);
      path.push(col);
      backtrack(row + 1);
      // 回溯：撤销选择
      cols.delete(col); diag1.delete(row - col); diag2.delete(row + col);
      path.pop();
    }
  }
  backtrack(0);
  return res; // res[i] 是每行卡片所在的列号数组
}
// solveNQueens(4) => [[1,3,0,2],[2,0,3,1]]
```

## 十六、大数据量处理

> ALG-149 ~ ALG-157：十万级数据的渲染分片、Worker 分治、流式解析、时间轮、堆取 TopK、基数估算、布隆过滤器、游标分页、指数退避。
