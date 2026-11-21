---
title: [OPS-040] Nginx 层应该加哪些安全响应头？CSP 怎么落地？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-040：Nginx 层应该加哪些安全响应头？CSP 怎么落地？
**答**：
- 基线五件套：CSP、X-Frame-Options（或 CSP frame-ancestors）、X-Content-Type-Options、Referrer-Policy、HSTS。
- CSP 是防 XSS 的纵深手段，落地策略：先 Report-Only 观察上报 → 收敛 inline/style-src → 逐步 enforce； nonce 方案适配现代框架。
- add_header 有继承陷阱：location 内任何 add_header 会覆盖 server 级全部 add_header，公共头要抽 include 文件每处引入。
- 头的值要结合业务：允许的脚本源与 CDN 域名对齐，避免上线即全站报 CSP violation。

```nginx
# /etc/nginx/snippets/security-headers.conf：公共安全头（include 引入，规避继承陷阱）
add_header Content-Security-Policy "default-src 'self';
    script-src 'self' 'nonce-{NONCE}' https://cdn.example.com;
    style-src 'self' 'unsafe-inline' https://cdn.example.com;
    img-src 'self' data: https://*.example.com;
    connect-src 'self' https://api.example.com wss://ws.example.com;
    frame-ancestors 'self';
    report-uri /api/csp-report;" always;

add_header X-Content-Type-Options "nosniff" always;
add_header X-Frame-Options        "SAMEORIGIN" always;
add_header Referrer-Policy        "strict-origin-when-cross-origin" always;
add_header Strict-Transport-Security "max-age=31536000" always;

# server 内使用：
server {
    listen 443 ssl http2;
    server_name www.example.com;

    location / {
        include snippets/security-headers.conf;
        root /data/web/current;
        try_files $uri $uri/ /index.html;
    }

    # CSP 上报接收：先 Report-Only 阶段收集违规样本
    location = /api/csp-report {
        proxy_pass http://api_backend;
        access_log /var/log/nginx/csp_report.log;
    }
}
```

---

## 五、容器与编排（OPS-041 ~ OPS-048）

容器把"在我机器上是好的"变成"在所有机器上是同一个镜像"。前端场景的核心实践：多阶段构建控制镜像体积、启动时注入运行时配置、K8s 侧用探针与滚动更新保证发布无损。
