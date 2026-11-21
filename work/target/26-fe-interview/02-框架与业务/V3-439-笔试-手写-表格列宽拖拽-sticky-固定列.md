---
title: [V3-439] 笔试：手写表格列宽拖拽（colgroup + 最小宽度约束）
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-439：笔试：手写表格列宽拖拽（colgroup + 最小宽度约束）
**题**：实现表格列宽拖拽：表头单元格右侧 8px 手柄；拖动更新 colgroup 中对应 col 的宽度；最小宽度约束（80px）；拖动中禁用文本选择；总宽超出容器出现横向滚动（sticky 固定首列同步宽度）。

```javascript
function useColumnResize(cols) {
  const widths = ref(cols.map(c => c.width))
  let dragging = null
  function onHandleDown(index, e) {
    dragging = { index, startX: e.clientX, startW: widths.value[index] }
    document.body.style.userSelect = 'none' // 禁止选中文本
    e.target.setPointerCapture(e.pointerId)
  }
  function onHandleMove(e) {
    if (!dragging) return
    const dw = e.clientX - dragging.startX
    const min = 80
    widths.value[dragging.index] = Math.max(min, dragging.startW + dw)
  }
  function onHandleUp() {
    dragging = null
    document.body.style.userSelect = ''
  }
  return { widths, onHandleDown, onHandleMove, onHandleUp }
}
// <colgroup><col v-for="(w, i) in widths" :style="{ width: w + 'px' }" /></colgroup>
// 首列 th { position: sticky; left: 0; z-index: 2; background: #fff } // 宽度随 colgroup 自动同步
```
**评分点**：
- colgroup 统一控宽（而非每行 td，保证对齐）。
- 最小宽度 Math.max 约束。
- 拖动中 userSelect 禁用 + pointer capture。
- sticky 首列与 colgroup 联动说明。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-ae15d8b4-3ef1-49e1-9ea2-e202949b691c-cwd'; fi
exit "$__zcode_status"
