---
title: [HW-147] 手写大表格渲染优化——contain/rga 固定布局 + 分块挂载 + 行高契约防抖动
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-147：手写大表格渲染优化——contain/rga 固定布局 + 分块挂载 + 行高契约防抖动
**答**：1000 行表格渲染卡顿三层优化：① table-layout: fixed + contain: strict（行子树样式/布局影响范围锁定，PER-345）；② 分块挂载（rAF 每帧 50 行，帧预算控制 PER-241）；③ 行高契约（CSS 固定行高，内容溢出 ellipsis——单元格内容不定高，杜绝逐行 layout 连锁）。

```javascript
function mountLargeTable(container, rows, { perFrame = 50 } = {}) {
  const table = container.querySelector('table');
  table.style.tableLayout = 'fixed';
  let i = 0;
  function chunk() {
    const start = performance.now();
    const frag = document.createDocumentFragment();       // 片段批量挂载（一次 reflow）
    while (i < rows.length && performance.now() - start < 8) {   // 8ms 预算（16.7ms 的一半留合成）
      frag.appendChild(buildRow(rows[i++]));
    }
    table.querySelector('tbody').appendChild(frag);
    if (i < rows.length) requestAnimationFrame(chunk);
  }
  requestAnimationFrame(chunk);
}
```
```css
.data-table { table-layout: fixed; width: 100%; }
.data-table td {
  height: 40px;                       /* 行高契约：内容溢出截断，行高恒定 */
  overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
  contain: content;                   /* 单元格子树样式/布局影响锁定（PER-345） */
}
.data-table tbody { content-visibility: auto; contain-intrinsic-size: auto 40000px; }  /* 屏外行跳过渲染 */
```
**评分点**：
- contain: content / content-visibility 组合（屏外行零渲染成本）——本题核心。
- 行高契约（固定 40px + ellipsis）防内容定高引起的连锁 layout。
- 分块挂载 8ms 预算 + DocumentFragment 单次 reflow。
- table-layout: fixed 与列宽独立性。
