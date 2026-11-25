---
title: [PER-042] 什么是 CSP？如何配置 CSP 头？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-042：什么是 CSP？如何配置 CSP 头？

**答**：
- CSP（Content Security Policy）通过响应头声明**允许加载的资源来源**，浏览器拒绝执行策略外的内联脚本与外域脚本，即使注入成功也执行不了。
- 关键指令：`default-src` 默认来源、`script-src` 脚本、`style-src` 样式、`img-src` 图片、`connect-src` XHR/fetch 目标、`frame-ancestors` 反点击劫持。
- 尽量避免 `'unsafe-inline'`（允许内联脚本会让 CSP 对 XSS 防护大打折扣），脚本外置或加 nonce。
- 上线先配 `Content-Security-Policy-Report-Only` 观察一段时间，确认无误报再强制。

```nginx
server {
    listen 443 ssl;
    server_name example.com;

    # CSP：脚本只允许自身与指定 CDN，禁止内联脚本，违规上报到 /csp-report
    add_header Content-Security-Policy "default-src 'self'; script-src 'self' https://cdn.example.com; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; connect-src 'self' https://api.example.com; frame-ancestors 'none'; report-uri /csp-report" always;

    location / {
        root /var/www/html;
    }
}
```
