---
title: [NODE-681] 大文件流式处理（CSV/Excel 导入导出）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-681：大文件流式处理怎么做？
**答**：
- 导出流式：查询流（DB cursor → transform → CSV/Excel 流写响应——内存 O(1)，SCN-FIN-547 内存守恒）——xlsx 的流式写（exceljs streaming workbook writer）。
- 导入流式：逐行解析（csv-parse stream / xlsx 流式读）→ 批量入库（每 N 行一批——事务分批，SCN-OPS-331 小事务）→ 进度上报（任务化——SCN-FIN-512 异步导出同构）。
- 校验与行级错误：逐行 schema 校验（错行进错误报告——其余行继续——部分成功语义，SCN-FIN-611 批量操作）；错误行汇总文件产出。
- 背压与限速：导入速率与 DB 容量匹配（限速——防止导入打垮 DB）；导出的响应背压（客户端慢——SCN-NODE-636 背压链）。
- 追问钩子：为什么导入用「部分成功 + 错误报告」优于「一行错全回滚」——万行文件一行格式错就全回滚，用户改一行重传一遍（体验极差）；部分成功让 9999 行落库 + 1 行错误报告（可修可补传）——前提是每批独立事务（批间无原子性要求——导入是幂等可重放的，SCN-NODE-655 幂等先行）。

```javascript
await pipeline(
  fs.createReadStream(csvFile),
  csvParse({ columns: true }),
  transform(validateRow),                              // 逐行校验（错行收集）
  batchInsert(db, { size: 500, transaction: 'per-batch' }),   // 分批小事务
);
await reportErrors(errorRows);                         // 错误行报告
```
