---
title: [FRP-282] 笔试：手写完整 keyed diff（复用判定 + LIS 最少移动）
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-282：笔试：手写完整 keyed diff
**答**：实现 `diffChildren(oldChildren, newChildren, container)`：old/new 是 `{ key, text }` 数组（DOM 为文本节点模拟）；要求：key 匹配复用 DOM 节点；移动次数最少（LIS）；新增/删除正确；返回操作统计 { moves, adds, removes }。

```javascript
function diffChildren(oldC, newC, container) {
  const stats = { moves: 0, adds: 0, removes: 0 }
  const oldMap = new Map(oldC.map((c, i) => [c.key, { node: c, idx: i }]))
  const newKeys = new Set(newC.map(c => c.key))
  // 删除旧有新的没有
  oldC.forEach(c => { if (!newKeys.has(c.key)) { container.removeChild(c.el); stats.removes++ } })
  // 按 new 顺序排列复用节点：newIndex -> oldIndex 映射
  const seq = []
  newC.forEach(c => {
    const hit = oldMap.get(c.key)
    if (hit) { seq.push(hit.idx); c.el = hit.node.el }
    else { c.el = document.createTextNode(c.text); stats.adds++ }
  })
  const keep = lis(seq).indices.map(i => seq[i]) // 无需移动的 oldIndex 集合
  let lastPlaced = -Infinity // 简化：按新顺序逐个 place
  newC.forEach((c, i) => {
    if (!c.el) return
    const oldIdx = oldMap.get(c.key)?.idx
    if (oldIdx !== undefined && keep.includes(oldIdx) && oldIdx >= lastPlaced) { lastPlaced = oldIdx; return }
    container.insertBefore(c.el, newC[i + 1]?.el || null)
    if (oldIdx !== undefined) stats.moves++
  })
  return stats
}
```
**评分点**：
- key Map 复用判定 + 删除批处理。
- LIS 求出「无需移动」集合（核心）。
- insertBefore 的 anchor 用新顺序后继（锚点正确性）。
- 统计返回便于测试断言。
