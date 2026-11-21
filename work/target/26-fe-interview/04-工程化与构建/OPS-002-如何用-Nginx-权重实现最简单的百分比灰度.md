---
title: [OPS-002] 如何用 Nginx 权重实现最简单的百分比灰度？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-002：如何用 Nginx 权重实现最简单的百分比灰度？
**答**：
- 用两个 upstream（旧版本 v1、新版本 v2）分别指向不同发布目录或不同实例组，通过 weight 控制流量比例。
- weight 是无状态的按连接分配，同一用户可能一次命中新版本一次命中旧版本，所以只适合"前后端资源已 hash 隔离、无状态依赖"的场景。
- 放量过程就是改 weight 并 reload，权重调整可以脚本化（改配置 + nginx -s reload）。
- 配合 $request_id 或 cookie 粘住用户可以避免"灰度跳变"，见下一题的定向灰度方案。

```nginx
# /etc/nginx/conf.d/gray.conf
upstream web_v1 {
    server 10.0.1.11:8080;
    server 10.0.1.12:8080;
}
upstream web_v2 {
    server 10.0.2.11:8080;
}

server {
    listen 80;
    server_name www.example.com;

    location / {
        # 灰度放量时按比例调整两边的 weight：10% 时改 weight=9 对 weight=1
        proxy_pass http://gray_pool;
        include /etc/nginx/conf.d/proxy_common.conf;
    }
}

# 灰度池：初始 95:5，放量阶段按 90:10、80:20 递增
upstream gray_pool {
    server 10.0.1.11:8080 weight=95;  # v1 旧版本
    server 10.0.1.12:8080 weight=95;  # v1 旧版本
    server 10.0.2.11:8080 weight=10;  # v2 新版本
}
```
