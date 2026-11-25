---
title: [OPS-064] 接口域名策略：同域反代 vs 独立 API 域名怎么选？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-064：接口域名策略：同域反代 vs 独立 API 域名怎么选？
**答**：
- 同域反代（www.example.com/api/）：零跨域、Cookie 简单、CDN/网关统一管控；缺点是前端与接口共享域名容量与缓存策略，网关层多一跳。
- 独立域名（api.example.com）：API 可独立扩缩容、独立安全策略；代价是 CORS 配置、Cookie 主域设计、证书多一套。
- 中大型业务常见折中：页面走 CDN 域名，接口走独立域名但同主域（Cookie 共享），再加一层 API 网关统一鉴权限流。
- 决策因素列表：跨域成本、Cookie 粒度、CDN 缓存冲突（API 被 CDN 误缓存是大事故）、安全边界。

```nginx
# 两种策略的落地配置对照（以 Nginx/Ingress 表达）

# 策略 A：同域反代（默认推荐）
#   前端：https://www.example.com
#   接口：https://www.example.com/api/  ->  proxy 到 api 集群
server {
    listen 443 ssl http2;
    server_name www.example.com;

    location /api/ {
        proxy_pass http://api_gateway;
        proxy_set_header Host $host;                 # 保持同域，后端拿到的就是 www
        add_header Cache-Control "no-store" always;  # 接口绝不进缓存
    }
    location / {
        root /data/web/current;
        try_files $uri $uri/ /index.html;
    }
}

# 策略 B：独立 API 域名（API 独立伸缩与安全边界）
#   接口：https://api.example.com
# server {
#     listen 443 ssl http2;
#     server_name api.example.com;
#     add_header Access-Control-Allow-Origin "https://www.example.com" always;
#     add_header Access-Control-Allow-Credentials "true" always;
#     add_header Access-Control-Allow-Headers "Content-Type, Authorization" always;
#     if ($request_method = OPTIONS) { return 204; }    # 预检快速通过
#     location / { proxy_pass http://api_gateway; }
# }
```
