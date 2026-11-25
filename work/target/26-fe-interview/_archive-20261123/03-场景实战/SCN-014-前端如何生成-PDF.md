---
title: [SCN-014] 前端如何生成 PDF？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-014：前端如何生成 PDF？
**答**：
- 方案一 window.print + @media print：浏览器原生分页，文字可选中，最稳，适合导出简历、报告。
- 方案二 html2canvas + jsPDF：截图式，还原度取决于 canvas，文字不可选中、体积大，适合海报、证书。
- 方案三 pdfmake/pdf-lib 直接构建文档或服务端 puppeteer：需要精确排版时用。
- 选型口诀：能打印就打印，要下载文件再考虑 jsPDF。

```javascript
import { jsPDF } from 'jspdf';
import html2canvas from 'html2canvas';

async function exportPDF(el, filename) {
  const canvas = await html2canvas(el, { scale: 2 }); // 放大 2 倍防模糊
  const pdf = new jsPDF('p', 'mm', 'a4');
  const pageW = pdf.internal.pageSize.getWidth();
  const imgH = (canvas.height * pageW) / canvas.width; // 等比缩放到 A4 宽
  pdf.addImage(canvas.toDataURL('image/jpeg', 0.95), 'JPEG', 0, 0, pageW, imgH);
  pdf.save(filename);
}
// 方案一示例：打印前给 body 加 class，@media print 里隐藏导航与按钮
// window.print();
```

## 四、表单与交互状态
