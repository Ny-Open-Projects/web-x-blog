---
title: [FRP-299] 笔试：手写「VDOM 价值」量化对比实验
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-299：笔试：手写 VDOM 价值量化实验
**答**：设计实验量化「VDOM 的代价与价值」：场景 1000 行列表改 1 行。A 方案：直接 innerHTML 全量重建；B 方案：手写 VDOM + diff（只 patch 变化行）；C 方案：细粒度 signal 单点更新。输出三者耗时与 DOM 节点变更数（MutationObserver 计数）。

```javascript
function countMutations(container, fn) {
  let count = 0
  const ob = new MutationObserver(muts => { count += muts.reduce((s, m) => s + (m.addedNodes.length + m.removedNodes.length + m.attributeChanges || 1), 0) })
  ob.observe(container, { childList: true, attributes: true, subtree: true, characterData: true })
  fn()
  ob.disconnect()
  return count
}
async function experiment(container, rows) {
  const setA = () => { container.innerHTML = rows.map(renderRow).join('') }           // 全量重建
  const setB = () => { const tree = buildVDOM(rows); diff(prevTree, tree, container) } // VDOM diff
  const setC = () => { cellSignals[500].set('changed') }                               // 细粒度
  console.log('A:', await bench(() => countMutations(container, setA)))
  console.log('B:', await bench(() => countMutations(container, setB)))
  console.log('C:', await bench(() => countMutations(container, setC)))
}
```
**评分点**：
- MutationObserver 计 DOM 变更数（量化「操作数」维度）。
- 三方案代表「无优化/VDOM/细粒度」三档。
- 预期结论：A 最快但 DOM 变更最贵；B 一次脚本开销换 DOM 最小化；C 两项都最小。
- 能说出 VDOM 的价值 = 「用脚本换 DOM」，瓶颈转移而非消除。
