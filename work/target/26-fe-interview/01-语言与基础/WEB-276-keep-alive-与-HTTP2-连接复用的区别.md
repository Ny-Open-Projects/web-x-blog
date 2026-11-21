---
title: [WEB-276] keep-alive 与 HTTP/2 连接复用的区别
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP]
type: 面试题
---

## WEB-276：keep-alive 与 HTTP/2 连接复用的区别

**答**：
- HTTP/1.1 keep-alive：TCP 连接不关闭可复用，但一次只能一个请求在途（串行），下一个请求要等上一个响应完——复用的是「连接」不是「带宽」。
- HTTP/2 多路复用：一条连接上多个 stream 并发在途，帧级交错，不用排队等前一个响应。
- 所以 HTTP/1.1 时代有「域名分片」（开多个域骗浏览器多开连接）的优化，HTTP/2 下反而有害（多连接浪费且降低 HPACK 效率），应该合并域名。
- 连接空闲超时：服务端 keepalive_timeout（Nginx 默认 75s）内没新请求就关连接，前端会碰到「连接被关闭→自动重试」，跨端开发要注意。

```bash
# 观察 keep-alive
curl -sv https://example.com -o /dev/null https://example.com/2 -o /dev/null 2>&1 \
  | grep -i 're-using'
# 第二次请求: Re-using existing connection — HTTP/2 复用
```
