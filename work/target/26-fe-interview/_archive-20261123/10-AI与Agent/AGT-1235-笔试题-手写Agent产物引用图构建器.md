---
title: [1235] 笔试手写：实现产物引用关系的图构建与悬空检测
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, 多Agent]
type: 笔试题
---

## 1235：笔试手写：实现产物引用关系的图构建与悬空检测

**需求**：实现 buildGraph(artifacts, refs)：artifacts 为 { id }[]，refs 为 { from: 产物id, to: uri }[]（uri 形如 art://task/id?v=n）。构建 { nodes, edges }；悬空检测：to 的 id 不在 artifacts 中记 dangling；循环检测（引用环）给出环路径。

```js
function buildGraph(artifacts, refs) {
  const ids = new Set(artifacts.map(a => a.id));
  const edges = [], dangling = [];
  for (const r of refs) {
    const toId = r.to.split('/')[2]?.split('?')[0];   // art://task/id?v=n
    if (!ids.has(toId)) { dangling.push(r); continue; }
    edges.push([r.from, toId]);
  }
  // 环检测（DFS 三色）
  const adj = {};
  edges.forEach(([a, b]) => (adj[a] ??= []).push(b));
  const color = {}, path = [];
  let cycle = null;
  function dfs(n) {
    if (cycle) return;
    color[n] = 1; path.push(n);
    for (const m of adj[n] || []) {
      if (color[m] === 1) { cycle = [...path.slice(path.indexOf(m)), m]; return; }
      if (!color[m]) dfs(m);
    }
    color[n] = 2; path.pop();
  }
  for (const id of ids) { if (!color[id] && !cycle) dfs(id); }
  return { nodes: [...ids], edges, dangling, cycle };
}
const arts = [{ id: 'a1' }, { id: 'a2' }];
const refs = [
  { from: 'a1', to: 'art://t/a2?v=1' },
  { from: 'a2', to: 'art://t/a9?v=1' },   // 悬空
];
console.log(buildGraph(arts, refs).dangling.length);  // 1
```

**评分点**：
- URI 解析提取目标产物 id（版本段剥离）
- 悬空引用检测（引用失效的前兆——生命周期治理输入）
- 环检测（DFS 三色）与环路径
- 能讨论：引用图与垃圾回收（引用计数归零清理）、版本不匹配的额外校验

