---
title: [V3-043] Vue3 的 diff 算法（快速 diff）分为哪几步？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-043：Vue3 的 diff 算法（快速 diff）分为哪几步？
**答**：
- 第一步：预处理相同前缀与相同后缀，缩小乱序区间。
- 第二步：旧节点遍历完则新节点批量挂载；新节点遍历完则旧节点批量卸载。
- 第三步：乱序区间为新节点建 key -> index 映射，记录旧节点对应的新下标 source。
- 第四步：对 source 求最长递增子序列，LIS 内节点不动，其余倒序遍历做 move 或挂载，把 DOM 移动次数降到最少。

```javascript
// Vue3 快速 diff 算法核心步骤（示意）
function diffChildren(oldChildren, newChildren) {
  // 1. 预处理：从头同步相同前缀，从尾同步相同后缀
  let start = 0;
  let oldEnd = oldChildren.length - 1;
  let newEnd = newChildren.length - 1;
  while (
    start <= oldEnd &&
    start <= newEnd &&
    oldChildren[start].key === newChildren[start].key
  ) {
    start++;
  }
  while (
    oldEnd >= start &&
    newEnd >= start &&
    oldChildren[oldEnd].key === newChildren[newEnd].key
  ) {
    oldEnd--;
    newEnd--;
  }

  // 2. 旧节点遍历完：新区间全部是新增，直接挂载
  if (start > oldEnd && start <= newEnd) {
    // mountBatch(newChildren.slice(start, newEnd + 1))
  }
  // 3. 新节点遍历完：旧区间全部卸载
  else if (start > newEnd) {
    // unmountBatch(oldChildren.slice(start, oldEnd + 1))
  }
  // 4. 乱序区间：
  //    为新节点建立 key -> index 映射，记录每个旧节点在新序列中的下标 source
  //    对 source 求最长递增子序列 LIS，LIS 中的节点保持不动
  //    倒序遍历新节点：不在 LIS 的执行 move 或挂载
  //    这样能把 DOM 移动次数降到最少
}
```
