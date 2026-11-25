---
title: [WEB-271] 反向代理与正向代理的区别？Nginx 在前端的角色
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 网络]
type: 面试题
---

## WEB-271：反向代理与正向代理的区别？Nginx 在前端的角色

**答**：
- 正向代理：代理「客户端」，服务端不知道真实客户端（VPN、翻墙）；反向代理：代理「服务端」，客户端不知道后面有几台机器（Nginx、CDN、负载均衡）。
- Nginx 在前端的四大角色：静态资源服务（高效文件服务）、API 反向代理（把 /api 转发到后端，顺带解决开发与生产的跨域）、负载均衡（upstream 轮询/权重/ip_hash）、HTTPS 终结与缓存。
- 前端高频配置：history 路由 try_files 兜底到 index.html、gzip/brotli、cache-control 头下发、CORS 头。
- 常见坑：SPA history 模式刷新 404 就是漏配 try_files；WebSocket 需要 proxy_set_header Upgrade。

```nginx
location / {
  try_files $uri $uri/ /index.html;      # history 路由兜底
}
location /api/ {
  proxy_pass http://backend:8080/;       # 反代后端，同源消灭 CORS
  proxy_set_header Host $host;
  proxy_set_header X-Real-IP $remote_addr;
}
location /ws {
  proxy_http_version 1.1;
  proxy_set_header Upgrade $http_upgrade;
  proxy_set_header Connection "upgrade"; # WebSocket 透传
}
```
