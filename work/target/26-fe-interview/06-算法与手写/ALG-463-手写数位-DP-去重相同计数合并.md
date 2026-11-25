---
title: [ALG-463] 手写数位 DP 去重（相同计数合并）：统计优化
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-463：手写数位 DP 去重（相同计数合并）：统计优化

**答**：
- 题目：状态数爆炸场景（多位 + 多约束）——相同「(状态, tight=false)」的记忆化本身就是去重；进一步：对「计数相同的分支」批量合并（矩阵快速幂思想：转移矩阵幂）。
- 思路：把「逐位转移」抽象为转移矩阵（状态 × 状态），区间计数 = 矩阵幂。状态少（<20）时矩阵快速幂 O(状态³ × 位数 × log)。
- 评分点：转移矩阵抽象；矩阵快速幂替代逐位 DFS；状态数与矩阵法的适用边界。

```javascript
function matrixCount(digits, states, transitions) {        // 转移矩阵 + 快速幂
  // states: 状态数；transitions: transitions[state][d] = 下一状态
  const M = buildMatrix(states, transitions);               // 字符集 → 转移矩阵
  let result = vectorE1(states);                            // 初始状态向量
  for (const d of digits) {                                 // 逐位（tight 简化）
    result = matVec(M, result, d);
  }
  return sum(result);
}
function matVec(M, v, d) {
  return M.map(row => row.reduce((s, m, i) => s + m[d]?.[i] * v[i], 0));
}
// 矩阵快速幂版：固定长度计数 = M^len × 初始向量，O(k³ log len)
// 适用：状态数 k 小（<30）且只需计数的批量场景（如统计所有 k 位合法数）
```
