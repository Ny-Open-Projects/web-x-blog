---
title: [WEB-004] Connection: keep-alive 解决了什么问题？和 HTTP 管道化有什么区别？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-004：Connection: keep-alive 解决了什么问题？和 HTTP 管道化有什么区别？
**答**：
- 短连接下每个请求都要经历 TCP 三次握手（HTTPS 还要 TLS 握手），成本高；keep-alive 让连接保持打开，多个请求复用同一条连接。
- keep-alive 只是连接复用，请求仍然是"发一个、等一个"的串行模式。
- 管道化允许不等响应就连续发出多个请求，但响应必须按请求顺序返回，慢响应仍会堵住后面的，实践问题多、未普及。
- keep-alive 有超时时间，由服务端的 `Keep-Alive: timeout=xx` 控制，超时后连接关闭。

```nginx
# nginx 配置：keep-alive 超时与最大请求数，属于服务端真实工程配置
http {
    keepalive_timeout 65;      # 连接空闲 65 秒后关闭
    keepalive_requests 100;    # 一条连接最多服务 100 个请求

    upstream app {
        server 127.0.0.1:3000;
        keepalive 32;          # 反向代理到上游也复用长连接，减少握手
    }
}
```
