---
title: [WEB-297] 部署 HTTP/3 服务端需要配什么？有哪些坑？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP3]
type: 面试题
---

## WEB-297：部署 HTTP/3 服务端需要配什么？有哪些坑？
**答**：
- 基础项：UDP 443 监听 + 证书 + Alt-Svc 响应头；Nginx 需要 1.25+ 且 --with-http_v3_module，Caddy 默认开 h3 最省事。
- 常见坑：reuseport 端口被多 worker 抢占要配 quic_reuseport；证书变更后 QUIC 侧不热加载要重启；UDP 被 QoS 时指标反而差，要盯 p99 而不是均值。
- 灰度建议：先 Alt-Svc 短 max-age 给 1% 流量，对比 TTFB/丢包指标再全量。

```javascript
# Nginx 1.25+ 最小配置
# server {
#   listen 443 quic reuseport;
#   listen 443 ssl;
#   http2 on;
#   ssl_protocols TLSv1.3;
#   add_header Alt-Svc 'h3=":443"; ma=86400' always;
#   quic_retry on;                # 反放大攻击
# }
console.log('UDP443 + Alt-Svc + TLS1.3 是 h3 三件套');
```
