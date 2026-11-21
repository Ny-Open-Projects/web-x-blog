---
title: [WEB-079] 中间盒和代理为什么会影响 HTTP/2 部署？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-079：中间盒和代理为什么会影响 HTTP/2 部署？
**答**：
- HTTP/2 明文升级（Upgrade: h2c）依赖中间设备放行该头，但大量企业防火墙、老代理会丢弃不认识的头或强行改写，导致明文 h2c 几乎不可用——现实中 HTTP/2 只在 TLS 上部署。
- 反向代理与 LB 若不支持 HTTP/2，会把它降级成 HTTP/1.1 转给上游，多路复用收益消失；nginx 需显式开启对上游的 h2。
- 另一个坑：HTTP/2 连接复用带来"连接合并"，同证书同源的不同域名可能共用连接，影响按域名分流的运维假设。
- QUIC 基于 UDP，部分网络会直接拦截 UDP 443，需要回退 HTTP/2 的降级策略。

```nginx
# nginx：边缘启用 h2，并显式与上游也用 HTTP/2 避免降级
server {
    listen 443 ssl;
    http2 on;
    location / {
        grpc_pass grpcs://backend;      # gRPC 强依赖 HTTP/2
        proxy_http_version 2;           # 到上游也走 h2，需要 upstream 支持
        proxy_set_header Connection ""; # 清空 Connection 头以支持多路复用
    }
}
```
