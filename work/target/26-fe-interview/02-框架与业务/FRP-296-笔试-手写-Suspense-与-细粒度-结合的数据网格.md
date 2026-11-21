---
title: [FRP-296] 笔试：手写细粒度数据网格（列/单元格级订阅）
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-296：笔试：手写细粒度数据网格
**题**：10×10 网格，cell(i,j) 是独立 signal；实现 renderGrid：每格绑定自己的信号 effect；改一格只更新一格（断言其他格的 effect 未触发）；提供行级派生（行合计 computed）与列合计，合计单元格只在其依赖行变化时更新。

```javascript
const grid = Array.from({ length: 10 }, (_, i) =>
  Array.from({ length: 10 }, (_, j) => createSignal(i * 10 + j)))
const fired = new Set() // 触发记录

function renderGrid(container) {
  for (let i = 0; i < 10; i++) {
    const rowSignals = grid[i]
    // 行合计 computed
    const rowSum = createComputed(() => rowSignals.reduce((s, sig) => s + sig.get(), 0))
    rowSignals.forEach((sig, j) => {
      const el = container.appendChild(document.createElement('div'))
      effect(() => { fired.add(`${i},${j}`); el.textContent = sig.get() })
    })
    const sumEl = container.appendChild(document.createElement('div'))
    effect(() => { fired.add(`sum,${i}`); sumEl.textContent = rowSum.read() })
  }
}
// updateCell(3,4,999) → fired 只含 3,4 与 sum,3
```
**评分点**：
- 单元格独立 signal + effect（粒度核心）。
- 行合计 computed 依赖该行信号、自动最小更新。
- fired 集合断言更新范围。
- 能对比组件级方案（改 1 格 → 全网格重渲染）说明收益。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-4cb88237-8e14-4975-876b-feda47b44c86-cwd'; fi
exit "$__zcode_status"
