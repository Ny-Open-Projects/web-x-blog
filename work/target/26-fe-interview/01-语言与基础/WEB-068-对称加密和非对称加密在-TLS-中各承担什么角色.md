---
title: [WEB-068] 对称加密和非对称加密在 TLS 中各承担什么角色？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-068：对称加密和非对称加密在 TLS 中各承担什么角色？
**答**：
- 非对称加密（RSA/ECDHE）只用于两个目的：验证证书身份、在握手阶段协商出会话密钥；它慢但解决了"密钥怎么安全地发给对方"。
- 对称加密（AES-GCM/ChaCha20）加密真正的应用数据，快几个数量级，TLS 记录层全部用它。
- 现代握手用 ECDHE 做密钥交换：双方交换椭圆曲线公钥，各自计算出相同的共享密钥，私钥永不传输，且每次会话换新密钥对实现前向保密。
- 面试一句话：非对称解决"信任与交换"，对称解决"性能与批量加密"。

```javascript
// 用 WebCrypto 复现 TLS 的分工：ECDHE 协商 + AES-GCM 加密
(async () => {
  // 模拟客户端与服务端各生成一对 ECDH 密钥
  const client = await crypto.subtle.generateKey(
    { name: 'ECDH', namedCurve: 'P-256' }, true, ['deriveKey']);
  const server = await crypto.subtle.generateKey(
    { name: 'ECDH', namedCurve: 'P-256' }, true, ['deriveKey']);

  // 双方用"对方公钥 + 自己私钥"推导出同一个会话密钥
  const clientKey = await crypto.subtle.deriveKey(
    { name: 'ECDH', public: server.publicKey }, client.privateKey,
    { name: 'AES-GCM', length: 256 }, false, ['encrypt', 'decrypt']);
  const serverKey = await crypto.subtle.deriveKey(
    { name: 'ECDH', public: client.publicKey }, server.privateKey,
    { name: 'AES-GCM', length: 256 }, false, ['encrypt', 'decrypt']);

  // 之后的通信全部使用对称加密
  const iv = crypto.getRandomValues(new Uint8Array(12));
  const ct = await crypto.subtle.encrypt(
    { name: 'AES-GCM', iv }, clientKey, new TextEncoder().encode('hello tls'));
  const pt = await crypto.subtle.decrypt(
    { name: 'AES-GCM', iv }, serverKey, ct);
  console.log(new TextDecoder().decode(pt)); // hello tls
})();
```
