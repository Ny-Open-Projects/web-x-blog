---
title: [WEB-016] HTTPS 已经加密了，抓包工具（如 mitmproxy/Charles）为什么还能看到明文？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-016：HTTPS 已经加密了，抓包工具（如 mitmproxy/Charles）为什么还能看到明文？
**答**：
- 抓包工具本质是自己充当中间人：对客户端伪装成服务器，对服务器伪装成客户端，各建一条 TLS 连接。
- 客户端信任它的前提是：设备里安装了抓包工具的根证书，于是假证书也能通过校验。
- 所以"HTTPS 防中间人"的前提是用户不主动安装不可信根证书；企业代理、家长控制类软件都是这个原理。
- 防御：APP 内置证书锁定（SSL Pinning），只信任指定证书/公钥，即使系统被装根证书也连不上。

```javascript
// Node.js 演示 SSL Pinning：校验服务器证书指纹，拒绝被代理的连接
const tls = require('tls');

const EXPECTED_FINGERPRINT = 'AA:BB:CC:DD:...'; // 上线前固化服务端证书的 SHA-256 指纹

const socket = tls.connect(
  {
    host: 'api.example.com',
    port: 443,
    servername: 'api.example.com',
  },
  () => {
    const cert = socket.getPeerCertificate();
    // 代理工具的假证书指纹与预期不符，直接断开
    if (cert.fingerprint256 !== EXPECTED_FINGERPRINT) {
      socket.destroy();
      console.error('certificate pinning failed, possible MITM');
    } else {
      console.log('server identity verified');
      socket.end();
    }
  }
);
```

## 三、状态码
