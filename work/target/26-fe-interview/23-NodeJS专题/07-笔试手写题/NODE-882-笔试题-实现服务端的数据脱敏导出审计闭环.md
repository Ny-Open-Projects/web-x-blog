---
title: [NODE-882] 笔试题——实现数据导出脱敏审计闭环（导出→脱敏→审计→追踪）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-882：手写导出闭环

**需求与边界**：
- 需求：导出脱敏审计（SCN-FIN-783/698）——① 导出脱敏强制（schema 驱动——SCN-FIN-773）；② 导出审计（操作者/范围/行数——SCN-FIN-783）；③ 导出文件水印（SCN-FIN-625）；④ 泄露追溯（水印 → 操作者——SCN-FIN-625）。
- 边界：① 导出的行级权限（SCN-OPS-609）；② 导出的保留期（SCN-FIN-625）；③ 导出的配额（频率限制——SCN-NODE-641）。

**答**：
```javascript
worker.on('export', async (job) => {
  const rows = await scopedQuery(job);                 // 行级权限（SCN-OPS-609）
  const masked = deepMask(rows, exportRules);          // 脱敏强制（SCN-FIN-773 出口统一）
  const file = await streamToCsv(masked, { watermark: { user: job.user, ts: Date.now() } });   // 水印
  const url = await oss.signPut(file, { expires: 3600 });
  await auditExport({ user: job.user, query: job.query, rows: rows.length,
    file: url, retention: '30d' });                    // 审计 + 保留期（SCN-FIN-625/783）
  notify(job.user, { url });
});
// 泄露追溯：文件水印 → 操作者（SCN-FIN-625）
traceWatermark(fileWatermarkText) → operator;
```

**评分点**:
- 脱敏强制（schema 驱动——SCN-FIN-773 出口统一）。
- 水印 + 泄露追溯（SCN-FIN-625）。
- 行级权限 + 配额（SCN-OPS-609/641）。
- 审计闭环 + 保留期（SCN-FIN-783）。
