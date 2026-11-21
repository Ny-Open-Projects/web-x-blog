---
title: [PER-061] CSP 如何与转义、净化组合成 XSS 纵深防御？nonce 模式怎么落地？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-061：CSP 如何与转义、净化组合成 XSS 纵深防御？nonce 模式怎么落地？

**答**：
- 纵深防御三层：**第一层输出转义/净化**（把 99% 的注入变成纯文本）、**第二层 CSP**（即使注入成功也禁止内联脚本和外联恶意域）、**第三层监控**（CSP violation report 当入侵告警）。
- 生产环境禁用 `unsafe-inline` 与 `unsafe-eval`，脚本统一用 **nonce**：服务端为每次响应生成随机 nonce，写入 CSP 头与 `<script nonce>` 一一对应。
- 资源域用域名白名单并尽量收敛（`script-src 'self'` 最优），`default-src` 兜底防漏配；`object-src 'none'`、`base-uri 'none'`、`frame-ancestors 'none'` 是三条常被漏掉的加固项。
- 用 `Content-Security-Policy-Report-Only` 先灰度观察违规上报，再切正式头，避免上线即断站。

```nginx
# nginx：nonce 模式 CSP，脚本必须带响应中生成的 nonce
server {
    listen 443 ssl;
    server_name example.com;

    location / {
        # 每次响应生成 32 字节随机 nonce
        set $csp_nonce "";
        if ($request_uri ~* ^/) {
            set_unescape_uri $csp_nonce $request_id;  # 简化示例，实际用 perl/lua 生成随机串
        }
        add_header Content-Security-Policy "default-src 'self'; script-src 'self' 'nonce-$request_id' https://cdn.example.com; style-src 'self'; img-src 'self' data:; object-src 'none'; base-uri 'none'; frame-ancestors 'none'; report-uri /csp-report" always;
        add_header Content-Security-Policy-Report-Only "script-src 'self'; report-uri /csp-report" always;
        proxy_pass http://app;
    }

    # 违规上报当入侵告警：聚合并接告警渠道
    location = /csp-report {
        proxy_pass http://log-collector;
    }
}
```

```html
<!-- 服务端渲染时把同一个 nonce 写进标签，只有匹配的脚本会执行 -->
<script nonce="{CSP_NONCE}" src="/app.js"></script>
<script nonce="{CSP_NONCE}">window.__INIT__ = {"user": {"name": "alice"}};</script>
<!-- 没带 nonce 的注入脚本被浏览器拒绝执行，即使转义被绕过 -->
```
