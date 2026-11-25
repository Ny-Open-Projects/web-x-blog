---
title: [WEB-413] TLS 1.3 的握手为什么只需 1-RTT
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTPS]
type: 面试题
---

## WEB-413：TLS 1.3 的握手为什么只需 1-RTT

**答**：
- TLS 1.2 需要 2-RTT：先协商参数、再交换密钥；1.3 把「支持的算法套件」直接写进 ClientHello，一次往返就完成密钥交换
- 密钥协商默认只用 ECDHE，砍掉了 RSA 密钥交换（不具备前向安全），CipherSuite 从几十个收敛到少数几个
- 复用场景配合 PSK 可做到 0-RTT，但 0-RTT 数据有重放风险
- 前端感知：新建连接的首包时间明显缩短，对短连接、多域名站点收益大

```javascript
// 用 Node 观察 TLS 1.3 握手耗时
const tls = require('tls');
const start = Date.now();
const sock = tls.connect(443, 'example.com', () => {
  console.log('协议版本:', sock.getProtocol()); // TLSv1.3
  console.log('握手耗时(ms):', Date.now() - start);
  sock.end();
});
```
