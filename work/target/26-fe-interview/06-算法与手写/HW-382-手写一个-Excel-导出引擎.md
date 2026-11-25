---
title: [HW-382] 手写一个 Excel 导出引擎：样式映射与大数据量分 Sheet
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-382：手写一个 Excel 导出引擎：样式映射与大数据量分 Sheet

**答**：
- 需求：实现 ExcelExport：数据 → SheetXML（用 ExcelJS 类 API：workbook/sheet/row/cell）；样式映射（前端 CSS 风格 → Excel 样式：字体/填充/边框/数字格式）；大数据分 Sheet（每 10 万行一个 sheet，避免内存与 Excel 行为问题）；流式写出（避免整本驻内存）。
- 边界：数字格式（金额千分位、日期序列值）；合并单元格；分 Sheet 的表头重复与命名；导出进度回调。
- 评分点：样式映射表；分 Sheet 阈值；流式写。

```javascript
class ExcelExport {
  constructor({ rowsPerSheet = 100000 } = {}) { this.rowsPer = rowsPerSheet; }
  async export(columns, data, { style = {}, onProgress } = {}) {
    const wb = new ExcelJS.Workbook();
    const sheetCount = Math.ceil(data.length / this.rowsPer);
    for (let s = 0; s < sheetCount; s++) {                   // 分 Sheet
      const ws = wb.addWorksheet(s === 0 ? 'Sheet1' : `Sheet${s + 1}`);
      ws.columns = columns.map(c => ({ header: c.label, key: c.key, width: c.width ?? 15 }));
      ws.getRow(1).font = { bold: true };                    // 表头样式
      const slice = data.slice(s * this.rowsPer, (s + 1) * this.rowsPer);
      for (const row of slice) {
        const r = ws.addRow(pickKeys(row, columns));
        for (const c of columns) {                           // 样式映射
          const cellStyle = style[c.key] ?? {};
          const cell = r.getCell(c.key);
          if (cellStyle.numFmt) cell.numFmt = cellStyle.numFmt;   // 数字格式
          if (cellStyle.bg) cell.fill = { type: 'pattern', pattern: 'solid',
            fgColor: { argb: cssToArgb(cellStyle.bg) } };
          if (cellStyle.color) cell.font = { color: { argb: cssToArgb(cellStyle.color) } };
        }
        if (onProgress && (r.number % 5000 === 0))
          onProgress((s * this.rowsPer + r.number) / data.length);
      }
      if (style.merge) ws.mergeCells(style.merge);           // 合并单元格
    }
    const buf = await wb.xlsx.writeBuffer();                 // 流式写
    return new Blob([buf], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
  }
}
function cssToArgb(css) {                                   // CSS 色 → ARGB
  const { r, g, b } = parseCssColor(css);
  return 'FF' + [r, g, b].map(x => x.toString(16).padStart(2, '0')).join('').toUpperCase();
}
function pickKeys(row, cols) { return Object.fromEntries(cols.map(c => [c.key, row[c.key]])); }
```
