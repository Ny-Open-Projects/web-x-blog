---
title: [WEB-135] HTTPDNS 是什么？它解决运营商 DNS 的哪些问题？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-135：HTTPDNS 是什么？它解决运营商 DNS 的哪些问题？
**答**：
- 传统解析走 UDP 53 的运营商递归：存在劫持（插广告/错解析）、LocalDNS 缓存过期导致调度不准、跨网访问慢三大问题。
- HTTPDNS 用 HTTP(S) 直接请求云解析服务拿到精确 IP，绕过运营商链路，防劫持还能拿到就近调度结果。
- 移动端重点场景：弱网下域名解析失败率暴涨，HTTPDNS 作为兜底通道大幅降低失败率。
- 限制：HTTPS 请求"连 IP"需要 SNI 与 Host 仍指向域名，浏览器无法改 SNI，因此 H5 场景主要服务于端上网络栈（JSBridge 下发解析结果）。

```javascript
// Node 演示 HTTPDNS 的两步走：先拿 IP，再连 IP 访问域名
const https = require('https');
// 第一步：向 HTTPDNS 服务查询（示例为通用参数风格，具体以服务商文档为准）
https.get('https://203.107.1.1/resolve?host=api.example.com', (r) => {
  let body = '';
  r.on('data', (c) => (body += c));
  r.on('end', () => {
    const ip = JSON.parse(body).data.ips[0];
    // 第二步：连接用 IP，SNI 与 Host 仍是域名，证书校验不受影响
    https.get({ host: ip, servername: 'api.example.com', path: '/' }, (resp) => {
      console.log('HTTPDNS 直连结果:', resp.statusCode);
    });
  });
});
// 浏览器 fetch 无法自定义 SNI，所以 H5 场景下 HTTPDNS 多通过 JSBridge 交给端上网络栈实现
```
