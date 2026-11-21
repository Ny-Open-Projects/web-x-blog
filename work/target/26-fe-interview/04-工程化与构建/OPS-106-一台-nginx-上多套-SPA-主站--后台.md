---
title: [OPS-106] 一台 nginx 上多套 SPA（主站 + 后台 + 门户）共存怎么配路由？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-106：一台 nginx 上多套 SPA（主站 + 后台 + 门户）共存怎么配路由？
**答**：
- 每个应用占一个 URL 前缀（/admin、/portal），资源构建时配置 publicPath 对应前缀，index 入口互不干扰。
- alias 与 try_files 组合有斜杠陷阱：alias 末尾必须有 /，try_files 回落写完整前缀入口 /admin/index.html。
- 各应用静态资源统一挂 /static/{app}/ 走 immutable 长缓存；入口 html no-cache。
- 应用间跳转走完整路径而非相对路径，避免嵌套路由解析错位；路由 base 与 nginx 前缀保持一致。
- 加新应用只需加一段 location，不影响既有应用；域名收敛还省证书与 CORS 配置。

```nginx
# 多 SPA 共存：/admin 与 /portal 各自路由，全部 history 模式
server {
    root /data/web/current;

    location /admin/ {
        alias /data/web/current/admin/;      # alias 结尾斜杠必须与 location 一致
        index index.html;
        try_files $uri $uri/ /admin/index.html;   # 回落写全前缀，防止串到主站入口
    }

    location /portal/ {
        alias /data/web/current/portal/;
        index index.html;
        try_files $uri $uri/ /portal/index.html;
    }

    # 主站 SPA
    location / {
        try_files $uri $uri/ /index.html;
    }

    # 各应用 hash 资源统一长缓存
    location /static/ {
        expires max;
        add_header Cache-Control "public, immutable";
    }
}
```
