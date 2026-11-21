---
title: [PER-653] 手写一个 RSA-OAEP 混合加密客户端：RSA 包裹 AES 会话密钥，实现大数据用对称且密钥用非对称的混合加密
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-653：手写一个 RSA-OAEP 混合加密客户端：RSA 包裹 AES 会话密钥，实现大数据用对称且密钥用非对称的混合加密

**答**：
- 混合加密标准姿势：数据用 AES-GCM 加密（快、支持大数据），AES 密钥本身用接收方 RSA-OAEP 公钥加密后一起传输——解决对称密钥怎么安全送达的问题。
- 要点：RSA 只加密密钥（RSA 不能加密大数据，OAEP padding 上限约 190 字节@2048 位）；每次会话生成新的随机 AES 密钥（前向性：私钥泄漏不影响历史会话，前提是会话密钥不复用）；公钥从服务端下发并验签防替换。
- 边界：公钥指纹要展示/校验（防中间人替换公钥）；私钥永不落前端；输出格式：`{rsaWrappedKey, iv, ciphertext}`。
- 评分点：会话密钥一次性生成与公钥校验。

```javascript

async function hybridEncrypt(publicKeyJwk, plaintext) {
  // 1) 随机会话密钥（一次性）
  const aesKey = await crypto.subtle.generateKey({ name: 'AES-GCM', length: 256 },
    true, ['encrypt', 'decrypt']);
  // 2) 数据用 AES-GCM
  const iv = crypto.getRandomValues(new Uint8Array(12));
  const ct = await crypto.subtle.encrypt({ name: 'AES-GCM', iv }, aesKey,
    new TextEncoder().encode(plaintext));
  // 3) 会话密钥导出并用 RSA-OAEP 公钥包裹
  const rawKey = await crypto.subtle.exportKey('raw', aesKey);
  const pub = await crypto.subtle.importKey('jwk', publicKeyJwk,
    { name: 'RSA-OAEP', hash: 'SHA-256' }, false, ['encrypt']);
  const wrapped = await crypto.subtle.encrypt({ name: 'RSA-OAEP' }, pub, rawKey);
  return {
    k: btoa(String.fromCharCode(...new Uint8Array(wrapped))),
    iv: btoa(String.fromCharCode(...iv)),
    c: btoa(String.fromCharCode(...new Uint8Array(ct))),
  };
}
// 公钥下发带签名：前端用内置 CA 公钥验签后才使用，防中间人替换公钥
```
