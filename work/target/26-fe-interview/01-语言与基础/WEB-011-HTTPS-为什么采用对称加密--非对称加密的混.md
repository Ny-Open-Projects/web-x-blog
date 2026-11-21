---
title: [WEB-011] HTTPS 为什么采用对称加密 + 非对称加密的混合方案？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-011：HTTPS 为什么采用对称加密 + 非对称加密的混合方案？
**答**：
- 纯对称加密（AES）：快，但双方要预先共享密钥，明文传密钥等于没加密。
- 纯非对称加密（RSA）：公钥可公开，但性能比对称加密慢几个数量级，不适合传输大流量。
- 混合方案：握手阶段用非对称加密安全地交换对称密钥（或通过 ECDHE 协商），之后的数据传输全用对称加密。
- 现代主流是 ECDHE 交换密钥 + AES-GCM 加密数据，兼顾安全与性能。

```javascript
// Node.js 演示混合加密的思想：RSA 解出对称密钥，再用 AES 解数据
const crypto = require('crypto');

// 服务端持有私钥，客户端用公钥加密一次性对称密钥
const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', {
  modulusLength: 2048,
});

// 客户端侧：生成会话密钥并用公钥封装
const sessionKey = crypto.randomBytes(32); // AES-256 密钥
const iv = crypto.randomBytes(16);
const cipher = crypto.createCipheriv('aes-256-gcm', sessionKey, iv);
const encrypted = Buffer.concat([cipher.update('hello https', 'utf8'), cipher.final()]);
const tag = cipher.getAuthTag();
const wrappedKey = crypto.publicEncrypt(publicKey, sessionKey); // RSA 封装密钥

// 服务端侧：私钥解出对称密钥，再解数据
const unwrapped = crypto.privateDecrypt(privateKey, wrappedKey);
const decipher = crypto.createDecipheriv('aes-256-gcm', unwrapped, iv);
decipher.setAuthTag(tag);
const plain = Buffer.concat([decipher.update(encrypted), decipher.final()]);
console.log(plain.toString('utf8')); // hello https
```
