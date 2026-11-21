---
title: [OPS-115] CORS 走 CDN 有什么坑？为什么必须回 Vary: Origin？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-115：CORS 走 CDN 有什么坑？为什么必须回 Vary: Origin？
**答**：
- 坑一：源站返回固定 CORS 头 + CDN 缓存了首个用户的响应 → 后续所有用户共享同一个 Access-Control-Allow-Origin，其他域名下资源被浏览器拒绝。
- 坑二：CDN 层与源站层重复添加 CORS 头，浏览器报 multiple values 错误——必须在 CDN 层 hide 源站头后统一注入。
- 正确姿势：CDN 按白名单 map 回显 Origin，并强制 Vary: Origin 让缓存按 Origin 分桶；带 cookie 时禁止通配 *。
- OPTIONS 预检响应不能缓存（各源答案不同），对 OPTIONS 直接边缘短路 204。
- 配置变更后用不同 Origin 的 curl 双向验证，再看命中率是否明显下降（分桶会摊薄命中率，属预期）。

```nginx
# CDN/代理层的 CORS 正确处理
map $http_origin $allow_origin {
    default                    "";
    "https://www.example.com"  $http_origin;
    "https://app.example.com"  $http_origin;
}
map $request_method $is_options {   # 预检请求不进缓存
    "OPTIONS"  1;
    default    0;
}

server {
    location /api/ {
        proxy_pass http://origin_backend;

        # 坑二处理：隐藏源站的 CORS 头，统一由边缘注入，避免重复头
        proxy_hide_header Access-Control-Allow-Origin;
        proxy_hide_header Access-Control-Allow-Credentials;

        add_header Access-Control-Allow-Origin      $allow_origin always;
        add_header Access-Control-Allow-Credentials "true"     always;
        # 坑一处理：响应因 Origin 不同而不同，缓存必须按 Origin 分桶
        add_header Vary "Origin" always;

        proxy_no_cache $is_options;   # OPTIONS 204 各源不同，不缓存
    }
}
```
