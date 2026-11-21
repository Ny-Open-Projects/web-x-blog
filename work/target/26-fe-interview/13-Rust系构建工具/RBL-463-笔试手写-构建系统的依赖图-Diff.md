---
title: [RBL-463] 笔试：手写依赖图 diff（两次构建的图变更）
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-463：手写依赖图 diff
**需求**：实现 `diffGraphs(prev, next)`：1) 节点 diff：新增/移除模块；2) 边 diff：新增/删除依赖边（import 变化的精确归因）；3) 变更影响传播：新增边影响「共享 chunk 划分」的预测（模块进入新 chunk 的风险提示）；4) 输出 { nodes: {added, removed}, edges: {added, removed}, riskNotes }；5) 归因到 commit（结合 git diff——哪个 commit 引入的边）；6) 大图性能（增量 diff：只对比受变更模块的子图——全图 diff 在 10k 模块上不可行）。

```javascript
export function diffGraphs(prev, next, gitBlame) {
  const addedNodes = [], removedNodes = [], addedEdges = [], removedEdges = [], riskNotes = []

  for (const [id, m] of next.modules)
    if (!prev.modules.has(id)) addedNodes.push({ id, size: m.size })
  for (const id of prev.modules.keys())
    if (!next.modules.has(id)) removedNodes.push(id)

  for (const [id, m] of next.modules) {
    const old = prev.modules.get(id)
    if (!old) continue
    for (const dep of m.imports)
      if (!old.imports.includes(dep)) {
        addedEdges.push({ from: id, to: dep })
        // 跨 chunk 新边 → chunk 划分风险
        if (next.chunkOf(id) !== next.chunkOf(dep))
          riskNotes.push({ type: 'cross-chunk-edge', edge: `${id}→${dep}`,
            risk: '可能导致 chunk 合并或循环依赖', commit: gitBlame?.[id]?.commit })
      }
    for (const dep of old.imports)
      if (!m.imports.includes(dep)) removedEdges.push({ from: id, to: dep })
  }

  return { nodes: { added: addedNodes, removed: removedNodes },
    edges: { added: addedEdges, removed: removedEdges }, riskNotes }
}
```
**评分点**：
- 节点与边双层 diff（边 diff 才能归因 import 变化）
- 跨 chunk 新边风险预测（图 diff 的价值是预测——不是记录）
- commit 归因（gitBlame 联动——变更到人）
- 大图性能诚实（增量子图 diff 策略——全图对比在规模化下不可行）
