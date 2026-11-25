---
title: [SCN-919] 政务受理单打印与 PDF 导出
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-919：政务受理单打印与 PDF 导出

**答**：
- 打印：受理单/回执打印（打印样式 @media print）、签名嵌入（电子签图片）。
- PDF：前端生成（jsPDF）或服务端渲染（复杂版式走服务端）。
- 一致性：打印样式与页面样式分离（专用 print stylesheet）。

```javascript
// 打印样式
const printCSS = `
@media print {
  .no-print { display: none !important; }
  .receipt { font-size: 12pt; page-break-after: always; }
  body { margin: 10mm; }
}`;
function printReceipt(receiptHtml) {
  const w = open('', '_blank');
  w.document.write(`<style>${printCSS}</style>${receiptHtml}`);
  w.document.close();
  w.print();
}
```
