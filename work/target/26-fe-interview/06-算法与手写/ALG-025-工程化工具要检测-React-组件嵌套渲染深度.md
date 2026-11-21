---
title: [ALG-025] 工程化工具要检测 React 组件嵌套渲染深度，超过阈值（如 30 层）告警。组件树抽象为多叉树后如何求最大深度？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-025：工程化工具要检测 React 组件嵌套渲染深度，超过阈值（如 30 层）告警。组件树抽象为多叉树后如何求最大深度？
**答**：多叉树最大深度 = 子树最大深度 + 1，DFS 后序合并即可；也可用 BFS 数层数（层数即深度），BFS 版不会因超深链式结构爆栈，生产建议用迭代。时间 O(n)，空间递归 O(h) / 迭代 O(w)。

```javascript
function maxDepth(node) {
  if (!node) return 0;
  let max = 0;
  for (const child of node.children || []) {
    max = Math.max(max, maxDepth(child));
  }
  return max + 1; // 自身这一层
}
// BFS 版（防爆栈）：
// let depth = 0; 队列初始 [root]; 每处理完一层 depth++;
```
