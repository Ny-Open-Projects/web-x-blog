---
title: [NODE-020] Node 如何起一个 HTTPS 服务？证书怎么来？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-020：Node 如何起一个 HTTPS 服务？证书怎么来？
**答**：
- HTTPS = TLS 层 + http，Node 用 `https.createServer({ key, cert }, handler)`；TLS 握手由 Node 内置 OpenSSL 完成。
- 证书来源：生产从 CA 签发（Let's Encrypt 的 ACME 可用 `greenlock`/certbot 自动续期）；本地开发用 `mkcert` 生成本地可信证书（比自签证书体验好，浏览器不报警）。
- 注意：`server.listen` 之后 `req.socket.getPeerCertificate()` 可取客户端证书（mTLS 双向认证）；TLS 版本至少 1.2，禁用旧 cipher。

```bash
# 本地开发：mkcert 生成受本机信任的证书
brew install mkcert
mkcert -install
mkcert localhost 127.0.0.1 ::1   # 生成 ./localhost+2.pem 与 ./localhost+2-key.pem
```

```javascript
const https = require('node:https');
const fs = require('node:fs');
const path = require('node:path');

const options = {
  key: fs.readFileSync(path.join(__dirname, 'localhost+2-key.pem')),
  cert: fs.readFileSync(path.join(__dirname, 'localhost+2.pem')),
  minVersion: 'TLSv1.2',               // 强制 TLS 1.2+
  // 双向认证 mTLS：要求客户端也带证书
  // requestCert: true,
  // rejectUnauthorized: true,
  // ca: fs.readFileSync('client-ca.pem'),
};

https.createServer(options, (req, res) => {
  const cert = req.socket.getPeerCertificate?.();
  res.writeHead(200, { 'content-type': 'application/json' });
  res.end(JSON.stringify({ secure: true, client: cert?.subject?.CN ?? 'anonymous' }));
}).listen(3443, () => console.log('https://localhost:3443'));
```
