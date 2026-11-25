---
title: [WEB-408] 浏览器打印/导出 PDF 前端要怎么适配？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 浏览器]
type: 面试题
---

## WEB-408：浏览器打印/导出 PDF 前端要怎么适配？
**答**：
- print 样式：@media print 隐藏交互元素、强制浅色（省墨）、避免分页断裂（break-inside: avoid）、隐藏背景图默认不打印。
- 页面上下边距与分页：@page { size: A4; margin: 2cm }；页眉页脚依赖浏览器设置，精确排版走服务端 PDF（Puppeteer/pdfmake）。
- 交互细节：print() 前展开折叠内容、textarea 改成渲染 div；window.print 前用 beforeprint 事件切状态。

```javascript
@media print {
  .no-print { display: none; }
  .card { break-inside: avoid; box-shadow: none; }
}
/* @page { size: A4; margin: 15mm; } */
window.addEventListener('beforeprint', () => expandAll());
console.log('复杂票据导 PDF: 服务端 Puppeteer page.pdf()');
```
