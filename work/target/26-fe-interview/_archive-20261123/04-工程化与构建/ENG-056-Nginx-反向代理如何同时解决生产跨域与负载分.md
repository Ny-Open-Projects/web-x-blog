---
title: [ENG-056] Nginx 反向代理如何同时解决生产跨域与负载分发？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-056：Nginx 反向代理如何同时解决生产跨域与负载分发？
**答**：
- 前端与 API 同域名，/api 前缀由 Nginx 转发到后端服务，浏览器视角全是同源，跨域消失。
- proxy_pass 末尾带 / 会去掉 location 前缀，注意与后端路由约定一致。
- 透传 X-Real-IP、X-Forwarded-For 让后端拿到真实客户端 IP。
- upstream 可配多台后端做轮询负载，配合 max_fails 剔除故障节点。

```nginx
upstream backend {
  server backend1:8080;
  server backend2:8080;
}

server {
  listen 80;

  # /api 转发到后端集群，同时解决生产跨域
  location /api/ {
    proxy_pass http://backend/;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_read_timeout 60s;
  }
}
```

---

## 第十四章 前端监控（ENG-057 ~ ENG-058）
