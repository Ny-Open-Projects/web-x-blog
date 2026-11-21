---
title: [WEB-105] HSTS 的作用是什么？preload 列表是怎么回事？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-105：HSTS 的作用是什么？preload 列表是怎么回事？
**答**：
- `Strict-Transport-Security` 让浏览器记住"该域在 max-age 内只准 HTTPS"，用户手输 http:// 也被浏览器内部 307 跳到 https，不给中间人劫持明文跳转的机会。
- `includeSubDomains` 覆盖所有子域；首次访问前的空窗期由 preload 列表弥补——域名提交进 Chromium 内置硬编码清单，首次连接即强制 HTTPS。
- 代价：加入 preload 后退出很难（移除要排队数月），子域没有 HTTPS 证书的站会被波及，提交前要全子域盘点。
- 与之配套的还有 Upgrade-Insecure-Requests（CSP 指令），处理页面内 http:// 子资源的改写。

```http
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload

# 生效时间线：
# 第一次响应携带该头后，浏览器把域写入本地 HSTS 状态
# 之后一年内：任何 http:// 请求在浏览器内部直接改写为 https://，不发起明文请求
# preload：提交 https://hstspreload.org 审核通过后，新装机浏览器首次访问即强制 HTTPS
# 灰度建议：先用小 max-age 观察子域证书覆盖情况，再逐步调大并提交 preload
```
