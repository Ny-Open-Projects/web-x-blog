---
title: [WEB-214] 对称加密与非对称加密的区别？HTTPS 为什么两者都用？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTPS]
type: 面试题
---

## WEB-214：对称加密与非对称加密的区别？HTTPS 为什么两者都用？

**答**：
- 对称加密：加解密同一把密钥（AES），速度快（硬件加速、AES-NI），问题是如何把密钥安全地给对方——明文传等于没加密。
- 非对称加密：公钥加密只有私钥能解（RSA/ECDHE），解决密钥分发，但比对称慢 2~3 个数量级，且数据量大时开销不可接受。
- HTTPS 混合方案：握手阶段用 ECDHE 协商出会话密钥（非对称只协商密钥不加密数据），之后全量数据用对称密钥 + AEAD 加密。
- ECDHE 还带来前向保密：每次会话密钥不同且由临时私钥参与生成，服务端私钥泄漏也无法解密历史流量。

```javascript
// Node crypto 直观感受性能差距
const crypto = require('crypto');
const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', { modulusLength: 2048 });
const data = Buffer.alloc(16, 1);

console.time('RSA 加密一次');
crypto.publicEncrypt(publicKey, data);
console.timeEnd('RSA 加密一次');

console.time('AES-GCM 加密一次');
const key = crypto.randomBytes(32);
const iv = crypto.randomBytes(12);
const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);
cipher.update(data); cipher.final();
console.timeEnd('AES-GCM 加密一次');
```
