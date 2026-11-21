---
title: ExcelJS 前端导出 Excel 与 JSZip 压缩包
date: 2026-11-17
categories: [课程, 低代码]
tags: [25-lowcode, 实战, ExcelJS, 导出]
---

## ExcelJS 前端导出 Excel 与 JSZip 压缩包

导出 Excel 完整链路（全部在前端完成，不占服务器）：

```ts
const buffer = await workbook.xlsx.writeBuffer();
const blob = new Blob([buffer], { type: 'application/octet-stream' });
const url = URL.createObjectURL(blob);
a.href = url; a.download = name; a.click();
URL.revokeObjectURL(url);  // 必须释放内存
```

数据流：antd Table 表头改造成 ExcelJS 列头 + 填行数据 → `writeBuffer` → Blob（**数组包裹** + MIME 类型）→ `URL.createObjectURL` 生成临时 blob: URL → `<a download>` + `click()` 触发下载 → **`revokeObjectURL` 释放内存**（漏了就是内存泄漏）。

压缩包导出：复用生成 Buffer 逻辑，`zip.file(name, content)` 逐个塞入 + `zip.generateAsync({type:'blob'})`，下载复用同一 saveFileWithBlob 链路。用 `isWriteFile` 开关区分两条分支。

**本项目实例**：问卷统计页的表头来自 component 表的组件 title，行数据来自 component_data；checkbox 数组 `join(',')` 转逗号串、数字兜底转字符串——导出前要先做这层数据规整。

出处「课程25 · 21-9、21-10、22-1」
