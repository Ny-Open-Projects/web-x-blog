---
title: [NODE-770] 笔试题——实现批次导入框架（分批事务 + 错误报告 + 断点）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-770：手写导入框架

**需求与边界**：
- 需求：CSV 批量导入框架（SCN-NODE-681）——① 流式解析（pipeline——SCN-NODE-725 背压）；② 分批事务（每 500 行一批——SCN-OPS-331 小事务）；③ 行级错误收集（部分成功——SCN-NODE-681）；④ 断点续传（批次进度——中断恢复）；⑤ 进度上报（任务化）。
- 边界：① 幂等（upsert ON CONFLICT——重导不重复）；② 限速（DB 保护——导入速率与容量匹配）；③ 错误报告产出（错误行 CSV——用户可修）。

**答**：
```javascript
async function importCsv(file, taskId, { batchSize = 500 } = {}) {
  const errors = []; let done = 0;
  const startBatch = await getProgress(taskId) ?? 0;   // 断点（SCN-NODE-682）
  let batchNo = 0, buffer = [];
  await pipeline(
    fs.createReadStream(file),
    csvParse({ columns: true }),
    async function* (rows) {
      for await (const row of rows) {
        batchNo++;
        if (batchNo <= startBatch * batchSize) continue;   // 断点跳过
        try { buffer.push(validate(row)); }             // 行级校验（SCN-联想-695）
        catch (e) { errors.push({ line: batchNo, err: e.message }); continue; }   // 部分成功
        if (buffer.length >= batchSize) {               // 分批事务
          await db.transaction(tx => upsertAll(tx, buffer));   // upsert 幂等（SCN-NODE-655）
          done += buffer.length; buffer = [];
          await saveProgress(taskId, batchNo / batchSize);   // 断点
          reportProgress(taskId, done);                 // 进度（SCN-FIN-512）
          await sleep(50);                              // 限速（DB 保护）
        }
        yield row;
      }
    });
  await writeErrorReport(taskId, errors);              // 错误报告（SCN-NODE-681）
  return { done, errors: errors.length };
}
```

**评分点**:
- 分批小事务 + 断点续传（SCN-OPS-331/682 联动）。
- 行级校验 + 部分成功（错误报告——SCN-NODE-681）。
- upsert 幂等（重导不重复——SCN-NODE-655）。
- 限速 + 进度上报（DB 保护 + 任务化）。
