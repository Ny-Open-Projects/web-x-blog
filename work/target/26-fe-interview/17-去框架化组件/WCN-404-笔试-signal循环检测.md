---
title: [WCN-404] 笔试：给 signal 系统加循环检测。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-404：笔试：给 signal 系统加循环检测。
**答**：检测两类环：① 依赖环（computed A 依赖 B，B 依赖 A）② effect 自写环（effect 写自己读的信号导致无限重跑，> 100 次判循环）。输出环路径。

```javascript
function checkCycle(node, path = []) {
  if (path.includes(node)) {
    const start = path.indexOf(node);
    throw new Error(`响应式环：${[...path.slice(start), node].map(n => n.name).join('→')}`);
  }
  for (const d of node.deps) checkCycle(d, [...path, node]);
}
let last = null, runs = 0;
function effectGuard(e) {
  if (e === last && ++runs > 100) throw new Error(`effect 自写循环：${e.name}`);
  if (e !== last) runs = 0;
  last = e;
}

```

**评分点**：
- 依赖环：建边时 DFS 检测回边（带路径栈）。
- 自写环：计数器（同 effect 连续 run 次数）。
- 路径输出（A→B→A）可读。
- dev 模式开启/生产关闭（配置）。
