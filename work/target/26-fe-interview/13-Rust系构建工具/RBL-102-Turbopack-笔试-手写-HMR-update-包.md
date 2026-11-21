---
title: [RBL-102] 笔试：手写 HMR update 包生成器（增量产物 + accept 链）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-102：笔试：手写 HMR update 包生成器（增量产物 + accept 链）
**题目**：实现 buildUpdate(changedModules, graph)：1) 找出每个变更模块沿依赖引用链向上传播的所有受影响模块；2) 判断根（无人引用的受影响模块）作为 update 入口；3) 生成 update 包：{ changed, affected, entry, hot }——hot 为 true 仅当根模块声明了 accept（源码含 module.hot.accept 或 import.meta.hot.accept）；4) 无 accept 的根 → hot: false（提示整页刷新）；5) 循环依赖不造成死循环。

```javascript
function buildUpdate(changedModules, graph) { // graph: Map<mod, {importers:Set, accepts:boolean}>
  const affected = new Set(changedModules);
  const roots = [];
  const queue = [...changedModules];

  while (queue.length) {
    const m = queue.pop();
    let hasImporter = false;
    for (const imp of graph.get(m)?.importers || []) {
      if (!affected.has(imp)) { affected.add(imp); queue.push(imp); }
      hasImporter = true;
    }
    if (!hasImporter) roots.push(m);           // 无人引用 → update 根
  }

  // 循环依赖下的根判定补充：在环中且环外无 importer 的也算根
  if (!roots.length) {
    for (const m of affected)
      if ([...graph.get(m).importers].every(i => affected.has(i))) roots.push(m);
  }

  const hot = roots.length > 0 && roots.every(r => graph.get(r).accepts);
  return {
    changed: changedModules,
    affected: [...affected],
    entry: roots,
    hot,                                       // false → 客户端应整页刷新
  };
}
module.exports = { buildUpdate };

// 场景：改 Leaf.tsx → App.tsx accept → { entry:['App.tsx'], hot:true }
//      改 utils.ts 但无人 accept → hot:false → 整页刷新
```
**评分点**：
- 沿 importers 反向传播受影响集（方向正确）。
- 根判定：无 importer 或环上无外部 importer（循环依赖处理，易漏）。
- hot 语义：根模块 accept 声明才可热替换，否则刷新——与 webpack HMR 协议对齐。
- affected/changed 区分（变更 vs 波及）。
- 能讲出浏览器侧应用顺序：按 entry 逐个 apply，失败降级 reload。
