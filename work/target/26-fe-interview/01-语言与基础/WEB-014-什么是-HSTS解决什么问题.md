---
title: [WEB-014] 什么是 HSTS？解决什么问题？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-014：什么是 HSTS？解决什么问题？
**答**：
- HTTPS 站点首次访问前，用户直接输入域名走的还是 HTTP，存在被劫持跳转的风险窗口。
- HSTS 通过响应头 `Strict-Transport-Security` 告诉浏览器：在 max-age 内，所有对该域名的访问强制走 HTTPS，且禁止用户点击"继续访问不安全链接"。
- 仅对 HTTPS 响应生效，HTTP 响应里的 HSTS 头会被忽略；可配合 `includeSubDomains` 覆盖子域。
- 还可申请加入浏览器 HSTS Preload 列表，连第一次访问都强制 HTTPS。

```nginx
# nginx 开启 HSTS 的标准配置
server {
    listen 443 ssl;
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;

    # 把所有 HTTP 请求 301 到 HTTPS（HSTS 生效前兜底）
}
server {
    listen 80;
    return 301 https://$host$request_uri;
}
```
