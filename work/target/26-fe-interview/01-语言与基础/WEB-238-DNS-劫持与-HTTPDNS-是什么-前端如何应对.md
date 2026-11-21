---
title: [WEB-238] DNS 劫持与 HTTPDNS 是什么？前端如何应对？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, DNS]
type: 面试题
---

## WEB-238：DNS 劫持与 HTTPDNS 是什么？前端如何应对？

**答**：
- DNS 劫持：运营商/中间盒篡改解析结果——跳广告、导流到镜像站、篡改静态资源注入脚本。
- 应对一（标准）：DoH/DoT 加密 DNS，防篡改防窥探，浏览器已内置（Chrome `chrome://flags` 与 Firefox 默认部分开启）。
- 应对二（国内大厂常用）：HTTPDNS——客户端直接 HTTPS 请求解析服务拿 IP，绕过运营商 DNS，App 端效果显著；Web 端受 CORS 限制常由后端下发 IP 列表。
- 前端兜底：静态资源加 SRI（hash 校验，被篡改不加载）；关键资源双域名；监控端比对 CDN 节点 IP 分布异常告警。

```html
<!-- DoH 声明 + SRI 防篡改 -->
<link rel="dns-prefetch" href="//cdn.example.com">
<script src="https://cdn.example.com/app.js"
        integrity="sha384-oqVuA..." crossorigin="anonymous"></script>
```
