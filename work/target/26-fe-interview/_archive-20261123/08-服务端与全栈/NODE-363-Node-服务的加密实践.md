---
title: [NODE-363] Node 服务的加密实践：对称/非对称/哈希的正确用法
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-363：Node 服务的加密实践
**答**:
- 哈希（不可逆）：密码用 argon2/bcrypt（自带盐、慢哈希抗暴力，禁 md5/sha1）；数据完整性校验用 sha256；HMAC 用于签名校验（webhook 验签）。
- 对称加密（AES-256-GCM）：可逆数据（手机号存储），必须随机 IV 每次生成（重复 IV 是 GCM 致命错误）+ authTag 完整性；密钥来自 KMS/配置（NODE-362）。
- 非对称（RSA/ECDSA）：签名验证（JWT/请求签名）与密钥交换；加密小数据用 RSA-OAEP。
- 随机数：crypto.randomBytes/randomInt，禁 Math.random（可预测——token/验证码场景致命）。
- 时序安全比较：token/签名比较用 crypto.timingSafeEqual（防时序攻击），不用 ===。
```javascript
const crypto = require('crypto');
function encrypt(text, key) {
  const iv = crypto.randomBytes(12);                             // 每次随机 IV
  const c = crypto.createCipheriv('aes-256-gcm', key, iv);
  const enc = Buffer.concat([c.update(text, 'utf8'), c.final()]);
  return Buffer.concat([iv, c.getAuthTag(), enc]).toString('base64');
}
function verifySign(raw, sig, pub) {
  const ok = crypto.verify('sha256', Buffer.from(raw), pub, Buffer.from(sig, 'base64'));
  return ok;
}
const tokenEq = crypto.timingSafeEqual(Buffer.from(a), Buffer.from(b)); // 时序安全
```
