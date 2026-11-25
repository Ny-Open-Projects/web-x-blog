---
title: [ALG-434] 手写 Trie+DFS 剪枝（单词搜索）：输入候选校验
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-434：手写 Trie+DFS 剪枝（单词搜索）：输入候选校验

**答**：
- 题目：输入法候选校验——确认用户输入序列能否拼出词库中的单词（字符可复用、四方向相邻）。棋盘单词搜索经典：Trie 预置词库 + DFS 剪枝。
- 思路：词库建 Trie；棋盘每格起 DFS，走 Trie 节点（不在 Trie 立即剪枝）；visited 标记防复用同格；命中词尾收集。
- 评分点：Trie 剪枝（无前缀即停）；visited 恢复现场；与暴力全搜的复杂度差。

```javascript
function findWords(board, words) {                         // 单词搜索（Trie 剪枝）
  const trie = { children: {}, word: null };
  for (const w of words) {
    let node = trie;
    for (const c of w) node = node.children[c] ??= { children: {}, word: null };
    node.word = w;
  }
  const result = new Set();
  const dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]];
  function dfs(i, j, node, visited) {
    const c = board[i][j];
    const next = node.children[c];
    if (!next) return;                                     // Trie 剪枝：无此前缀
    if (next.word) result.add(next.word);
    visited.add(i + ',' + j);
    for (const [dx, dy] of dirs) {
      const ni = i + dx, nj = j + dy;
      if (ni >= 0 && nj >= 0 && ni < board.length && nj < board[0].length
        && !visited.has(ni + ',' + nj))
        dfs(ni, nj, next, visited);
    }
    visited.delete(i + ',' + j);                           // 恢复现场
  }
  for (let i = 0; i < board.length; i++)
    for (let j = 0; j < board[0].length; j++) dfs(i, j, trie, new Set());
  return [...result];
}
```
