---
title: [WEB-008] HTTP/3 基于 QUIC，相比 HTTP/2 有哪些改进？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-008：HTTP/3 基于 QUIC，相比 HTTP/2 有哪些改进？
**答**：
- 传输层从 TCP 换成 UDP 上的 QUIC：把可靠性、流控、拥塞控制搬进用户态协议，握手集成 TLS 1.3。
- 独立的 Stream 层流控：一个流丢包只重传该流，彻底解决 TCP 层队头阻塞。
- 连接迁移：用 Connection ID 标识连接而非四元组，Wi-Fi 切 4G 不必重新握手。
- 内置 TLS 1.3，握手与传输握手合并，首包即加密；0-RTT 恢复更快。
- 前端感知不大：浏览器与 CDN 配合切换，代码仍然是 fetch。

```nginx
# nginx 1.25+ 开启 HTTP/3 的配置（需要 quic 分支或主线版本）
server {
    listen 443 quic reuseport;          # QUIC 监听（UDP）
    listen 443 ssl http2;               # 同时保留 HTTP/2 走 TCP 兜底
    ssl_certificate     /etc/ssl/cert.pem;
    ssl_certificate_key /etc/ssl/key.pem;
    add_header Alt-Svc 'h3=":443"; ma=86400';  # 告知浏览器可用 HTTP/3
    quic_retry on;
}
```
