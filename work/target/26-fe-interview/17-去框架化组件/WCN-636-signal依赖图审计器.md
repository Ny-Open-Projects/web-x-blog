---
title: [WCN-636] 笔试：实现 signal 依赖图审计器（采集依赖边 + 找出「更新风暴」热点与孤立节点）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-636：笔试：实现 signal 依赖图审计器（采集依赖边 + 找出「更新风暴」热点与孤立节点）

**答**：
- 需求：实现 auditSignals()，返回 { edges, hotNodes, orphans }：edges 是依赖边，hotNodes 是 set 次数超阈值的节点，orphans 是无任何依赖的 signal（疑似泄漏或死代码）。
- 思路：全局 registry 记录节点与更新计数；effect 执行时记录 active 读取的边；审计时统计度数与阈值过滤。
- 边界：去重边；计数阈值可配；孤立定义要排除「刚创建未使用」的误报（提供 minAge 参数）。

```javascript
const registry = new Map();
let currentEffect = null;
const edges = [];
function tracked(name, value) {
  const node = { name, sets: 0, created: Date.now() };
  registry.set(name, node);
  return {
    get() { if (currentEffect) edges.push([currentEffect, name]); return value; },
    set(v) { if (v === value) return; value = v; node.sets++; notify(name); },
  };
}
function effectOf(name, fn) {
  const run = () => { currentEffect = name; fn(); currentEffect = null; };
  run(); return run;
}
function auditSignals({ maxSets = 10, minAgeMs = 1000 } = {}) {
  const now = Date.now();
  const deg = new Map();
  edges.forEach(([from, to]) => deg.set(to, (deg.get(to) || 0) + 1));
  const hot = [...registry.values()].filter(n => n.sets > maxSets).map(n => n.name);
  const orphans = [...registry.values()]
    .filter(n => now - n.created > minAgeMs && !deg.has(n.name) && n.sets === 0)
    .map(n => n.name);
  return { edges: [...new Set(edges.map(e => e.join('->')))], hotNodes: hot, orphans };
}
```

**评分点**：
- 依赖边在 get 时采集且去重（[effect, signal] 形式）。
- hotNodes 基于 set 次数阈值，能定位更新风暴。
- orphans 结合 minAge 排除新建误报，识别死 signal。
- 返回值结构化，可直接喂给可视化面板。
