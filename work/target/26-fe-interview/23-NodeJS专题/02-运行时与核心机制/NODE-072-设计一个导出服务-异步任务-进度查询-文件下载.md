---
title: [NODE-072] 设计一个导出服务（异步任务、进度查询、文件下载）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-072：设计一个导出服务（异步任务、进度查询、文件下载）？
**答**：
- 大数据量导出绝不能同步返回（超时+内存）：**异步任务化**——`POST /exports` 创建任务返回 taskId → 后台 worker 流式生成文件（写临时目录/对象存储）→ 前端轮询 `GET /exports/:id` 拿状态与进度 → 完成后给带签名的临时下载 URL（时效防盗链）。
- 服务端要点：任务持久化（DB/Redis，重启可恢复）、并发上限（防导出风暴打挂 DB，用队列 + p-limit）、**流式生成**（逐行查 + 写 CSV，cursor 分页避免 OFFSET 深翻页）、进度上报（已处理行数/总行数）、失败重试与清理策略。
- 进阶：WebSocket/SSE 推送进度替代轮询；超大导出拆分多个分片文件打包。

```javascript
const { Queue, Worker } = require('bullmq');
const { createObjectCsvStringifier } = require('csv-writer');

// 1. 创建任务
const exportQueue = new Queue('export', { connection: redisOpts });
router.post('/exports', async (ctx) => {
  const { type, filters } = ctx.request.body;
  const task = { id: crypto.randomUUID(), uid: ctx.state.user.uid, type, filters,
                 status: 'pending', progress: 0, total: 0, fileUrl: null };
  await redis.setex(`export:${task.id}`, 86400, JSON.stringify(task));
  await exportQueue.add('export', task, { attempts: 3, backoff: { type: 'exponential', delay: 5000 } });
  ctx.body = { taskId: task.id, pollAfterMs: 1000 };
});

// 2. Worker：流式生成 + 进度上报
new Worker('export', async (job) => {
  const task = job.data;
  const total = await db.query('SELECT COUNT(*) c FROM orders WHERE uid = ?', [task.uid]).then((r) => r[0].c);
  await saveTask(task.id, { status: 'running', total });

  const filePath = `/tmp/export-${task.id}.csv`;
  const out = require('fs').createWriteStream(filePath);
  const csv = createObjectCsvStringifier({ header: [{ id: 'id', title: '订单号' }, { id: 'amount', title: '金额' }] });
  out.write(csv.getHeaderString());

  let processed = 0, lastId = 0;
  while (true) {
    // 游标分页：避免 OFFSET 深翻页
    const rows = await db.query(
      'SELECT id, amount FROM orders WHERE uid = ? AND id > ? ORDER BY id LIMIT 1000', [task.uid, lastId]);
    if (!rows.length) break;
    out.write(csv.stringifyRecords(rows));
    lastId = rows[rows.length - 1].id;
    processed += rows.length;
    await saveTask(task.id, { progress: Math.round((processed / total) * 100) }); // 进度可查
  }
  out.end();
  await new Promise((r) => out.on('close', r));
  const fileUrl = await ossUpload(filePath, `exports/${task.id}.csv`, { expiresIn: 3600 }); // 签名临时 URL
  await saveTask(task.id, { status: 'done', fileUrl });
  await fs.unlink(filePath);   // 清理临时文件
}, { connection: redisOpts, concurrency: 3 });   // 隔离舱：最多 3 个导出并发

// 3. 进度查询
router.get('/exports/:id', async (ctx) => {
  const raw = await redis.get(`export:${ctx.params.id}`);
  if (!raw) ctx.throw(404);
  const task = JSON.parse(raw);
  if (task.uid !== ctx.state.user.uid) ctx.throw(403);   // 只能查自己的任务
  ctx.body = { status: task.status, progress: task.progress, fileUrl: task.fileUrl };
});
```
