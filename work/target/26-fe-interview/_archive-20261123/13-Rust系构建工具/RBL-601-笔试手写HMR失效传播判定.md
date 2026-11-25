---
title: [RBL-601] 笔试：手写 HMR 失效传播判定（接受边界 + 环 + reload 兜底）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-601：笔试：手写 HMR 失效传播判定（接受边界 + 环 + reload 兜底）

**需求**：实现 `hmrPropagate(graph, changedId)`。graph: `{ imports: Map<id, id[]>, accepts: (parentId, depId) => boolean }`（imports 是模块的依赖，传播走反向）。返回 `{ stale: string[], actions: Array }`——actions 按传播结果给出：`{ type: 'accept', boundary, affected }` 或 `{ type: 'reload' }`。规则：1) 失效沿依赖反向边向上传播；2) 父模块 accept 该子模块时停止冒泡，记 accept（affected 为从 changed 到 boundary 的失效路径）；3) 到达 entry 仍未被接受 → reload；4) 同一模块重复到达只处理一次；5) 环路不产生重复失效但环上模块都计入 stale。

```javascript
function hmrPropagate(graph, changedId) {
  const stale = new Set([changedId]);
  const actions = [];
  const visited = new Set();                            // 传播去重

  function up(id, path) {
    const parents = [...graph.imports.entries()]
      .filter(([p, deps]) => deps.includes(id)).map(([p]) => p);
    for (const parent of parents) {
      if (path.includes(parent)) continue;              // 环保护：不沿环冒泡
      if (graph.accepts(parent, id)) {
        actions.push({ type: 'accept', boundary: parent, affected: [...path, id] });
        stale.add(parent);                              // 边界本身要重执行
        continue;                                       // 停止冒泡
      }
      stale.add(parent);
      if (parent === 'entry') {
        actions.push({ type: 'reload' });
        continue;
      }
      if (visited.has(parent + ':' + id)) continue;
      visited.add(parent + ':' + id);
      up(parent, [...path, parent]);
    }
  }
  up(changedId, [changedId]);
  return { stale: [...stale], actions };
}

// 自测
// app(entry) -> page -> Comp；app 接受 page，page 接受 Comp；lib 被 page 与 comp 引用
const graph = {
  imports: new Map([
    ['entry', ['page', 'lib']],
    ['page', ['Comp', 'lib']],
    ['Comp', ['lib']],
    ['lib', []],
  ]),
  accepts: (p, d) => (p === 'entry' && d === 'page') || (p === 'page' && d === 'Comp'),
};
// 1) Comp 失效：page 接受
let r = hmrPropagate(graph, 'Comp');
console.log(r.actions[0].type === 'accept' && r.actions[0].boundary === 'page');
console.log(r.stale.includes('Comp') && r.stale.includes('page'));

// 2) lib 失效：无 accept 路径到 entry
r = hmrPropagate(graph, 'lib');
console.log(r.actions.some(a => a.type === 'reload'));

// 3) 环：a <-> b，无 accept
const cyc = { imports: new Map([['entry', ['a']], ['a', ['b']], ['b', ['a']]]), accepts: () => false };
r = hmrPropagate(cyc, 'a');
console.log(r.actions.filter(x => x.type === 'reload').length >= 1 && r.stale.size >= 3);
```

**评分点**：
- 传播走反向边且遇到 accept 正确停止（affected 记录完整失效路径）
- reload 兜底判定正确（entry 未被接受）；多路径失效去重
- 环保护：不无限冒泡，环上模块计入 stale 不重复 accept
- 能说清「accept 边界本身也要重执行」与「路径 vs 闭包」的区分属于加分
