---
title: [NODE-070] 设计一个文件上传服务（分片上传、断点续传、秒传的服务端配合）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-070：设计一个文件上传服务（分片上传、断点续传、秒传的服务端配合）？
**答**：
- 协议设计：① 客户端计算文件 **hash（sha256，Web Worker 分块算）**→ `POST /upload/init` 查秒传：服务端已有该 hash 直接返回 URL（秒传完成）；② 未命中则返回 uploadId，客户端切片（如 5MB/片）**并发 PUT /upload/chunk**（每片带 index 与 hash）；③ 全部完成后 `POST /upload/complete`，服务端按序合并分片并校验整体 hash。
- 断点续传：`init` 时返回**已有分片列表**（`uploaded: [0,1,2]`），客户端跳过已传分片。
- 服务端要点：分片临时目录隔离 uploadId、合并用流式 append（`fs.appendFile`/createWriteStream append 防内存）、整体 hash 校验失败清理脏分片、限制并发与总大小、病毒扫描钩子。

```javascript
const crypto = require('node:crypto');
const fs = require('node:fs/promises');
const path = require('node:path');

const CHUNK_DIR = '/data/uploads/chunks';
const FINAL_DIR = '/data/uploads/files';

// 1. 初始化：查秒传，返回已有分片
router.post('/upload/init', async (ctx) => {
  const { fileHash, fileName, fileSize, chunkSize } = ctx.request.body;
  const finalPath = path.join(FINAL_DIR, fileHash);
  try {
    await fs.access(finalPath);
    return (ctx.body = { skipUpload: true, url: `/files/${fileHash}` });   // 秒传
  } catch { /* 不存在，继续走分片 */ }

  const uploadId = crypto.randomUUID();
  await fs.mkdir(path.join(CHUNK_DIR, uploadId), { recursive: true });
  await fs.writeFile(path.join(CHUNK_DIR, `${uploadId}.meta.json`),
    JSON.stringify({ fileHash, fileName, fileSize, chunkSize, createdAt: Date.now() }));

  const uploaded = (await fs.readdir(path.join(CHUNK_DIR, uploadId)))
    .filter((f) => f.startsWith('chunk-')).map((f) => Number(f.split('-')[1]));
  ctx.body = { uploadId, uploaded };   // 断点续传：客户端跳过 uploaded 索引
});

// 2. 分片上传：流式落盘 + 校验分片 hash
router.post('/upload/chunk/:uploadId/:index', async (ctx) => {
  const { uploadId, index } = ctx.params;
  const filePath = path.join(CHUNK_DIR, uploadId, `chunk-${index}`);
  await new Promise((resolve, reject) => {
    const ws = require('fs').createWriteStream(filePath);
    ctx.req.pipe(ws).on('finish', resolve).on('error', reject);  // 流式：不占内存
  });
  ctx.body = { ok: true };
});

// 3. 完成：按序合并 + 整体 hash 校验
router.post('/upload/complete', async (ctx) => {
  const { uploadId, fileHash, totalChunks } = ctx.request.body;
  const dir = path.join(CHUNK_DIR, uploadId);
  const hash = crypto.createHash('sha256');
  const finalPath = path.join(FINAL_DIR, fileHash);
  const out = require('fs').createWriteStream(finalPath);

  for (let i = 0; i < totalChunks; i++) {
    const chunkPath = path.join(dir, `chunk-${i}`);
    const buf = await fs.readFile(chunkPath);
    hash.update(buf);
    if (!out.write(buf)) await new Promise((r) => out.once('drain', r)); // 手工背压
  }
  out.end();
  await new Promise((r) => out.on('close', r));

  if (hash.digest('hex') !== fileHash) {              // 完整性校验
    await fs.rm(dir, { recursive: true });
    await fs.unlink(finalPath).catch(() => {});
    ctx.throw(422, '文件校验失败，请重传');
  }
  await fs.rm(dir, { recursive: true });              // 清理分片
  ctx.body = { url: `/files/${fileHash}` };
});
```
