---
title: [OPS-029] SPA history 路由在 Nginx 怎么配？多应用共存怎么处理？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-029：SPA history 路由在 Nginx 怎么配？多应用共存怎么处理？
**答**：
- 核心是 try_files：先找真实文件，找不到回退到该应用的 index.html，由前端路由接管。
- 多个 SPA 共存（主站 /mall、管理台 /admin）时，各自 location 回退各自的入口，避免 404 或回退错应用。
- 回退要区分资源请求与路由请求：带后缀的静态资源缺失应返回 404（暴露问题）而不是回退 html 造成"内容不对但不报错"。
- 子路径部署还要处理前端构建的 base/publicPath 与 Nginx 的 alias 配合。

```nginx
# 单机多 SPA 部署：/ 主站、/admin 管理台、/m 移动端
server {
    listen 80;
    server_name www.example.com;
    root /data/web/current;

    # 主站：文件不存在回退主站入口
    location / {
        index index.html;
        try_files $uri $uri/ /index.html;
    }

    # 管理台子应用：独立目录独立入口
    location /admin/ {
        alias /data/web/current/admin/;
        index index.html;
        try_files $uri $uri/ /admin/index.html;
    }

    # 移动端
    location /m/ {
        alias /data/web/current/m/;
        try_files $uri $uri/ /m/index.html;
    }

    # 静态资源缺失必须 404，不能回退 html 掩盖问题
    location ~* \.(js|css|png|jpg|woff2)$ {
        try_files $uri =404;
        expires 30d;
    }
}
```
