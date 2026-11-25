---
title: [PER-1021] TLS 层性能：会话恢复、TLS 1.3 与 OCSP 的取舍
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1021：TLS 层性能：会话恢复、TLS 1.3 与 OCSP 的取舍

**答**：
- TLS 1.3 握手 1-RTT（较 1.2 少一个 RTT），支持 0-RTT 恢复；现代部署下 TLS 成本已大幅降低。
- 会话票据（session ticket）让重连免完整握手；密钥轮换与票据有效期要短（票据窃取可解密会话）。
- OCSP 装订（stapling）：证书状态由服务器随握手附带，避免浏览器串行查询 OCSP 服务器（可省数百 ms）。
- 证书链优化：中间证书随握手下发完整链、链越短握手包越少；ECDSA 证书比 RSA 小且快。

```javascript
// 证书链体检（Node 端诊断）
const tls = require('tls');
const sock = tls.connect({ host: 'example.com', port: 443, servername: 'example.com' }, () => {
  const cert = sock.getPeerCertificate(true);
  let chain = 0;
  for (let c = cert; c; c = c.issuerCertificate) { chain++; if (c === c.issuerCertificate) break; }
  console.log({ chainDepth: chain, sigAlgo: cert.sigalg,    // ECDSA-with-SHA256 更优
    validTo: cert.valid_to });
  sock.end();
});
// OCSP 验证：openssl s_client -status 检查装订是否开启
```
