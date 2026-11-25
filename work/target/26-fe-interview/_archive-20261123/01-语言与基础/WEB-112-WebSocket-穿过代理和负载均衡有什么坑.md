---
title: [WEB-112] WebSocket 穿过代理和负载均衡有什么坑？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-112：WebSocket 穿过代理和负载均衡有什么坑？
**答**：
- 反向代理默认按 HTTP 短请求处理，必须显式配置 Upgrade/Connection 头透传并把 read timeout 调大，否则连接被网关定时掐断。
- 负载均衡要支持粘性会话：握手后的帧不再有 HTTP 语义，普通轮询 LB 无法把同一连接的多帧转回同一路由，长连接级 LB 按连接哈希即可。
- 应用层心跳是保活刚需：云 LB 空闲超时（常见 60s）内没有数据就断连，心跳间隔要小于它。
- 水平扩展时跨节点广播要靠 Redis pub/sub 之类外部总线，单机内存里的连接表撑不起多实例。

```nginx
# nginx 反向代理 WebSocket 的完整配置
map $http_upgrade $connection_upgrade {
    default upgrade;
    ''      close;   # 无升级头时按普通请求处理
}
upstream ws_backend {
    server 127.0.0.1:3001;
    server 127.0.0.1:3002;
    # 同一连接始终落在同一节点（按连接分配，天然粘性）
}
server {
    location /ws/ {
        proxy_pass http://ws_backend;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;               # 关键：透传升级头
        proxy_set_header Connection $connection_upgrade;
        proxy_read_timeout 300s;                              # 大于应用心跳间隔
        proxy_send_timeout 300s;
    }
}
```
