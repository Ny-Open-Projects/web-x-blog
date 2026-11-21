---
title: [ALG-093] 活动页要把互为"竞品"的推荐位分到 A/B 两组轮播（相邻不能同组，即图二染色/二分图判定）。如何用 BFS 染色判断是否可行分组？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-093：活动页要把互为"竞品"的推荐位分到 A/B 两组轮播（相邻不能同组，即图二染色/二分图判定）。如何用 BFS 染色判断是否可行分组？
**答**：二分图判定：任取未染色节点染成 1，BFS 扩散时邻居必须染相反颜色；发现邻居与自己同色则无法分成两组。图中每个连通分量都要处理。时间 O(V + E)，空间 O(V)。

```javascript
function isBipartite(graph) { // graph: 邻接表
  const color = new Array(graph.length).fill(0); // 0 未染 1/-1 两组
  for (let i = 0; i < graph.length; i++) {
    if (color[i]) continue;
    color[i] = 1;
    const queue = [i];
    while (queue.length) {
      const cur = queue.shift();
      for (const nb of graph[cur]) {
        if (color[nb] === color[cur]) return false; // 冲突
        if (!color[nb]) {
          color[nb] = -color[cur];
          queue.push(nb);
        }
      }
    }
  }
  return true;
}
```
