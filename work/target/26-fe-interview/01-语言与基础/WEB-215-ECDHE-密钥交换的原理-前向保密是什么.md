---
title: [WEB-215] ECDHE 密钥交换的原理？前向保密是什么？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTPS]
type: 面试题
---

## WEB-215：ECDHE 密钥交换的原理？前向保密是什么？

**答**：
- ECDHE = 椭圆曲线 + 短暂密钥（Ephemeral）+ Diffie-Hellman。双方各生成临时椭圆曲线密钥对，交换公钥后用「对方公钥 × 自己私钥」各自算出同一个共享秘密，监听者拿到两个公钥算不出这个值（椭圆曲线离散对数难题）。
- 「临时」是关键：每次握手生成新的临时密钥对，会话密钥只用一次，这就是前向保密（PFS）。
- 前向保密的价值：即使服务端长期私钥将来泄漏，历史抓包也无法解密（RSA 密钥交换做不到——私钥泄漏后历史流量全可解）。
- TLS 1.3 只允许 (EC)DHE 与 PSK 两类，彻底删除 RSA 密钥交换正是为了强制 PFS。

```javascript
// Node 演示 ECDH 双方算出相同共享密钥
const crypto = require('crypto');
const a = crypto.createECDH('secp256k1'); a.generateKeys();
const b = crypto.createECDH('secp256k1'); b.generateKeys();
const secretA = a.computeSecret(b.getPublicKey()); // A 用 B 的公钥算
const secretB = b.computeSecret(a.getPublicKey()); // B 用 A 的公钥算
console.log(secretA.equals(secretB)); // true —— 双方得到同一密钥
// 监听者只有 a公钥/b公钥，无法推导 secret
```
