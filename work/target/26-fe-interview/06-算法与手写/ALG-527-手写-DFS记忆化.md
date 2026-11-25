---
title: [ALG-527] 手写 DFS+记忆化：组件树渲染开销
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-527：手写 DFS+记忆化：组件树渲染开销

**答**：
- 题目：组件树每个节点有渲染成本（动态），缓存命中可跳过子树——求「指定缓存配置下最小总渲染成本」。树形 DP + 记忆化（DFS 返回子树最小成本）。
- 思路：dfs(node) = min(渲染自己+全部子树, 缓存该节点(缓存成本)+0)。记忆化按节点 id。
- 评分点：树形 DP 决策（缓存 vs 渲染）；记忆化；成本模型简化声明。

```javascript
function minRenderCost(tree, costs, cacheCost) {           // tree: {id, children}
  const memo = new Map();
  function dfs(node) {
    if (memo.has(node.id)) return memo.get(node.id);
    let full = costs[node.id] ?? 0;                        // 渲染自己
    for (const c of node.children ?? []) full += dfs(c);
    const cached = cacheCost[node.id] ?? Infinity;         // 缓存成本
    const ans = Math.min(full, cached);
    memo.set(node.id, ans);
    return ans;
  }
  return dfs(tree);
}
```
