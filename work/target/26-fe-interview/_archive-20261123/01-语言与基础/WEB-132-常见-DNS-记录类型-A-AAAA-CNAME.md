---
title: [WEB-132] 常见 DNS 记录类型 A、AAAA、CNAME、NS、TXT 各自的用途是什么？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-132：常见 DNS 记录类型 A、AAAA、CNAME、NS、TXT 各自的用途是什么？
**答**：
- A / AAAA：域名到 IPv4 / IPv6 地址，业务流量最终都落在这两类记录上。
- CNAME：别名指向另一个域名，CDN 接入就是给域名加一条 CNAME 指到调度域名。
- NS：声明"这个区域由哪些权威服务器解析"，子域委托和云厂商切换全靠它。
- TXT：任意文本，常用于 SPF/DKIM 邮件反垃圾、各大平台的域名归属验证串就放在 TXT。
- 工程要点：CNAME 链会多一次查询，关键域名建议直接 A/AAAA；MX、SRV、CAA 等按需了解。

```bash
dig +short www.example.com A        # A 记录，直接给出 IPv4
dig +short www.example.com AAAA     # AAAA 记录，IPv6
dig +short cdn.example.com CNAME    # CNAME，别名链，CDN 场景常见多层
dig +short example.com NS           # NS，区域的权威服务器
dig +short example.com TXT          # TXT，SPF 与站点验证串都在这里
dig +short example.com MX           # 顺带，邮件交换记录
```
