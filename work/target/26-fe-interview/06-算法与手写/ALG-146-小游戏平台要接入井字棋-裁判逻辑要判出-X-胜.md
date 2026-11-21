---
title: [ALG-146] 小游戏平台要接入井字棋，裁判逻辑要判出 X 胜、O 胜、平局、进行中四种状态。如何实现？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-146：小游戏平台要接入井字棋，裁判逻辑要判出 X 胜、O 胜、平局、进行中四种状态。如何实现？
**答**：8 条连线（3 行 3 列 2 对角线）统一收进数组，任一连线三子相同即该方胜；否则看棋盘是否下满——满且无胜者为平局，否则进行中。O(1)（8 条线 × 3 格固定）。

```javascript
function judge(board) { // board: 3x3，元素 'X' / 'O' / null
  const lines = [];
  for (let i = 0; i < 3; i++) {
    lines.push([board[i][0], board[i][1], board[i][2]]); // 行
    lines.push([board[0][i], board[1][i], board[2][i]]); // 列
  }
  lines.push([board[0][0], board[1][1], board[2][2]]);   // 主对角
  lines.push([board[0][2], board[1][1], board[2][0]]);   // 副对角
  for (const [a, b, c] of lines) {
    if (a && a === b && a === c) return a;               // 'X' 或 'O' 胜
  }
  return board.flat().every(Boolean) ? 'draw' : 'pending';
}
// judge([['X','O','X'],['O','X','O'],['O','X','X']]) => 'X'
```
