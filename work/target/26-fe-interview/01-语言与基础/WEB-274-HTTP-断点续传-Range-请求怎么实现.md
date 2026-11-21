---
title: [WEB-274] HTTP 断点续传：Range 请求怎么实现？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP]
type: 面试题
---

## WEB-274：HTTP 断点续传：Range 请求怎么实现？

**答**：
- 服务器支持检测：HEAD 请求看响应是否带 `Accept-Ranges: bytes`。
- 下载：`Range: bytes=1000000-` 请求剩余部分，服务器回 206 Partial Content + `Content-Range: bytes=1000000-1999999/2000000`。
- 前端并行分片下载：按 Content-Length 切 N 片并发 Range 请求，各自保存到分片文件，全部完成后按顺序拼合（浏览器端可用 Blob 切片写入 IndexedDB）。
- 上传断点续传：分片上传，每片带 index/hash，服务端记录已收分片，中断后查询 missing 分片续传；最后合并校验整体 hash。
- 注意：CDN 要开启 Range 回源，否则回源拉全量浪费；响应不完整用 If-Range 防止文件已变时拼错内容。

```javascript
async function resumableDownload(url) {
  const head = await fetch(url, { method: 'HEAD' });
  const total = +head.headers.get('content-length');
  const chunk = 4 * 1024 * 1024;
  const parts = [];
  for (let start = 0; start < total; start += chunk) {
    const end = Math.min(start + chunk, total) - 1;
    const res = await fetch(url, { headers: { Range: `bytes=${start}-${end}` } });
    if (res.status !== 206) throw new Error('服务器不支持 Range');
    parts.push(await res.arrayBuffer());
  }
  return new Blob(parts);
}
```

**评分点**：
- 知道 206 与 Content-Range 语义
- 分片并发下载/上传合并思路完整
- 提到 If-Range 或整体 hash 校验
