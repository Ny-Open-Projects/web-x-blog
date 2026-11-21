---
title: [OPS-037] Nginx 怎么代理 WebSocket？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-037：Nginx 怎么代理 WebSocket？
**答**：
- WebSocket 升级靠 HTTP 101：必须显式转发 Upgrade 与 Connection 头，且用 HTTP/1.1，否则握手失败。
- 长连接场景要放大 read timeout（或配置心跳），否则 Nginx 默认 60s 空闲断链，表现为"聊天几分钟就掉线"。
- 客户端断线重连要有退避策略，服务端配合心跳（ping/pong）维持连接并清理僵尸连接。
- 多实例的 WS 服务必须共享会话（Redis pub/sub）或用 ip_hash 粘住实例，否则广播消息丢失。

```nginx
# WebSocket 代理：/ws 走独立 location
map $http_upgrade $connection_upgrade {
    default upgrade;    # 有 Upgrade 头则升级
    ""      close;      # 普通 http 请求按 close 处理
}

upstream ws_backend {
    ip_hash;                        # 粘住实例，避免多实例广播丢失
    server 10.0.4.11:9501;
    server 10.0.4.12:9501;
}

server {
    listen 443 ssl http2;
    server_name www.example.com;

    location /ws/ {
        proxy_pass http://ws_backend;
        proxy_http_version 1.1;
        proxy_set_header Upgrade    $http_upgrade;          # 关键：升级头
        proxy_set_header Connection $connection_upgrade;    # 关键：连接头
        proxy_set_header Host       $host;
        proxy_set_header X-Real-IP  $remote_addr;

        # 长连接保活：默认 60s 会踢掉空闲 WS，配合客户端心跳设 300s
        proxy_read_timeout  300s;
        proxy_send_timeout  300s;
    }
}
```
