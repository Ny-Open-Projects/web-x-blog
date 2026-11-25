---
title: [WEB-065] Expect: 100-continue 头是干什么的？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-065：Expect: 100-continue 头是干什么的？
**答**：
- 客户端要发送大体积请求体前，先带 `Expect: 100-continue` 询问服务器是否愿意接收，服务器回 `100 Continue` 后客户端才真正发送 Body。
- 价值：Body 未发出前就能被拒绝（如 401、413），避免白白上传几十 MB 后才收到 4xx，节省带宽。
- curl 对超过 1KB 的 POST 会自动启用该机制；服务器若不支持会在超时后才收 Body，个别老网关因此出兼容问题。
- 前端关联：fetch/XHR 不暴露 Expect 头，大文件上传的分片预检（OPTIONS/HEAD 探测）是应用层的等价方案。

```http
POST /upload HTTP/1.1
Host: api.example.com
Content-Type: video/mp4
Content-Length: 104857600
Expect: 100-continue

HTTP/1.1 100 Continue

（客户端此刻才开始发送 100MB 的请求体）

HTTP/1.1 413 Payload Too Large
Content-Length: 0

（另一种结局：服务器一开始就拒绝，客户端一个字节都不用发）
```
