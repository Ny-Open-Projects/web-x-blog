---
title: [SCN-147] B 端单据要"打印"：多页分页控制、每页页眉页脚、还要和预印纸（套打）对齐，怎么做？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-147：B 端单据要"打印"：多页分页控制、每页页眉页脚、还要和预印纸（套打）对齐，怎么做？
**答**：
- 打印优先用浏览器原生能力 + 打印样式，而不是生成 PDF：`@media print` 隐藏交互元素，`break-inside: avoid` 保证单据块不被劈开。
- 每页页眉页脚用 CSS `position: fixed`（打印时每页重复），页码用 `@page` 边距 + 计数方案；复杂页码用分页渲染（把数据按每页 N 行手动切）。
- 套打：只打印数据不打印底图，用绝对定位毫米单位模板对准预印纸，先用一张废纸校准再放量。
- 打印前 `window.onbeforeprint` 可以做数据快照兜底，并提供"打印预览"页让用户先看。

```javascript
// 打印方案：分页渲染 + 固定页眉页脚 + 套打模板注入
const PRINT_CSS = `
  @media print {
    .screen-only { display: none !important; }         // 隐藏按钮/导航
    .doc-block { break-inside: avoid; }                // 单据块不跨页劈开
    .page-header, .page-footer { position: fixed; left: 0; right: 0; }
    .page-header { top: 0; } .page-footer { bottom: 0; }
    @page { size: A4; margin: 18mm 12mm; }             // 预留页眉页脚空间
  }
  /* 套打：只打数据层，底图由预印纸提供 */
  .dot-matrix { position: relative; font-family: monospace; }
  .dot-matrix .field { position: absolute; }
`;

export function printDocument(order) {
  const style = document.createElement('style');
  style.textContent = PRINT_CSS;
  document.head.appendChild(style);

  // 手动分页：按每页行数切数据，页码可控
  const ROWS_PER_PAGE = 18;
  const pages = chunk(order.items, ROWS_PER_PAGE).map((items, i) => ({
    items,
    pageNo: i + 1,
    total: Math.ceil(order.items.length / ROWS_PER_PAGE),
  }));

  const win = window.open('', '_blank', 'width=900,height=700');
  win.document.write(renderPrintTemplate(order, pages)); // 每页独立 .page，页眉页脚随页渲染
  win.document.head.appendChild(style.cloneNode(true));
  win.onload = () => { win.focus(); win.print(); };      // 打印完保留窗口由用户关闭
}

// 套打校准：毫米定位 + 微调偏移存 localStorage
export function dotMatrixOffset(key) {
  const saved = JSON.parse(localStorage.getItem(`print-offset:${key}`) ?? '{"x":0,"y":0}');
  return saved; // 模板根节点 transform: translate(Xmm, Ymm)
}
```
