---
title: [OPS-003] 如何基于 Cookie 或 Header 做定向灰度（内部员工/白名单用户先体验）？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-003：如何基于 Cookie 或 Header 做定向灰度（内部员工/白名单用户先体验）？
**答**：
- 定向灰度是"指定谁用新版"而不是"多少比例用新版"，用于内部 dogfooding 和种子用户验证。
- 常见载体：登录后下发的灰度 Cookie（如 gray=v2）、特定 Header（网关注入 x-gray-tag）、或白名单 uid 集合。
- Nginx 用 map 把 Cookie/Header 值映射到不同 root 或 upstream，避免散落的 if 判断。
- 前端在监控上报里带上同一标记，保证灰度数据可归因。

```nginx
# 按 Cookie 决定默认版本目录
map $cookie_gray $gray_by_cookie {
    default  /data/web/v1;      # 默认走旧版
    "v2"     /data/web/v2;      # Cookie gray=v2 命中灰度
}
# 网关/Header 优先：header 有值用 header 的目录，否则回落看 Cookie
map $http_x_gray_tag $gray_root {
    default  $gray_by_cookie;
    "v2"     /data/web/v2;
}

server {
    listen 80;
    server_name www.example.com;

    location / {
        root $gray_root;
        index index.html;
        try_files $uri $uri/ /index.html;
    }
}
```
