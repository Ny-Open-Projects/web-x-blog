---
title: [OPS-038] 大文件上传经 Nginx 代理要注意什么？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-038：大文件上传经 Nginx 代理要注意什么？
**答**：
- 默认 client_max_body_size 1m，超过直接 413，前端表现是"上传大文件必失败"，必须按业务放大（如 100m~1g）。
- 三个超时都要放大：client_body_timeout（客户端传 body 间隙）、proxy_send_timeout、proxy_read_timeout。
- 开启 client_body_temp_path 所在磁盘要够；proxy_request_buffering off 可让 Nginx 流式转发不落盘，降低延迟与磁盘压力。
- 分片上传才是根治方案：单分片控制在 5~10m，配合断点续传；Nginx 层面只需保证分片尺寸上限。

```nginx
# 上传通道：独立 location 精细化配置，不影响常规接口
server {
    listen 443 ssl http2;
    server_name www.example.com;

    # 普通接口保持默认小体积，防止误传大 body 占用资源
    location /api/ {
        client_max_body_size 2m;
        proxy_pass http://api_backend;
    }

    # 分片上传接口：单分片 10m
    location /api/upload/chunk {
        client_max_body_size 16m;            # 分片 + 冗余
        client_body_timeout   120s;          # 弱网上传间隔容忍
        client_body_buffer_size 256k;

        proxy_pass              http://api_backend;
        proxy_request_buffering off;         # 流式转发，不在 Nginx 落盘
        proxy_connect_timeout   5s;
        proxy_send_timeout      300s;        # 大分片慢速上传
        proxy_read_timeout      300s;
    }

    # 直传对象存储的预签名场景：只放大超时，URL 由后端签发，Nginx 仅转发
    location /oss-upload/ {
        client_max_body_size 1024m;
        proxy_pass https://bucket.oss.example.com/;
        proxy_set_header Host bucket.oss.example.com;
        proxy_read_timeout 600s;
        proxy_send_timeout 600s;
    }

    error_page 413 /413.json;
    location = /413.json {
        return 429 '{"code":"FILE_TOO_LARGE","msg":"文件超过大小限制"}';
    }
}
```
