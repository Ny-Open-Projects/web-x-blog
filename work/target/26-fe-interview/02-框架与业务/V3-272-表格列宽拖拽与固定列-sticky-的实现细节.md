---
title: [V3-272] 表格列宽拖拽与固定列（sticky）的实现细节是什么？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-272：表格列宽拖拽与固定列（sticky）的实现细节是什么？
**答**：
- 列宽拖拽：表头单元格右缘放 4px 拖拽把手，`pointerdown` 记起始 x 与列宽，`pointermove` 计算差值实时更新该列 `width`（写 colgroup/内联样式），`pointerup` 结束并持久化到 localStorage。
- 性能：拖动过程**只改一列宽度**，表格用 `table-layout: fixed` 避免整表重排；宽列动画用 rAF 节流，结束时才 commit 到 store。
- 固定列：sticky 需要显式定位偏移——左侧固定列 `position: sticky; left: 0/120px`，偏移量 = 前面所有固定列宽之和；同理右侧。
- 阴影指示：主区域 scrollLeft > 0 时左侧固定列加投影，用 IntersectionObserver 或 scroll 事件计算，避免每帧重算全部列。
- 坑：`table-layout: fixed` 下 sticky 列在 Safari 的层叠问题（需要 zIndex 分层）；行 hover 的跨列高亮需要 tr 级别事件而非 td。

```vue
<script setup>
import { reactive, ref } from 'vue';
const cols = reactive([
  { key: 'id', width: 80, fixed: 'left' }, { key: 'name', width: 200 }, { key: 'amount', width: 120 },
]);
const dragging = ref(null); // { index, startX, startW }
function onHandleDown(e, i) { dragging.value = { i, startX: e.clientX, startW: cols[i].width }; }
function onHandleMove(e) {
  if (!dragging.value) return;
  const { i, startX, startW } = dragging.value;
  cols[i].width = Math.max(60, startW + (e.clientX - startX)); // 只改一列
}
window.addEventListener('pointermove', onHandleMove);
window.addEventListener('pointerup', () => (dragging.value = null));
// sticky 偏移：cols.filter 前 n 个固定列宽度和
const stickyLeft = (i) => cols.slice(0, i).reduce((s, c) => s + c.width, 0) + 'px';
</script>
<template>
  <span class="col-resizer" @pointerdown="onHandleDown($event, i)"></span>
</template>
```
