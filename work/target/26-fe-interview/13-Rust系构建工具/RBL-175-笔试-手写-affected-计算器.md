---
title: [RBL-175] 笔试：手写 affected 计算器（变更文件 → 受影响包集合）
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-175：笔试：手写 affected 计算器（变更文件 → 受影响包集合）

**题目**：写 affected.js：1) 输入：包列表（每包含 root、name）、依赖关系（包名 → 依赖的本地包名数组）、变更文件列表；2) 把文件映射到所属包（按 root 前缀最长匹配）；3) 沿"谁依赖我"的反向边 BFS 求受影响闭包；4) 根目录公共文件（tsconfig.base.json、pnpm-lock.yaml）视为影响全部包；5) 输出受影响包名列表并按依赖序（拓扑）排列。

```javascript
// affected.js
function affected(pkgs, deps, changedFiles, rootFiles = ['pnpm-lock.yaml', 'tsconfig.base.json']) {
  const isGlobal = changedFiles.some(f => rootFiles.includes(f));
  const owners = [...pkgs].sort((a, b) => b.root.length - a.root.length); // 最长前缀优先
  const ownerOf = (f) => owners.find(p => f.startsWith(p.root + '/'))?.name;

  const changed = new Set(changedFiles.map(ownerOf).filter(Boolean));
  if (isGlobal) pkgs.forEach(p => changed.add(p.name));

  // 反向邻接表：rdeps[x] = 依赖 x 的包集合
  const rdeps = {};
  for (const p of pkgs) rdeps[p.name] ??= [];
  for (const [pkg, ds] of Object.entries(deps)) {
    rdeps[pkg] ??= [];
    for (const d of ds) (rdeps[d] ??= []).push(pkg);
  }
  const hit = new Set(changed);
  const queue = [...changed];
  while (queue.length) {                 // BFS 向下游传播
    const x = queue.shift();
    for (const y of rdeps[x] ?? []) if (!hit.has(y)) { hit.add(y); queue.push(y); }
  }
  // 拓扑排序输出（Kahn），保证 build 顺序可执行
  const out = [], indeg = new Map();
  for (const name of hit) indeg.set(name, (deps[name] ?? []).filter(d => hit.has(d)).length);
  let ready = [...hit].filter(n => indeg.get(n) === 0);
  while (ready.length) {
    const n = ready.pop(); out.push(n);
    for (const m of rdeps[n] ?? []) if (hit.has(m)) {
      indeg.set(m, indeg.get(m) - 1);
      if (indeg.get(m) === 0) ready.push(m);
    }
  }
  return out;
}
// 示例：apps/web -> packages/ui -> packages/utils
// changedFiles=['packages/utils/src/a.ts'] ⇒ ['utils','ui','web']
module.exports = { affected };
```
**评分点**：
- 文件→包映射用最长前缀匹配（嵌套包正确）。
- 反向边 BFS 是下游闭包（改 utils 影响依赖它的，而不是它依赖的）。
- 根目录公共文件全局失效特判。
- 输出按拓扑序可直接喂给流水线。
- 未声明依赖的包不误伤（图外包保持独立）。
