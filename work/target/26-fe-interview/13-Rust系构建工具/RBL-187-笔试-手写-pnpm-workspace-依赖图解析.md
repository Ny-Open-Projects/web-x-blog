---
title: [RBL-187] 笔试：手写 pnpm-workspace 依赖图解析器
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-187：笔试：手写 pnpm-workspace 依赖图解析器

**答**：写 workspace-graph.mjs：1) 读 pnpm-workspace.yaml 的 packages glob（如 ['apps/*', 'packages/*']）与各包 package.json；2) 构建内部依赖图：deps/devDeps/peerDeps 里名字匹配 workspace 内包的算内部依赖，其他为外部；3) 检测循环依赖并输出环路径；4) 提供 dependents(name)：谁（含传递）依赖该包；5) 输出：节点数、边数、无上游的根包列表（可独立发版的候选）。

```javascript
// workspace-graph.mjs
import { readFileSync, existsSync } from 'node:fs';
import { parse } from 'yaml';
import { globSync } from 'node:fs'; // 简化：用 glob 库或 readdir 展开均可

export function buildGraph(root = '.') {
  const ws = parse(readFileSync(`${root}/pnpm-workspace.yaml`, 'utf8'));
  const pkgs = new Map();                       // name -> { dir, manifest }
  for (const g of ws.packages ?? []) {
    for (const dir of globSync(`${root}/${g}/package.json`)) {
      const m = JSON.parse(readFileSync(dir, 'utf8'));
      if (m.name) pkgs.set(m.name, { dir: dir.replace('/package.json', ''), manifest: m });
    }
  }
  const edges = new Map();                      // name -> Set<内部依赖>
  for (const [name, { manifest }] of pkgs) {
    const all = { ...manifest.dependencies, ...manifest.devDependencies, ...manifest.peerDependencies };
    edges.set(name, new Set(Object.keys(all ?? {}).filter(k => pkgs.has(k))));
  }
  // 环检测（DFS 三色标记 + 回溯路径）
  const WHITE = 0, GRAY = 1, BLACK = 2, color = new Map(), stack = [], cycles = [];
  function dfs(n) {
    color.set(n, GRAY); stack.push(n);
    for (const d of edges.get(n) ?? []) {
      if ((color.get(d) ?? WHITE) === GRAY)
        cycles.push([...stack.slice(stack.indexOf(d)), d].join(' -> '));
      else if (color.get(d) === WHITE) dfs(d);
    }
    stack.pop(); color.set(n, BLACK);
  }
  for (const n of pkgs.keys()) if (!color.get(n)) dfs(n);

  const dependents = (target) => {              // 传递依赖者（下游闭包）
    const hit = new Set(), q = [];
    for (const [n, ds] of edges) if (ds.has(target)) { hit.add(n); q.push(n); }
    while (q.length) {
      const x = q.shift();
      for (const [n, ds] of edges) if (ds.has(x) && !hit.has(n)) { hit.add(n); q.push(n); }
    }
    return [...hit];
  };
  const roots = [...pkgs.keys()].filter(n => ![...edges.values()].some(s => s.has(n)));
  return { size: pkgs.size, edges: [...edges.values()].reduce((a, s) => a + s.size, 0),
           cycles, dependents, roots, names: [...pkgs.keys()] };
}
```
**评分点**：
- 三类依赖字段都算（devDeps 也构成构建顺序约束）。
- DFS 灰色节点判环并输出环路径。
- dependents 是传递闭包（BFS 反向传播），非直接依赖。
- roots 概念正确（无内部上游 → 独立发版候选）。
- 能说明该图是 affected/拓扑调度/发版顺序的共同底座。
