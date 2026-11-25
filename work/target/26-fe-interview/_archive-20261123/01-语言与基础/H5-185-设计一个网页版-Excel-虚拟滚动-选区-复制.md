---
title: [H5-185] 设计一个网页版 Excel（虚拟滚动/选区/复制粘贴）
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-185：设计一个网页版 Excel（虚拟滚动/选区/复制粘贴）
**答**：
- 数据模型：`Map<"r:c", value>` 只存非空单元格——10 万行也占不了多少内存；渲染层与数据分离。
- 虚拟滚动：撑出真实滚动高度的 spacer，只渲染可视窗口的 ~20 行 DOM，scroll 事件 rAF 节流重算。
- 选区：pointerdown 定锚点、按住移动扩展矩形选区；编辑用单个复用的浮动 input（双击/Enter 进入）。
- 剪贴板协议：copy 时按选区生成 **TSV** 写入 text/plain（与 Excel/WPS 双向兼容）；paste 时解析 TSV 从锚点展开。
- 公式概览：单元格存公式字符串，求值 = 解析引用（=A1+B2）建依赖图 + 拓扑排序，DFS 检测循环引用。

```html
<div id="sheet" tabindex="0"></div>
<style>
  #sheet { position: relative; overflow: auto; height: 320px; width: 840px;
           font: 13px/32px sans-serif; background: #fff; }
  .row { position: absolute; left: 0; display: flex; height: 32px; }
  .cell { width: 96px; flex: none; padding: 0 6px; white-space: nowrap;
          border-right: 1px solid #eee; border-bottom: 1px solid #eee; }
  .cell.sel { background: #dbeafe; }
</style>
<script>
// 三大件：数据模型 Map<r,c,value> + 虚拟滚动 + 选区/剪贴板
const data = new Map();               // key: "r:c"，10 万格只存非空
const ROWS = 10000, COLS = 8, ROW_H = 32;
const sheet = document.getElementById('sheet');

// 1) 虚拟滚动：spacer 撑出真实滚动条，只渲染可视 ~20 行
const spacer = document.createElement('div');
spacer.style.height = ROWS * ROW_H + 'px';
sheet.append(spacer);
sheet.addEventListener('scroll', () => requestAnimationFrame(paintVisible));
function paintVisible() {
  const r0 = Math.floor(sheet.scrollTop / ROW_H);
  const r1 = Math.ceil((sheet.scrollTop + sheet.clientHeight) / ROW_H);
  sheet.querySelectorAll('.row').forEach((n) => n.remove());
  for (let r = r0; r < r1; r++) {
    const row = document.createElement('div');
    row.className = 'row';
    row.style.top = r * ROW_H + 'px';           // 内容坐标，随容器自然滚动
    for (let c = 0; c < COLS; c++) {
      const cell = document.createElement('div');
      cell.className = 'cell';
      cell.dataset.r = r; cell.dataset.c = c;
      cell.textContent = data.get(`${r}:${c}`) ?? '';
      row.append(cell);
    }
    sheet.append(row);
  }
}
paintVisible();

// 2) 选区：pointerdown 定锚点，按住移动扩展矩形
let anchor = null, selRect = null;
sheet.addEventListener('pointerdown', (e) => {
  const cell = e.target.closest('.cell'); if (!cell) return;
  anchor = { r: +cell.dataset.r, c: +cell.dataset.c };
  setSelection(anchor, anchor);
});
sheet.addEventListener('pointermove', (e) => {
  if (!anchor || !(e.buttons & 1)) return;
  const cell = e.target.closest('.cell'); if (!cell) return;
  setSelection(anchor, { r: +cell.dataset.r, c: +cell.dataset.c });
});
function setSelection(a, b) {
  selRect = {
    minR: Math.min(a.r, b.r), maxR: Math.max(a.r, b.r),
    minC: Math.min(a.c, b.c), maxC: Math.max(a.c, b.c),
  };
  for (const el of sheet.querySelectorAll('.cell')) {
    const r = +el.dataset.r, c = +el.dataset.c;
    el.classList.toggle('sel',
      r >= selRect.minR && r <= selRect.maxR && c >= selRect.minC && c <= selRect.maxC);
  }
}

// 3) 剪贴板协议：copy 生成 TSV（与 Excel 双向兼容），paste 解析 TSV 展开
sheet.addEventListener('copy', (e) => {
  const { minR, minC, maxR, maxC } = selRect;
  const lines = [];
  for (let r = minR; r <= maxR; r++)
    lines.push(Array.from({ length: maxC - minC + 1 },
      (_, i) => data.get(`${r}:${minC + i}`) ?? '').join('\t'));
  e.clipboardData.setData('text/plain', lines.join('\n'));
  e.preventDefault();
});
sheet.addEventListener('paste', (e) => {
  if (!anchor) return;
  const tsv = e.clipboardData.getData('text/plain');
  tsv.replace(/\r/g, '').split('\n').forEach((line, dr) =>
    line.split('\t').forEach((v, dc) =>
      data.set(`${anchor.r + dr}:${anchor.c + dc}`, v)));
  paintVisible();
  e.preventDefault();
});

// 4) 公式概览：单元格存公式串，求值 = 解析引用建依赖图 + 拓扑排序，
//    DFS 检测循环引用；编辑用单个复用浮动 input（双击/Enter 进入）
// 5) 性能：rAF 合帧渲染；输入态只重渲染编辑格；10 万行虚拟化下 DOM 恒定 ~200
</script>
```
