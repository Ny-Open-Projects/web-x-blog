---
title: [SCN-013] 10 万行数据要导出 Excel/CSV，前端怎么处理？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-013：10 万行数据要导出 Excel/CSV，前端怎么处理？
**答**：
- 首选方案永远是后端异步导出：接口返回任务 ID，前端轮询任务状态后拿文件地址下载，前端只做触发与提示。
- 数据确实在前端时：CSV 比 Excel 简单可靠——字符串拼接 + Blob 下载；注意加 BOM 防 Excel 中文乱码、字段转义引号防注入。
- 大数据量分批拼接（按 5MB 分段或放 Web Worker），避免主线程长任务卡死页面。

```javascript
function exportCSV(rows, filename) {
  // BOM 头：否则 Excel 打开中文乱码
  let csv = '\uFEFF' + Object.keys(rows[0]).join(',') + '\n';
  for (const row of rows) {
    csv += Object.values(row)
      .map((v) => `"${String(v ?? '').replaceAll('"', '""')}"`) // 引号转义防 CSV 注入
      .join(',') + '\n';
  }
  const blob = new Blob([csv], { type: 'text/csv;charset=utf-8' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = filename;
  a.click();
  URL.revokeObjectURL(a.href); // 释放内存
}
```
