---
title: [XP-099] Electron 大文件下载管理怎么设计？多线程分片与断点续传？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-099：Electron 大文件下载管理怎么设计？多线程分片与断点续传？
**答**：
- 分片下载：HEAD 拿 `Content-Length` 与是否支持 `Range`，按并发数（一般 3-6）切片并行请求，分片结果写临时文件或单文件 `pwrite` 指定偏移，避免内存堆积。
- 断点续传：持久化任务状态（分片完成位图、已写字节数、ETag/Last-Modified 校验服务端资源未变），重启后校验通过即从断点继续；服务端资源变更则整体重下。
- 工程要点：磁盘预分配（`fallocate`/创建等长文件）防碎片写、分片校验（各片 md5 或整体 md5）、失败分片指数退避重试、代理与限速配置透传。
- 进度与 IPC：渲染进程只收聚合进度（主进程 200ms 节流推送），不逐 chunk 跨 IPC；任务列表持久化（XP-102 SQLite）支持管理页恢复展示。
- 降级链路：不支持 Range 时退化为单流下载 +整体断点（已下载字节保留）；网络切换自动暂停恢复。

```javascript
// main/download/manager.js —— 分片 + 断点续传 + 校验
const CONCURRENCY = 4, CHUNK_RETRY = 5;

async function download(task, onProgress) {
  const head = await fetch(task.url, { method: 'HEAD' });
  const total = Number(head.headers.get('content-length'));
  const canRange = head.headers.get('accept-ranges') === 'bytes';
  const etag = head.headers.get('etag');                   // 断点前先校验资源未变

  const state = await db.loadTask(task.id) ?? initTask(task, total, canRange, etag);
  if (state.etag !== etag) resetTask(state);               // 服务端资源已变：整体重下

  await ensureFile(task.filePath, total);                  // 预分配等长文件
  const ranges = planChunks(state, CONCURRENCY);           // 未完成分片队列（含位图）

  await pMap(ranges, async (chunk) => {
    for (let i = 0; i < CHUNK_RETRY; i++) {
      try {
        const res = await fetch(task.url, {
          headers: { Range: `bytes=${chunk.start + chunk.done}-${chunk.end}` },
        });
        await streamToFile(res.body, task.filePath, chunk.start + chunk.done, (n) => {
          chunk.done += n; state.doneBytes += n;
          onProgress(state.doneBytes / total);             // 主进程聚合，节流后推 IPC
        });
        await db.saveChunk(task.id, chunk);                // 分片级持久化：崩溃可续传
        return;
      } catch (e) { await sleep(2 ** i * 500); }           // 指数退避重试
    }
    throw new Error(`chunk ${chunk.index} failed`);
  }, { concurrency: CONCURRENCY });

  await verifyMd5(task.filePath, task.md5);                // 整包校验，失败清位图重下
  await db.finishTask(task.id);
}
// 进度推送：主进程 setInterval 200ms 聚合后 webContents.send，渲染端只做 UI
// 不支持 Range：退化为单流 + 保留已下载字节的伪断点（state.doneBytes 记录）
```
