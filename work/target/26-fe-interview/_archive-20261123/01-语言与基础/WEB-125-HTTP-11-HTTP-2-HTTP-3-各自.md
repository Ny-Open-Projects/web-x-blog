---
title: [WEB-125] HTTP/1.1、HTTP/2、HTTP/3 各自解决了什么、又引入了什么新问题？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-125：HTTP/1.1、HTTP/2、HTTP/3 各自解决了什么、又引入了什么新问题？
**答**：
- 1.1：文本协议、keep-alive 复用连接、Host/缓存协商成熟；遗留队头阻塞与 6 连接限制，前端靠域名分片、雪碧图硬扛。
- 2：二进制分帧 + 多路复用解决应用层队头阻塞，头部压缩 HPACK 与流优先级提升效率；但 TCP 层队头阻塞仍在——一个包丢全连接等待，复用越狠受害面越大。
- 3：QUIC 把传输搬到 UDP，流间独立丢包恢复消除传输层队头阻塞，握手 1-RTT/0-RTT，连接迁移（换网不断连）；代价是 UDP 被限速/拦截的网络要回退、CPU 加解密成本更高。
- 面试收束：协议演化主线是"消灭排队"——从连接排队（1.1）到流排队（2）到无排队（3），每代都换了排队发生的位置。

```nginx
# 同一台 nginx 同时提供 HTTP/1.1 / 2 / 3 服务
server {
    listen 443 ssl;
    http2 on;                 # HTTP/2 over TLS
    listen 443 quic reuseport;# HTTP/3 over QUIC
    ssl_protocols TLSv1.2 TLSv1.3;

    add_header Alt-Svc 'h3=":443"; ma=86400';  # 告知浏览器可用 h3，下次请求升级
    # 客户端首次仍走 h2，拿到 Alt-Svc 后尝试 QUIC
    # QUIC 被网络拦截时浏览器自动回退 h2，业务无感
}
```
