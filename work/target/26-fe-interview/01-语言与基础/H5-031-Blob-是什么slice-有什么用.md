---
title: [H5-031] Blob 是什么？slice 有什么用？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-031：Blob 是什么？slice 有什么用？
**答**：
- Blob（Binary Large Object）是不可变的二进制数据容器，File 是带元数据的 Blob。
- `blob.slice(start, end)` 可以零拷贝地切出子 Blob，这是大文件分片上传的基础。
- `new Blob([字符串或ArrayBuffer])` 可在前端生成文件，配合 `createObjectURL` + a 标签 download 实现纯前端导出。
- Blob 存磁盘、ArrayBuffer 存内存：`blob.arrayBuffer()` 可互相转换。

```javascript
// 纯前端导出 CSV 文件
function downloadCSV(rows) {
  const csv = rows.map((r) => r.join(',')).join('\n');
  const blob = new Blob(['\ufeff' + csv], { type: 'text/csv;charset=utf-8' }); // BOM 防 Excel 乱码

  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'export.csv'; // download 属性触发下载而非导航
  a.click();
  URL.revokeObjectURL(url);
}
downloadCSV([['name', 'age'], ['Wang', 30]]);

// slice 分片：1GB 文件切成 5MB 一片（配合 H5-033 上传）
function splitChunks(file, size = 5 * 1024 * 1024) {
  const chunks = [];
  for (let start = 0; start < file.size; start += size) {
    chunks.push(file.slice(start, start + size)); // Blob 切片，不占用整块内存
  }
  return chunks;
}
```
