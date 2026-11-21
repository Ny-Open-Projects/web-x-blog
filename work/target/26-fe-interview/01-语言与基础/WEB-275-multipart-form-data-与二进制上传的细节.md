---
title: [WEB-275] multipart/form-data 与二进制上传的细节
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP]
type: 面试题
---

## WEB-275：multipart/form-data 与二进制上传的细节

**答**：
- multipart 报文结构：boundary 分隔每部分，每部分有自己的头（Content-Disposition: form-data; name/file; filename）。不能手动设 Content-Type（浏览器自动生成 boundary），否则服务端解析失败。
- FormData 与 fetch：直接传 FormData，Content-Type 让浏览器补全；axios 同理。
- 大文件优化：切片并行上传（每片独立 multipart 或纯二进制 PUT），进度用 XMLHttpRequest.upload.onprogress 或 fetch + ReadableStream 统计。
- 纯二进制上传（无 multipart）：body 直接是文件二进制，Content-Type 用文件的 MIME 或 application/octet-stream，服务端按流接收，开销最小，对象存储（S3/OSS PUT）都是这种。

```javascript
// 分片并行上传
async function uploadChunked(file) {
  const size = 4 * 1024 * 1024;
  const total = Math.ceil(file.size / size);
  await Promise.all(Array.from({ length: total }, (_, i) => {
    const blob = file.slice(i * size, (i + 1) * size);
    const fd = new FormData();
    fd.append('index', i); fd.append('file', blob, file.name + '.part' + i);
    return fetch('/upload/chunk', { method: 'POST', body: fd });
  }));
  return fetch('/upload/merge', { method: 'POST',
    body: JSON.stringify({ name: file.name, total }) });
}
```
