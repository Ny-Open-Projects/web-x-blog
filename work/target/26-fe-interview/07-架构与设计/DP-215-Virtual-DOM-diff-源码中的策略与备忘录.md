---
title: [DP-215] 源码识别：Virtual DOM diff 源码中的策略与备忘录？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-215：源码识别：Virtual DOM diff 源码中的策略与备忘录？
**答**：
- 策略模式：diff 的三个启发式都是"策略声明"——同层比较（不跨层）、同类型复用（不同类型重建）、key 标识（最长递增子序列 LIS 优化移动）。
- 备忘录：静态提升（hoistStatic）把不随 props 变化的节点提升为常量，patchFlag 标记动态部分——编译期 memo（Vue3 编译优化核心）。
- 命令模式：patch 产生的"操作序列"（insertBefore/moveBefore）是命令批量执行；Vue3 的移动操作基于 LIS 算最小移动集。
- 识别要点：React 的 lane/双缓冲 fiber 也是备忘录（当前树 vs 工作树快照），Vue3 是编译期备忘录——两条技术路线同模式。

```javascript
// Vue3 diff LIS 简化
function diffChildren(c1, c2) {
  let i = 0;
  while (i < c1.length && i < c2.length && sameType(c1[i], c2[i])) patch(c1[i], c2[i++]);  // 前缀
  while (i < c1.length && i < c2.length && sameType(c1[c1.length-1], c2[c2.length-1])) patch(c1[--c1.length-1+1], c2[--c2.length]);
  // 中段乱序：key → index 映射，求 c2 中需要移动的最小集合
  const keyToNew = new Map(c2.slice(i).map((v, j) => [v.key, j]));
  const oldIdx = c1.slice(i).map(v => keyToNew.get(v.key) ?? -1);
  const lis = longestIncreasingSubsequence(oldIdx);        // 最长递增子序列：不动的最大集合
  for (let j = oldIdx.length - 1, k = lis.length - 1; j >= 0; j--) {
    if (k >= 0 && lis[k] === j) k--;                        // LIS 内：不动（备忘复用）
    else insertBefore(c2[i + j], anchor);                   // 其余：最小移动命令
  }
}
```
