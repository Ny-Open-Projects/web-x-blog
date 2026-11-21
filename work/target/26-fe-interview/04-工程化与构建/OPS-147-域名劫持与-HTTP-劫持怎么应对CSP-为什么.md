---
title: [OPS-147] 域名劫持与 HTTP 劫持怎么应对？CSP 为什么要 report-only 渐进上线？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-147：域名劫持与 HTTP 劫持怎么应对？CSP 为什么要 report-only 渐进上线？
**答**：
- HTTP 劫持发生在明文层（运营商插广告/script）：全站 HTTPS + HSTS 从根上消除；301 到 HTTPS 的 HTTP 端口也要保留监控。
- 域名劫持（解析层）：注册商转移锁、注册局锁，DNS 侧双解析商比对监控，变更走双人流程。
- CSP 渐进：先 Content-Security-Policy-Report-Only 观察 2-4 周误报（第三方脚本、内联样式），报告量收敛后再切 enforce，避免一刀切把页面打断。
- SRI 兜底资源篡改（OPS-148）；前端监控检测注入特征（白名单外 script/iframe）上报。
- 页面加载后做关键资源指纹校验（如版本注入点校验），发现被改写即告警——劫持检测平民化。

```nginx
# 劫持应对：HTTPS + HSTS + CSP 渐进
server {
    listen 443 ssl http2;
    # 80 端口 server 全量 301 到 https，并保留劫持采样监控

    add_header Strict-Transport-Security "max-age=63072000; includeSubDomains" always;
    ssl_stapling on;              # OCSP 装订，防证书状态查询被劫持
    ssl_stapling_verify on;

    # 阶段一（2-4 周）：report-only 只观察不拦截，收集误报
    add_header Content-Security-Policy-Report-Only \
      "default-src 'self'; script-src 'self' https://cdn.example.com; report-uri /csp-report" always;

    # 阶段二：报告收敛后切换 enforce（保留 report-uri 持续监控）
    # add_header Content-Security-Policy \
    #   "default-src 'self'; script-src 'self' https://cdn.example.com; report-uri /csp-report" always;

    location = /csp-report {
        proxy_pass http://collector.internal;
        access_log off;
    }
}
# 域名解析层：注册商转移锁 + 双解析商比对监控，DNS 变更双人复核
```
