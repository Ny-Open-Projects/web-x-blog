---
title: [BAS-106] HTTP 断点续传怎么实现？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-106：HTTP 断点续传怎么实现？
**答**：
- 客户端带 `Range: bytes=start-end` 请求部分内容，服务端支持时返回 206 Partial Content 和 `Content-Range: bytes start-end/总大小`。
- 靠它实现分片并行下载、失败从断点续传；服务端不支持 Range 时返回 200 全量内容。
- 前端大文件上传同理：按分片切割、逐片传、记录进度，失败只重传失败分片。

```http
GET /video.mp4 HTTP/1.1
Range: bytes=1048576-

HTTP/1.1 206 Partial Content
Content-Range: bytes 1048576-2097151/5242880
Content-Length: 1048576
```
