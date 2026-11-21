---
title: [WEB-136] DNS over HTTPS（DoH）和 DoT 是什么？对前端有什么影响？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-136：DNS over HTTPS（DoH）和 DoT 是什么？对前端有什么影响？
**答**：
- 传统 DNS 明文传输，链路上的设备能看到并篡改你访问了哪个域名；DoH（RFC 8484）把 DNS 查询装进 HTTPS，DoT 用 853 端口的 TLS 承载。
- DoH 复用 443 穿透性强；DoT 是独立端口，更容易被防火墙识别与管制。
- 浏览器已内置 DoH（Chrome/Firefox 的安全 DNS 设置），查询行为变了但页面代码无感知。
- 对前端的影响：可观测性下降（本地抓包看不到明文 DNS）、hosts/预解析逻辑不变、企业网排障要考虑 DoH 绕过内网解析。
- 延伸概念：Oblivious DoH 在 DoH 之上再加代理层隔离客户端 IP，进一步保护隐私。

```javascript
// 用公共 DoH 的 JSON 接口（application/dns-json 扩展）做一次解析
const url = 'https://dns.alidns.com/resolve?name=www.example.com&type=A';
const { Answer } = await (await fetch(url, { headers: { accept: 'application/dns-json' } })).json();
console.log(Answer); // [{ name, type: 1, TTL, data: '93.184.x.x' }]
// 浏览器内置 DoH 开启后，系统层发出的查询同样会被加密，页面层完全无感
```

## 二十三、代理与网关
