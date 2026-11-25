---
title: [WEB-237] DNS 常见记录类型：A/CNAME/AAAA/TXT/NS 用法
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, DNS]
type: 面试题
---

## WEB-237：DNS 常见记录类型：A/CNAME/AAAA/TXT/NS 用法

**答**：
- A：域名 → IPv4；AAAA：域名 → IPv6。
- CNAME：域名 → 另一个域名，CDN 接入的标配（`cdn.example.com → cdn.dnsv1.com`），链路末端必须是 A/AAAA（CNAME 不能指向 CNAME 无限套）。
- TXT：附加文本，验证域名所有权（SSL 签发、SPF 反垃圾邮件）、存配置。
- NS：指定该域名的权威解析服务器；SOA 存域的元数据（序列号、刷新时间）。
- 前端工程实践：域名统一 CNAME 到 CDN；灰度解析用 DNS 权重；HTTPS 记录（SVCB）可让浏览器首次连接就拿到 HTTP/3 支持信息，省一次 Alt-Svc 探测。

```bash
dig +short cdn.example.com        # → CNAME 链 → 最终 IP
dig +short example.com TXT        # "v=spf1 include:..." 验证记录
dig +short example.com NS         # a.ns.example.com.
```
