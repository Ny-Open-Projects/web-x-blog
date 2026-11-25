---
title: [OPS-105] CORS 收口到 nginx 网关层要注意什么？add_header 和 OPTIONS 预检有哪些坑？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-105：CORS 收口到 nginx 网关层要注意什么？add_header 和 OPTIONS 预检有哪些坑？
**答**：
- CORS 统一在网关处理、业务代码不再各自设置，避免重复头导致浏览器报"multiple values"。
- 带凭证（cookie）时 Access-Control-Allow-Origin 不能是 *，必须按白名单回显具体 Origin；白名单用 map 管理而非 if。
- add_header 的继承陷阱：location 里出现任意 add_header，http/server 层的同名指令全部失效，所以 CORS 头要写在同一层级。
- 响应因 Origin 不同而不同，必须回 Vary: Origin，否则 CDN/代理可能把 A 站点的 CORS 头缓存给 B 站点（OPS-115 同源坑）。
- OPTIONS 预检在网关层直接 204 短路，不打到应用；Access-Control-Max-Age 让浏览器缓存预检结果减少预检请求。

```nginx
# CORS 统一网关层处理
map $http_origin $cors_origin {
    default "";
    "~^https://(www|app)\.example\.com$"  $http_origin;   # 白名单回显 Origin
}
map $http_origin $cors_credentials {
    default "false";
    "~^https://(www|app)\.example\.com$"  "true";
}

server {
    location /api/ {
        # 注意：location 内的 add_header 会使外层同名指令失效，CORS 头集中在此维护
        add_header Access-Control-Allow-Origin      $cors_origin      always;
        add_header Access-Control-Allow-Credentials $cors_credentials always;
        add_header Vary "Origin" always;   # 按 Origin 分桶缓存，CDN 场景必加

        # OPTIONS 预检网关层短路，不透传应用
        if ($request_method = OPTIONS) {
            add_header Access-Control-Allow-Origin  $cors_origin always;
            add_header Access-Control-Allow-Methods "GET, POST, PUT, DELETE, OPTIONS" always;
            add_header Access-Control-Allow-Headers "Authorization, Content-Type, X-Trace-Id" always;
            add_header Access-Control-Max-Age 86400 always;   # 预检结果浏览器缓存 24h
            add_header Content-Length 0;
            return 204;
        }

        proxy_pass http://app_backend;
    }
}
```
