---
title: [ALG-528] 手写 BFS 分层：关系链路最短
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-528：手写 BFS 分层：关系链路最短

**答**：
- 题目：社交关系图找「两人间最短认识链路」（六度理论验证）。BFS 分层（层号即距离）。
- 思路：起点 BFS，队列按层推进；访问标记防重复；找到目标返回层数。
- 评分点：分层 BFS；访问标记；路径还原（父指针）。

```javascript
function shortestChain(graph, from, to) {                  // graph: Map<user, Set<friend>>
  const queue = [[from, 0]];
  const visited = new Set([from]);
  const parent = new Map();
  while (queue.length) {
    const [u, dist] = queue.shift();
    if (u === to) {                                        // 命中：还原路径
      const path = [u];
      let cur = u;
      while (parent.has(cur)) { cur = parent.get(cur); path.unshift(cur); }
      return { degree: dist, path };
    }
    for (const v of graph.get(u) ?? []) {
      if (visited.has(v)) continue;
      visited.add(v);
      parent.set(v, u);
      queue.push([v, dist + 1]);
    }
  }
  return null;                                             // 不连通
}
```
