---
title: [OPS-028] 跨域与 Cookie 域如何设计？主域共享登录态怎么做？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-028：跨域与 Cookie 域如何设计？主域共享登录态怎么做？
**答**：
- 最省事的方案是"同域反代"：前端 www.example.com、接口 www.example.com/api/，天然无跨域，Cookie 直接可用。
- 接口独立域名（api.example.com）时：后端 Set-Cookie 的 Domain 设为主域 example.com，前后端都带 Domain=.example.com 的 Cookie 即可共享登录态；CORS 需配置允许来源与 Allow-Credentials。
- 注意 SameSite=Lax/Strict 跨站限制：跨子域属于同站（site）不受影响；跨主域（mall.com 与 pay.com）则必须 SameSite=None; Secure 并注意第三方 Cookie 政策。
- 多站点（www/m/admin）登录态复用：Token 类方案放主域存储或统一认证中心（SSO）跳换取票。

```nginx
# 方案 A（推荐）：同域反代，无跨域问题
server {
    listen 443 ssl http2;
    server_name www.example.com;

    # 前端静态
    location / {
        root /data/web/current;
        try_files $uri $uri/ /index.html;
    }

    # 接口同域转发：浏览器视角全程 www.example.com
    location /api/ {
        proxy_pass http://api_backend/;
        proxy_set_header Host api.internal:8080;
        proxy_cookie_domain api.internal www.example.com;   # 后端 Cookie 域改写
        proxy_cookie_path / "/; SameSite=Lax; Secure";
    }
}

# 方案 B：接口独立域名时，CORS + 主域 Cookie 的关键响应头
# add_header Access-Control-Allow-Origin "https://www.example.com" always;
# add_header Access-Control-Allow-Credentials "true" always;
# 后端 Set-Cookie: session=xxx; Domain=.example.com; Path=/;
#                Secure; HttpOnly; SameSite=Lax; Max-Age=604800
```

---

## 四、Nginx 实战（OPS-029 ~ OPS-040）

Nginx 是前端上线最常打交道的服务器。面试重点不是背指令，而是理解每段配置解决什么线上问题：路由回退、缓存、限流、代理、安全头，以及出问题时如何从配置定位原因。
