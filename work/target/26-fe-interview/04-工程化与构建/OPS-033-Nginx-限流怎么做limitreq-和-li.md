---
title: [OPS-033] Nginx 限流怎么做？limit_req 和 limit_conn 的区别是什么？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-033：Nginx 限流怎么做？limit_req 和 limit_conn 的区别是什么？
**答**：
- limit_conn 限制并发连接数，防单 IP 大量并发占满资源；limit_req 按速率限制（漏桶算法），防突发流量，两者通常配合使用。
- limit_req_zone 的 rate 是平均速率，burst 允许排队突增，nodelay 表示突发请求立即处理不排队；不配 burst 会把正常突发也拒掉。
- 白名单要先行：内网、健康检查、拨测 IP 必须放行（geo + map 组合），否则监控系统自己触发限流造成误报。
- 被限流要返回 429 并带上 Retry-After，前端可据此提示用户而不是静默失败。

```nginx
# 限流三段式：定义 zone -> 白名单豁免 -> 应用到 location
geo $limit_exempt {
    default         0;
    10.0.0.0/8      1;     # 内网
    192.168.0.0/16  1;     # 办公网
    10.0.3.100      1;     # 拨测机
}
map $limit_exempt $limit_key {
    0   $binary_remote_addr;
    1   "";                # 白名单 key 为空 = 不限流
}

# 速率：单 IP 每秒 20 个请求，内存 10m 约可跟踪 16 万 IP
limit_req_zone  $limit_key  zone=req_perip:10m  rate=20r/s;
limit_conn_zone $limit_key  zone=conn_perip:10m;

# 全站级别：按 server 维度再兜一层，防海量分布式 IP
limit_req_zone  $server_name zone=req_global:10m rate=5000r/s;

server {
    listen 80;
    server_name www.example.com;

    # 接口：单 IP 20r/s，允许 10 个突发立即处理，超出 429
    location /api/ {
        limit_req  zone=req_perip burst=10 nodelay;
        limit_req  zone=req_global burst=1000 nodelay;
        limit_conn conn_perip 20;
        limit_req_status 429;
        limit_conn_status 429;

        proxy_pass http://api_backend;
    }

    # 静态资源限流放宽，避免页面并发加载被误伤
    location /assets/ {
        limit_req zone=req_perip burst=100 nodelay;
    }
}
```
