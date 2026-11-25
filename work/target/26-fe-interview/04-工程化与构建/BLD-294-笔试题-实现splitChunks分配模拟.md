---
title: [BLD-294] 笔试题——实现 chunk 分配模拟（共享模块提升）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## BLD-294：手写 chunk 分配

**需求与边界**：
- 需求：入口集 + 模块图 → chunk 分配——① 入口专属模块归入口 chunk；② 被多个入口共享的模块提升公共 chunk（minChunks 阈值，SCN-BLD-233）；③ chunk 图无环（提升后校验）；④ 共享 chunk 大小下限（太小不值得独立 chunk）。
- 边界：① 阈值参数化（minChunks/minSize）；② 提升后重新校验无环（提升可能制造环——把公共 chunk 提到被依赖方）；③ 输出分配报告（每 chunk 的模块数/体积估算）。

**答**：
```javascript
function assignChunks(entries, graph, { minChunks = 3, minSize = 20_000 } = {}) {
  const chunks = {};                                   // chunkName -> Set(module)
  // 1. 每入口先独立
  for (const e of entries) chunks[e] = new Set(closure(graph, e));
  // 2. 共享计数（每模块被几个入口包含）
  const counts = {};
  for (const [name, mods] of Object.entries(chunks))
    for (const m of mods) (counts[m] ??= { n: 0, entries: [] }).entries.push(name);
  Object.values(counts).forEach(c => (c.n = c.entries.length));
  // 3. 共享提升
  const shared = Object.entries(counts).filter(([m, c]) =>
    c.n >= minChunks && moduleSize(m) >= minSize);     // 阈值双重过滤
  const sharedChunk = new Set(shared.map(([m]) => m));
  chunks.shared = sharedChunk;
  for (const [name, mods] of Object.entries(chunks)) {
    if (name === 'shared') continue;
    sharedChunk.forEach(m => mods.delete(m));          // 从入口 chunk 移除
  }
  // 4. 无环校验（chunk 依赖 = chunk 内模块引用其他 chunk 的模块）
  const chunkDeps = buildChunkDeps(chunks, graph);
  assertNoCycle(chunkDeps);                            // 提升制造环 → 合并回退
  return { chunks: summarize(chunks), deps: chunkDeps };
}
```

**评分点**:
- 双重阈值（minChunks + minSize——SCN-BLD-233 平衡点）。
- 提升后无环校验（提升可能制造环——回退机制）。
- 共享计数正确（跨入口模块统计）。
- 分配报告输出（可度量）。
