---
title: [WEB-239] DoH/DoT 是什么？与传统 DNS 差在哪？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, DNS]
type: 面试题
---

## WEB-239：DoH/DoT 是什么？与传统 DNS 差在哪？

**答**：
- 传统 DNS 用 UDP 53 明文传输：内容可被嗅探（你访问了什么域名）、可被劫持篡改、可被中间设备阻塞。
- DoT：DNS over TLS，走 TCP 853 端口，加密但端口独立易被识别封锁。
- DoH：DNS over HTTPS，复用 443 端口与正常 HTTPS 流量混在一起，难区分难封锁，浏览器主推。
- 收益：防劫持防窥探 + 浏览器可在解析阶段就拿到 HTTPS/HTTP3 支持信息（HTTPS/SVCB 记录），连接更快。
- 成本：绕过运营商 DNS 后，部分「就近解析」失准（CDN 调度看到的是 DoH 服务器 IP）；EDNS Client Subnet 是补偿手段。

```javascript
// 浏览器侧无法直接指定 DoH，由系统/浏览器设置；
// Node 可以验证 DoH 响应格式（RFC 8484）
const res = await fetch('https://dns.google/resolve?name=example.com&type=A');
const { Answer } = await res.json();
console.log(Answer.map(a => a.data)); // IP 列表
```
