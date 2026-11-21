---
title: [ALG-182] 前端实现一个简化 Excel 公式引擎：单元格值形如 `=B1+A1*2`，改一个格子要重算所有依赖它的格子，且循环引用要报错。如何设计？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-182：前端实现一个简化 Excel 公式引擎：单元格值形如 `=B1+A1*2`，改一个格子要重算所有依赖它的格子，且循环引用要报错。如何设计？
**答**：两阶段：① 依赖解析——用正则提取公式里的引用，构建"被依赖者 -> 依赖者"的依赖图与入度表；② 拓扑排序（Kahn 算法）——入度为 0 的格子先求值，求完把它依赖者的入度减一，减到 0 的入队。排序后仍有剩余格子说明存在循环引用，报错。求值时把引用替换为已算出的值再执行表达式（生产用安全表达式解析器，不用 eval）。建图 O(单元格数 × 引用数)，排序 O(V + E)。

```javascript
function evalExpr(expr, vars) { // 表达式求值：引用已替换成数值
  const js = expr.replace(/([A-Z]+\d+)/g, (_, k) => `(${vars[k] ?? 0})`);
  return Function('"use strict"', `return (${js})`)(); // 生产应换安全解析器
}
function evaluateSheet(cells) {
  // 1. 依赖解析：'=B1+A1*2' 提取引用建图
  const deps = {}, dependents = {}, indeg = {};
  for (const k of Object.keys(cells)) indeg[k] = 0;
  for (const [k, raw] of Object.entries(cells)) {
    deps[k] = typeof raw === 'string' && raw.startsWith('=')
      ? [...raw.matchAll(/([A-Z]+\d+)/g)].map(m => m[1]) : [];
    for (const d of deps[k]) (dependents[d] ||= []).push(k), indeg[k]++;
  }
  // 2. 拓扑排序 Kahn：入度 0 的先算
  const evaluated = {}, queue = Object.keys(indeg).filter(k => !indeg[k]);
  while (queue.length) {
    const k = queue.shift();
    const raw = cells[k];
    evaluated[k] = typeof raw === 'string' && raw.startsWith('=')
      ? evalExpr(raw.slice(1), evaluated)  // 引用的格子此刻都已求值
      : raw;
    for (const dep of dependents[k] || []) {
      if (--indeg[dep] === 0) queue.push(dep);
    }
  }
  if (Object.keys(evaluated).length < Object.keys(cells).length) {
    throw new Error('circular reference');  // 有格子没被求值 => 存在环
  }
  return evaluated;
}
```
