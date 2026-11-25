---
title: [RBL-069] 笔试：手写 chunk 依赖闭合检测器（环检测 + 闭合修复）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-069：笔试：手写 chunk 依赖闭合检测器（环检测 + 闭合修复）
**答**：给定 chunk 划分 { chunkId: moduleIds[] } 与模块依赖图，实现 checkClosure：1) 找出跨 chunk 的模块依赖边；2) 判断 chunk 级是否有循环（chunk A→B→A）；3) 有环时输出「需要合并的 chunk 对」；4) 合并后重新校验直到无环；5) 返回最终 chunk 划分。

```javascript
function checkClosure(chunkOf, deps) { // chunkOf: Map<modId, chunkId>
  let chunks = new Map();               // chunkId -> Set<modId>
  for (const [m, c] of chunkOf) {
    if (!chunks.has(c)) chunks.set(c, new Set());
    chunks.get(c).add(m);
  }
  for (;;) {
    // 1) 建 chunk 级依赖图
    const cg = new Map();               // chunkId -> Set<依赖的 chunkId>
    for (const [c, mods] of chunks) cg.set(c, new Set());
    for (const [m, mods] of deps) {
      const from = chunkOf.get(m);
      for (const d of mods) {
        const to = chunkOf.get(d);
        if (to && to !== from) cg.get(from).add(to);
      }
    }
    // 2) DFS 找环
    const cycle = findCycle(cg);
    if (!cycle) break;
    // 3) 合并环上 chunk，重新校验
    const merged = cycle[0];
    for (const c of cycle.slice(1)) {
      for (const m of chunks.get(c)) chunkOf.set(m, merged);
      chunks.get(merged).addAll?.(chunks.get(c)); // 合并成员
      chunks.delete(c);
      for (const [m, cc] of chunkOf) if (cc === c) chunkOf.set(m, merged);
    }
  }
  return { chunkOf, chunks };
}

function findCycle(cg) {
  const color = new Map(); // 0白 1灰 2黑
  const stack = [];
  function dfs(c) {
    color.set(c, 1); stack.push(c);
    for (const next of cg.get(c) || []) {
      if (color.get(next) === 1)
        return stack.slice(stack.indexOf(next)).concat(next);
      if (!color.get(next) && dfs(next)) return true;
    }
    stack.pop(); color.set(c, 2);
  }
  for (const c of cg.keys()) if (!color.get(c) && dfs(c)) return stack.slice();
  return null;
}
module.exports = { checkClosure };
```
**评分点**：
- chunk 级依赖图构建（跨 chunk 边提取）。
- DFS 三色找环并输出环路径。
- 合并环上 chunk 后迭代重校验（循环直到无环）。
- 能讲出「为什么闭合」：chunk 间循环 import 在浏览器加载顺序下会 TDZ 报错。
