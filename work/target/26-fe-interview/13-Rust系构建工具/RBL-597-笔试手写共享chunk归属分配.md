---
title: [RBL-597] 笔试：手写共享 chunk 归属分配（引用计数 + 尺寸带宽校验）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-597：笔试：手写共享 chunk 归属分配（引用计数 + 尺寸带宽校验）

**答**：实现 `splitChunks(entries, modules, opts)`。entries: `{ id, closure: string[] }`（闭包含模块尺寸，尺寸从 `modules` 取）。规则：1) 每个模块初始归属「引用它的 entry 闭包集合」；2) 被 ≥`minShared` 个 entry 引用且自身尺寸 ≥`minSize` 的模块 → 拆出独立 shared chunk；3) 被多个 entry 引用但尺寸 < `minSize` → 保留在每个 entry chunk（内联复制）；4) 同 entry chunk 总尺寸 > `maxChunkKB` 时按引用计数降序把模块移入共享池直至达标。返回 `Map<chunkId, modules[]>`。边界：单 entry；全模块都 < minSize；entries 为空。

```javascript
function splitChunks(entries, modules, opts) {
  const { minShared = 2, minSize = 30, maxChunkKB = 200 } = opts ?? {};
  const owner = new Map();                               // module -> Set(entryIds)
  for (const e of entries)
    for (const m of e.closure)
      if (!owner.has(m)) owner.set(m, new Set());
      // 同一 entry 闭包内重复模块去重
  for (const e of entries)
    for (const m of e.closure) owner.get(m).add(e.id);

  const chunks = new Map();
  const sharedPool = [];

  for (const [m, refs] of owner) {
    const size = modules.get(m)?.size ?? 0;
    if (entries.length === 0) return chunks;
    if (refs.size >= minShared && size >= minSize) sharedPool.push({ m, refs, size });
    else if (refs.size >= minShared) {                   // 小模块：内联进每个引用 entry
      for (const e of refs) pushChunk(chunks, `entry-${e}`, m);
    } else {
      for (const e of refs) pushChunk(chunks, `entry-${e}`, m);
    }
  }
  if (sharedPool.length) chunks.set('shared', sharedPool.map(s => s.m));

  // 带宽校验：超重 entry chunk 按引用计数降序移出模块进共享池
  for (const e of entries) {
    let list = chunks.get(`entry-${e.id}`) || [];
    const total = () => list.reduce((s, m) => s + (modules.get(m)?.size ?? 0), 0);
    if (total() > maxChunkKB) {
      const movable = [...list].sort((a, b) =>
        (owner.get(b).size - owner.get(a).size) || (modules.get(b)?.size ?? 0) - (modules.get(a)?.size ?? 0));
      for (const m of movable) {
        if (total() <= maxChunkKB) break;
        list = list.filter(x => x !== m); chunks.get('shared').push(m);
      }
      chunks.set(`entry-${e.id}`, list);
    }
  }
  return chunks;
}
const pushChunk = (chunks, id, m) => (chunks.get(id) || chunks.set(id, []).get(id)).push(m);

// 自测
const modules = new Map([
  ['a', { size: 150 }], ['b', { size: 40 }], ['c', { size: 10 }],
  ['d', { size: 5 }], ['big1', { size: 90 }], ['big2', { size: 80 }],
]);
const entries = [
  { id: 'home', closure: ['a', 'c', 'd', 'big1'] },
  { id: 'shop', closure: ['a', 'b', 'big2', 'big1'] },
];
const out = splitChunks(entries, modules, { minShared: 2, minSize: 30, maxChunkKB: 200 });
// 断言：
// out.get('shared') 含 'a'（150≥30 且被 2 entry 引用）与 'big1'（被 2 引用）；
// 'c'/'d'（<30）内联进 entry-home；'b' 内联进 entry-shop；
// home 超 200KB 时（150 已移共享后 10+5+90=105 不超——自校验打印）
console.log([...out.entries()].map(([k, v]) => `${k}: ${v.sort().join(',')}`));
```

**评分点**：
- 归属判定三级正确：shared 拆出 / 小模块内联复制 / 单引用留在 entry
- minShared 与 minSize 双条件缺一不可（只有尺寸不够或只有引用不够都不拆）
- 超重再平衡按引用计数降序移出（优先移走「最能被共享受益」的模块）
- 边界：单 entry 不拆 shared、空 entries 直接返回空 Map
