---
title: [PER-045] 什么是中间人攻击？HTTPS 和 HSTS 如何防御？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-045：什么是中间人攻击？HTTPS 和 HSTS 如何防御？

**答**：
- 中间人攻击（MITM）：攻击者位于用户与服务器之间窃听或篡改流量，典型场景是公共 WiFi、DNS 劫持、HTTP 响应注入广告或脚本。
- HTTPS（TLS）通过证书校验 + 非对称握手 + 对称加密，保证传输的机密性与完整性。
- HSTS：`Strict-Transport-Security` 强制浏览器一段时间内只用 HTTPS 访问，防止用户首次访问被 301 剥离的降级攻击。
- 加固：只启用 TLS 1.2/1.3、`includeSubDomains` 覆盖子域、提交 preload 列表、证书到期监控。

```nginx
# 所有 HTTP 请求 301 到 HTTPS
server {
    listen 80;
    server_name example.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name example.com;

    # HSTS：强制浏览器一年内只走 HTTPS，包含子域名，可申请进入预加载列表
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;

    # 仅启用安全版本 TLS
    ssl_protocols TLSv1.2 TLSv1.3;
}
```
