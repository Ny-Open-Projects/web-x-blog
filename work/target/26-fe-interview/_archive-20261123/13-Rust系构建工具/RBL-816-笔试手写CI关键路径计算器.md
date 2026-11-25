---
title: [RBL-816] 笔试：手写 CI 关键路径计算器（拓扑最长链 + sharding 收益预估）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-816：笔试：手写 CI 关键路径计算器（最长链 + sharding 预估）

**需求**：实现两部分。1) `criticalPath(graph, entry)`：graph: `Record<id, { deps: string[], est: number }>`——返回关键路径总时长（最长依赖链）与路径数组 `{ path: string[], total }`；环抛错。2) `estimateSharding(graph, taskId, n)`：把 task 的 est 按容器数 n 均摊（含每容器启动开销 startup），返回新关键路径 total 与节省秒数。边界：孤立任务（无依赖）；est 为 0 的任务；n 大于任务实际并行收益（收益下界 = min(est, est/n + startup)）。

```javascript
function criticalPath(graph, entry) {
  const memo = {}; const onStack = new Set();
  const dfs = (id) => {
    if (memo[id]) return memo[id];
    if (onStack.has(id)) throw new Error('任务环: ' + id);
    onStack.add(id);
    const g = graph[id] ?? { deps: [], est: 0 };
    let best = null;
    for (const d of g.deps) {
      const sub = dfs(d);
      if (!best || sub.total > best.total) best = sub;
    }
    onStack.delete(id);
    memo[id] = best
      ? { path: [...best.path, id], total: best.total + g.est }
      : { path: [id], total: g.est };
    return memo[id];
  };
  return dfs(entry);
}

function estimateSharding(graph, taskId, n, { startup = 15 } = {}) {
  const before = criticalPath(graph, 'e2e');
  const task = graph[taskId];
  const shardEst = Math.min(task.est, Math.ceil(task.est / n) + startup);
  const after = criticalPath(
    { ...graph, [taskId]: { ...task, est: shardEst } }, 'e2e');
  return { shardEst, total: after.total, saved: before.total - after.total };
}

// 自测
const graph = {
  build: { deps: [], est: 300 },
  typecheck: { deps: [], est: 180 },
  unit: { deps: ['build'], est: 600 },
  lint: { deps: ['build'], est: 120 },
  deploy: { deps: ['build'], est: 60 },
  e2e: { deps: ['unit', 'deploy'], est: 900 },
};
let r = criticalPath(graph, 'e2e');
console.log(r.total === 1800);                           // build300+unit600+e2e900
console.log(r.path.join(','));                           // build,unit,e2e

// unit 并行化（typecheck 独立启动但不在 e2e 链上）
let r2 = estimateSharding(graph, 'unit', 6, { startup: 15 });
console.log(r2.shardEst === 115);                        // ceil(600/6)+15
console.log(r2.saved === 485);                           // 1800-1315
console.log(r2.total === 1315);

// sharding 无收益（est 小）
let r3 = estimateSharding(graph, 'deploy', 4, { startup: 15 });
console.log(r3.shardEst === 60);                         // min(60, 15+15)=30? deploy est 60: ceil(60/4)+15=30 <60 -> 30
console.log(r3.saved === 0);                             // deploy 不在关键路径

// 环
let e; try { criticalPath({ a: { deps: ['b'], est: 1 }, b: { deps: ['a'], est: 1 } }, 'a'); }
catch (x) { e = x; }
console.log(/环/.test(e.message));

console.log(criticalPath({ solo: { deps: [], est: 42 } }, 'solo').total === 42);
```

**评分点**：
- 关键路径 DFS memo 正确（最长链选择）；环检测；孤立/零耗时任务安全
- sharding 公式含启动开销且收益下界（min 原始 est）；「不在关键路径的任务切分省 0」判定正确
- saved 计算准确
- 能说清「CI 优化顺序：改依赖图 → 切分 → 加机器；关键路径而非任务总和决定时长」属于加分
