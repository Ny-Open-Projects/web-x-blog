---
title: [NODE-245] PM2 与 systemd、Nginx 的部署组合？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-245：PM2 与 systemd、Nginx 的部署组合？
**答**:
- 三层组合：systemd/pm2（进程守护层）→ PM2 cluster（多核层）→ Nginx（LB+静态+限流层）。
- systemd 替代方案：`systemd --user` + ExecStart=node server + Restart=always——容器外更简单的进程守护（省 daemon）；多核仍需 cluster 内建。
- Nginx 层职责清单：TLS 终结、静态资源、gzip/br、限流（limit_req）、灰度路由（ARC-276 服务端版）。
- 探针链路：K8s probe 或 Nginx health check → PM2 health → 应用 /health（ELU+依赖检查 NODE-28x）。

```nginx
# Nginx 层
upstream node_api {
  server 127.0.0.1:3000;   # PM2 cluster 单端口（cluster 共享）
  # fork 模式多端口：
  # server 127.0.0.1:3001; server 127.0.0.1:3002; least_conn;
}
server {
  location /api/ { proxy_pass http://node_api; proxy_http_version 1.1; proxy_set_header Connection ""; }
  limit_req zone=api burst=100 nodelay;
  location /assets/ { root /var/www; expires 1y; add_header Cache-Control immutable; }
}
```
