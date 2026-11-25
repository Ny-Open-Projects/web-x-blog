---
title: [OPS-101] Nginx 性能调优从哪些参数入手？worker_processes、keepalive、缓冲区怎么配？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-101：Nginx 性能调优从哪些参数入手？worker_processes、keepalive、缓冲区怎么配？
**答**：
- worker_processes auto 按 CPU 核数起 worker，worker_connections 调到 10240+，理论并发 ≈ worker 数 × connections（反代时要打折）。
- 上游长连接最易漏：upstream 配 keepalive 32 的同时必须 proxy_http_version 1.1 + proxy_set_header Connection ""，否则配置无效，每次请求都重建 TCP。
- 缓冲区三件套：proxy_buffers（响应体内存缓冲）、proxy_buffer_size（响应头）、proxy_busy_buffers_size，避免大响应频繁落盘。
- 静态文件走 sendfile + tcp_nopush 零拷贝；worker_rlimit_nofile 与系统 ulimit 对齐，否则改了 connections 仍报 too many open files。
- 调优必须压测验证：wrk 对比 QPS/P99，同时观察 TIME_WAIT 数量与 CPU 上下文切换。

```nginx
# /etc/nginx/nginx.conf：生产级性能基线
user  www-data;
worker_processes auto;              # 等于 CPU 核数
worker_rlimit_nofile 65535;         # 每个 worker 可打开文件数上限，需与 ulimit 对齐

events {
    worker_connections  10240;      # 单 worker 并发连接数
    multi_accept on;                # 一次性接收完积压的新连接
    use epoll;                      # Linux 事件模型
}

http {
    sendfile on;
    tcp_nopush on;                  # sendfile 时合并响应头与数据块
    tcp_nodelay on;                 # keepalive 连接不攒小包
    keepalive_timeout 65;           # 客户端侧长连接存活时间
    keepalive_requests 1000;        # 单连接最多请求数，防连接内存滞留

    # 反代到 Node/网关时启用上游长连接（最常见遗漏项）
    upstream app {
        server 127.0.0.1:3000;
        keepalive 32;               # 与上游保持的空闲长连接数
    }

    server {
        location / {
            proxy_pass http://app;
            proxy_http_version 1.1;             # keepalive 要求 1.1
            proxy_set_header Connection "";     # 清空 Connection 才能复用连接
            proxy_buffers 16 16k;               # 响应体内存缓冲
            proxy_buffer_size 32k;              # 首包（响应头）缓冲
            proxy_busy_buffers_size 64k;        # 忙碌缓冲上限，超出落盘
        }
    }
}
```
