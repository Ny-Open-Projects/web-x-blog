---
title: [BLD-292] 笔试题——实现依赖图反向查询（why 接口）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## BLD-292：手写 why 接口

**需求与边界**：
- 需求：给定模块依赖图（正向边），实现 `why(target)` 返回所有「入口→target」的引用链（最短优先，SCN-BLD-277），并标注链类型（direct/transitive）。
- 边界：① BFS 保证最短链优先；② 环图不死循环（visited per-path）；③ 链条数上限（防止爆炸——大仓一条链可能上万条）；④ 输出带分类标注。

**答**：
```javascript
function why(graph, entries, target, { maxChains = 20 } = {}) {
  const chains = [];
  const queue = entries.map(e => ({ node: e, path: [e] }));
  const visitedDepth = new Map();                      // 记录最短到达深度（剪枝）
  while (queue.length && chains.length < maxChains) {
    const { node, path } = queue.shift();
    if (node === target) {
      chains.push({ chain: path, type: path.length <= 2 ? 'direct' : 'transitive' });
      continue;                                        // 继续找其他链
    }
    // 剪枝：已用更短路径到达过该节点则跳过（防爆炸 + 去冗余）
    if ((visitedDepth.get(node) ?? Infinity) < path.length) continue;
    visitedDepth.set(node, path.length);
    for (const dep of graph[node] ?? [])
      if (!path.includes(dep))                         // 路径内环防御
        queue.push({ node: dep, path: [...path, dep] });
  }
  return { chains, truncated: chains.length >= maxChains };
}
// why('lodash') → [{ chain: ['app','dashboard','lodash'], type: 'transitive' }, ...]
```

**评分点**:
- BFS 最短链优先（最短引用链最有诊断价值）。
- 剪枝（更短路径已到达则跳过——防大仓链爆炸）+ 路径内环防御。
- 链类型标注（direct/transitive——SCN-BLD-277 修复映射）。
- maxChains 截断语义（truncated 提示）。
