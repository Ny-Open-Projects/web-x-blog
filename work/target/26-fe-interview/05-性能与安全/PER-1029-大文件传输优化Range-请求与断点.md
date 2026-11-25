---
title: [PER-1029] 大文件传输优化：Range 请求与断点续传
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1029：大文件传输优化：Range 请求与断点续传

**答**：
- 视频/大文件用 Range 分片拉取：服务器支持 Accept-Ranges: bytes，客户端带 Range 头按需取片段。
- 断点续传：记录已下载偏移，失败/中断后从 offset 继续；配合 ETag 校验资源未变（变了则重传）。
- 并行分片：把文件切成 N 片并行下载（限并发），完成后合并——下载器核心逻辑。
- 深水：服务端要正确处理 206 响应与 multipart range；CDN 需开启 range 缓存，否则每次回源拉全量。

```javascript
async function rangedDownload(url, { chunk = 1024 * 1024, onProgress } = {}) {
  const head = await fetch(url, { method: 'HEAD' });
  const total = +head.headers.get('Content-Length');
  const etag = head.headers.get('ETag');
  const parts = [];
  for (let start = 0; start < total; start += chunk) {
    const end = Math.min(start + chunk, total) - 1;
    const r = await fetch(url, { headers: { Range: `bytes=${start}-${end}` } });
    if (r.status !== 206) throw new Error('range not supported');
    if (r.headers.get('ETag') && r.headers.get('ETag') !== etag)
      throw new Error('resource changed');            // 中途变更，重传
    parts.push(await r.arrayBuffer());
    onProgress?.(end + 1, total);
  }
  return new Blob(parts);
}
```
