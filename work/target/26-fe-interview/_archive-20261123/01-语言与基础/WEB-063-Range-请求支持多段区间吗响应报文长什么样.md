---
title: [WEB-063] Range 请求支持多段区间吗？响应报文长什么样？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-063：Range 请求支持多段区间吗？响应报文长什么样？
**答**：
- 支持。`Range: bytes=0-1023, 4096-5119` 一次请求多个区间，服务器返回 `206 Partial Content`，Body 是 `multipart/byteranges` 多段结构。
- 每一段都有独立的 `Content-Type` 和 `Content-Range: bytes 起始-结束/总长`，段之间用 boundary 分隔。
- 典型场景：视频播放器同时拉取片头 moov box 和当前播放位置；下载器并行拉取多个分片。
- 服务器可以忽略多段请求返回完整 `200`，客户端必须兼容两种响应。

```http
GET /video.mp4 HTTP/1.1
Host: cdn.example.com
Range: bytes=0-1023, 4096-5119

HTTP/1.1 206 Partial Content
Content-Type: multipart/byteranges; boundary=FRONT3ND
Content-Length: 2312

--FRONT3ND
Content-Type: video/mp4
Content-Range: bytes 0-1023/1048576

（1024 字节二进制数据）
--FRONT3ND
Content-Type: video/mp4
Content-Range: bytes 4096-5119/1048576

（1024 字节二进制数据）
--FRONT3ND--
```
