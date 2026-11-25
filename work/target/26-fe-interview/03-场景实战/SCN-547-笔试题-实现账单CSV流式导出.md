---
title: [SCN-547] 笔试题——实现前端账单 CSV 流式导出（分块 + 内存守恒）？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-547：手写小数据量账单 CSV 流式导出（<1 万行走前端）

**需求与边界**：
- 需求：游标分页拉全量 → 流式写 CSV → Blob 下载；全程内存只保留当前块。
- 边界：① CSV 注入防御（`=`, `+`, `-`, `@` 开头的单元格前置 `'`）；② 字段含逗号/引号/换行转义；③ BOM 头保证 Excel 中文；④ 中断可取消。

**答**：
```javascript
function csvCell(v) {
  let s = String(v ?? '');
  if (/^[=+\-@\t\r]/.test(s)) s = "'" + s;                  // 防 CSV 公式注入
  if (/[",\n]/.test(s)) s = '"' + s.replace(/"/g, '""') + '"';
  return s;
}
async function exportCsv(cursorLoader, columns, { onProgress, signal } = {}) {
  const encoder = new TextEncoder();
  const chunks = []; let bytes = 0;
  const write = (line) => {
    const buf = encoder.encode(line + '\r\n');              // CRLF 标准
    chunks.push(buf); bytes += buf.length;
  };
  write('\uFEFF' + columns.map(csvCell).join(','));         // BOM + 表头
  let cursor = null, rows = 0;
  while (true) {
    if (signal?.aborted) throw new DOMException('取消', 'AbortError');
    const { list, next } = await cursorLoader(cursor);
    for (const r of list) write(columns.map(c => csvCell(r[c.key])).join(','));
    rows += list.length;
    onProgress?.(rows);
    if (!next) break;
    cursor = next;
  }
  const blob = new Blob(chunks, { type: 'text/csv;charset=utf-8' });   // 合并下载
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = `bill_${Date.now()}.csv`;
  a.click();
  URL.revokeObjectURL(a.href);                              // 释放
  return rows;
}
// 内存守恒说明：chunks 数组本身持有全部文本——超大数据量时改用
// File System Access API 的 writable 流逐块写盘，或直接走服务端异步导出（SCN-512）。
```

**评分点**:
- CSV 注入防御（公式前缀）与字段转义三件套（逗号/引号/换行）。
- BOM + CRLF 的兼容性细节。
- 游标分页 + AbortSignal 可取消 + 进度回调。
- 明确说出前端导出的内存边界与超限时的替代方案（加分项）。
