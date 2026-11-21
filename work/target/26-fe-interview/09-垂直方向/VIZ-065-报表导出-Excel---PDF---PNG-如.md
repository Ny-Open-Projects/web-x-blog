---
title: [VIZ-065] 报表导出 Excel / PDF / PNG 如何实现？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-065：报表导出 Excel / PDF / PNG 如何实现？
**答**：**Excel**：SheetJS（xlsx）或 exceljs 前端生成 xlsx，AOA（array of arrays）转 sheet，支持多 sheet、列宽、合并单元格；超 10 万行走服务端流式导出。**PNG**：图表 `getDataURL` / SVG 转 PNG（见 VIZ-014）。**PDF**：jsPDF 把 PNG 逐页 addImage，或复用浏览器打印。批量导出注意：置 loading 防重复点击；任务大时逐个 yield 让出主线程；文件名带时间戳；数字列保持数值类型（别导成文本）。

```javascript
import * as XLSX from 'xlsx';
// 报表导出：前端生成 xlsx，多 sheet 支持；超大报表(>10w 行)改走服务端流式
function exportExcel(sheets) {
  const wb = XLSX.utils.book_new();
  for (const { name, aoa, widths } of sheets) {
    const ws = XLSX.utils.aoa_to_sheet(aoa);        // 二维数组转 sheet
    ws['!cols'] = widths?.map(w => ({ wch: w }));   // 列宽
    XLSX.utils.book_append_sheet(wb, ws, name);
  }
  XLSX.writeFile(wb, `报表_${new Date().toISOString().slice(0, 10)}.xlsx`);
}
// PNG：chart.getDataURL({ pixelRatio: 2 }) 直接下载
function downloadDataURL(url, filename) {
  const a = document.createElement('a');
  a.href = url; a.download = filename; a.click();
}
// PDF：jsPDF 分页 addImage；批量导出置 loading，逐个 await 防止主线程长任务
```
