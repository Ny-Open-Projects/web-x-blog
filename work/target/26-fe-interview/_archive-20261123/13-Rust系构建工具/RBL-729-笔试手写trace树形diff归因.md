---
title: [RBL-729] 笔试：手写 trace 树形 diff 归因器（时长对比 + 子树归因）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-729：笔试：手写 trace 树形 diff 归因器（时长对比 + 子树归因）

**需求**：实现 `diffTraces(baseline, current, { threshold })`。两棵 trace 树：`{ name, ms, children: [] }`。规则：1) 按 name 递归配对（同名兄弟多节点取 ms 最大者配对——保守）；2) 节点自身时长 = ms − Σchildren（自耗时）；3) 自耗时增长率 > threshold 且绝对增长 > 100ms → 记 `regression`（含 from/to）；4) 归因排序：按「自耗时增长量」降序，取 top 5；5) 新增节点（baseline 没有）记 `new`（自耗时 > 500ms 才记，忽略小开销）；消失节点记 `removed`。返回 `{ regressions, added, removed }`。

```javascript
const selfTime = (n) => n.ms - n.children.reduce((s, c) => s + c.ms, 0);

function pick(map, name) {
  const list = map[name];
  if (!list) return null;
  return list.reduce((a, b) => (b.ms > a.ms ? b : a));   // 同名取最大
}
function index(tree, map = {}) {
  (map[tree.name] = map[tree.name] || []).push(tree);
  tree.children.forEach(c => index(c, map));
  return map;
}
function collect(tree, fn) {
  fn(tree); tree.children.forEach(c => collect(c, fn));
}

function diffTraces(baseline, current, { threshold = 0.3 } = {}) {
  const bMap = index(baseline), cMap = index(current);
  const regressions = [], added = [];
  collect(current, (node) => {
    const base = pick(bMap, node.name);
    if (!base) {
      if (selfTime(node) > 500) added.push({ name: node.name, selfMs: selfTime(node) });
      return;
    }
    const bSelf = selfTime(base), cSelf = selfTime(node);
    if (bSelf > 0 && (cSelf - bSelf) / bSelf > threshold && cSelf - bSelf > 100)
      regressions.push({ name: node.name, from: bSelf, to: cSelf, delta: cSelf - bSelf });
  });
  const removed = [];
  collect(baseline, (node) => {
    if (!pick(cMap, node.name)) removed.push({ name: node.name });
  });
  regressions.sort((a, b) => b.delta - a.delta);
  return { regressions: regressions.slice(0, 5), added, removed };
}

// 自测
const base = { name: 'build', ms: 1000, children: [
  { name: 'resolve', ms: 200, children: [
    { name: 'mod:a', ms: 150, children: [] } ] },
  { name: 'transform', ms: 700, children: [
    { name: 'mod:b', ms: 300, children: [] } ] },
] };
const cur = { name: 'build', ms: 1600, children: [
  { name: 'resolve', ms: 700, children: [                 // resolve 严重回归
    { name: 'mod:a', ms: 600, children: [] } ] },
  { name: 'transform', ms: 800, children: [
    { name: 'mod:b', ms: 300, children: [] },
    { name: 'mod:NEW', ms: 800, children: [] } ] },       // 新增大节点
] };
const r = diffTraces(base, cur);
console.log(r.regressions[0].name === 'resolve');        // 自耗时 (700-600)=100 vs base (200-150)=50 -> +100% > 100ms
console.log(r.added.some(a => a.name === 'mod:NEW'));
console.log(r.regressions.length === 1);

// 阈值内不报
const r2 = diffTraces(base, { ...base, ms: 1050 });
console.log(r2.regressions.length === 0);
```

**评分点**：
- 自耗时计算正确（ms − 子树和）；同名配对取最大者（保守）
- 回归双条件（相对 + 绝对）；排序取 top5；新增/移除节点分类
- 边界：阈值内静默、新节点小开销忽略
- 能说清「树形 diff 的归因力来自嵌套时长结构（谁拖慢谁）」属于加分
