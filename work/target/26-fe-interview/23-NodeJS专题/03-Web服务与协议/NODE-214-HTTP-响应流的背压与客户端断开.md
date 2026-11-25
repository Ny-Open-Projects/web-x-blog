---
title: [NODE-214] HTTP 响应流的背压与客户端断开？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-214：HTTP 响应流的背压与客户端断开？
**答**:
- 大响应场景：把文件流/上游代理流接到 res（res 是 Writable）——客户端读得慢时 res.write 返回 false，上游必须背压（手工 pipe 裸用常见 OOM 点）。
- 客户端断开：res 的 close 事件 → 上游流必须 destroy，否则上游继续读文件占内存与 fd（NODE-070 分片上传的镜像问题）。
- 实现路径：pipeline(fileStream, res, { signal }) + abortController（req.close 时 abort）。
- 下载断点续传配合 Range：响应流从偏移 start 读（createReadStream(path, { start })），背压交给 pipeline。

```javascript
import { pipeline } from 'node:stream/promises';
import { createReadStream } from 'node:fs';

app.get('/download/:id', async (req, res) => {
  const file = await repo.getFileMeta(req.params.id);
  const range = parseRange(req.headers.range, file.size);
  res.writeHead(range ? 206 : 200, {
    'Content-Length': range?.length ?? file.size,
    'Accept-Ranges': 'bytes',
    ...(range && { 'Content-Range': `bytes ${range.start}-${range.end}/${file.size}` }),
  });
  const ac = new AbortController();
  req.on('close', () => ac.abort());          // 客户端断开 → 取消管道
  await pipeline(
    createReadStream(file.path, { start: range?.start ?? 0, end: range?.end }),
    res,                                      // res 作为可写端：客户端慢 → 自动背压
    { signal: ac.signal },
  ).catch(e => { if (!ac.signal.aborted) log.error(e); });
});
```
