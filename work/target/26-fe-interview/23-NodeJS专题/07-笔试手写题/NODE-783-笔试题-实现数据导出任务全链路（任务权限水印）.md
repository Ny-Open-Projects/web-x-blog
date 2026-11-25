---
title: [NODE-783] 笔试题——实现导出任务全链路（任务/权限/水印/审计）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-783：手写导出全链路

**需求与边界**：
- 需求：导出全链路（SCN-NODE-714）——① 异步任务（创建/进度/完成通知——SCN-FIN-512）；② 行级权限过滤（导出数据按权限裁剪——SCN-OPS-609）；③ 水印与审计（谁导出了什么——SCN-FIN-625）；④ 签名直链下载（SCN-FIN-494 短时效）。
- 边界：① 数据量上限（行数上限——超限引导异步任务）；② 导出去重（同参数短窗口合并——SCN-NODE-714）；③ 导出文件的保留期（TTL 清理——存储治理）。

**答**：
```javascript
app.post('/export', auth(), quota(), async (req, res) => {
  const count = await countRows(req.query, req.user);  // 行数预检
  if (count > 100_000) return res.status(413).json({ code: 'TOO_LARGE' });   // 上限
  const taskId = crypto.randomUUID();
  await queue.add('export', { taskId, query: req.query, userId: req.user.id });
  res.json({ taskId });                                // 异步任务（SCN-FIN-512）
});
worker.on('export', async (job) => {
  const rows = await db.query(`SELECT * FROM (${job.query.sql}) t WHERE ${rowScope(job.user)}`);   // 行级权限（SCN-OPS-609）
  const file = await streamToCsv(rows, { watermark: job.user.id });   // 水印（SCN-FIN-625）
  const url = await oss.signPut(file, { expires: 3600 });
  await auditExport(job.user, job.query, rows.length); // 审计（谁导出了什么）
  notifyDone(job.user, { url, taskId: job.taskId });   // 签名直链通知（SCN-FIN-494）
});
```

**评分点**:
- 行数预检 + 异步任务化（SCN-FIN-512）。
- 行级权限过滤进导出（rowScope——SCN-OPS-609）。
- 水印 + 审计闭环（谁导出了什么——SCN-FIN-625）。
- 签名直链（短时效——SCN-FIN-494）。
