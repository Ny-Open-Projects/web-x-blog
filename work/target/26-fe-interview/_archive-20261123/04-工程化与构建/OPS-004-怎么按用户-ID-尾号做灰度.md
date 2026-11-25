---
title: [OPS-004] 怎么按"用户 ID 尾号"做灰度？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-004：怎么按"用户 ID 尾号"做灰度？
**答**：
- 尾号灰度的好处是天然均匀且用户感知稳定：同一用户始终落在同一批次，不会今天新版明天旧版。
- 依赖登录态里可读的 uid（一般在 Cookie 或网关注入的 Header 中），用正则取最后一位数字。
- Nginx 用两级 map：第一级用正则提取尾号，第二级把尾号映射到版本；放量就是逐步扩大尾号区间。
- 注意未登录用户没有 uid，默认归入旧版本，登录后再按尾号分流。

```nginx
# 从 Cookie 的 uid 提取尾号，再映射版本：放量时改第二张 map 即可
map $cookie_uid $uid_tail {
    default      "-1";          # 未登录统一旧版
    ~(\d)$       $1;            # 取 uid 最后一位数字
}

map $uid_tail $gray_root {
    default      /data/web/v1;  # 其余尾号走旧版
    "0"          /data/web/v2;  # 第一批：尾号 0
    "1"          /data/web/v2;  # 第二批放量：尾号 0、1
    "2"          /data/web/v2;
    "3"          /data/web/v2;
    "4"          /data/web/v2;
    "5"          /data/web/v2;
    "6"          /data/web/v2;
    "7"          /data/web/v2;
    "8"          /data/web/v2;  # 全量：0 到 9
    "9"          /data/web/v2;
}

server {
    listen 80;
    server_name www.example.com;
    location / {
        root $gray_root;
        try_files $uri $uri/ /index.html;
    }
}
```
