---
title: [DP-246] 源码识别：前端网关层（Nginx/边缘函数）中的策略路由？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-246：源码识别：前端网关层（Nginx/边缘函数）中的策略路由？
**答**:
- 策略链：location 匹配（精确 → 前缀 → 正则）是一条策略链，第一个命中者处理请求——DP 模式在运维配置里的投影。
- 代理模式：proxy_pass 把请求代理到后端（静态资源 CDN/接口网关），网关是"访问控制的代理"。
- 命令式改写：rewrite/redirect 是请求改写命令；灰度路由（ARC-276）在网关层实现"决策即配置"。
- 识别要点：面试问"静态资源 404 排查"时能说出 Nginx 的 try_files 链（fallback 策略）与 SPA history 模式配置。

```nginx
# 策略链 + 代理 + fallback
location ~ ^/assets/ {
  expires 1y;
  add_header Cache-Control "public, immutable";
  try_files $uri @cdn;                    # 本地优先 → CDN fallback（策略链）
}
location @cdn {
  proxy_pass https://cdn.example.com;     # 代理模式
}
location / {
  try_files $uri /index.html;             # SPA history：fallback 到入口
}
# 灰度决策（边缘函数版）：
# if ($cookie_gray_bucket ~ "^v2") { root /builds/v2; } else { root /builds/v1; }
```
