---
title: [NODE-181] 设计一个文件预览服务（office→pdf 转换概览）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-181：设计一个文件预览服务（office→pdf 转换概览）？
**答**：
- 链路：请求预览 → 命中缓存直接返回 → 未命中投转换队列（异步 + 轮询）→ LibreOffice headless 转换 → PDF 上传 OSS → 缓存元数据。
- 缓存键用**文件内容 hash**（md5）：同内容只转一次；预览与源文件解耦，源更新自动失效。
- 资源控制：转换是 CPU 大户，worker 并发限 4；任务超时 2 分钟；并发大时队列削峰（NODE-144）。
- 安全：魔数校验（防伪造扩展名）、转换容器无网络隔离、超大文件拒绝、预览 PDF 加水印。

```javascript
const convertQueue = new Queue('convert', { connection: redis });

app.get('/api/preview/:fileId', async (ctx) => {
  const file = await db.file.findUnique({ where: { id: ctx.params.fileId } });
  const cacheKey = `preview:${file.id}:${file.md5}`;       // 内容 hash 缓存
  const cached = await redis.get(cacheKey);
  if (cached) return (ctx.body = JSON.parse(cached));      // 秒出
  const job = await convertQueue.add('office2pdf',
    { fileId: file.id, src: file.ossKey, md5: file.md5 },
    { timeout: 120_000, attempts: 2 });
  ctx.body = { status: 'CONVERTING', jobId: job.id, pollAfter: 2000 }; // 异步轮询
});

new Worker('convert', async (job) => {
  const local = await oss.get(job.data.src);               // 沙箱内执行转换
  const out = `/tmp/${job.data.fileId}.pdf`;
  await execFileAsync('libreoffice',
    ['--headless', '--convert-to', 'pdf', '--outdir', '/tmp', local]);
  await oss.put(`preview/${job.data.fileId}.pdf`, out);
  const meta = { pdfUrl: `${CDN}/preview/${job.data.fileId}.pdf`, pages: await pdfPages(out) };
  await redis.setex(`preview:${job.data.fileId}:${job.data.md5}`, 86_400, JSON.stringify(meta));
}, { concurrency: 4 });                                    // CPU 大户限并发
```
