---
title: [H5-091] Web Crypto API 做加解密的概览：generateKey、importKey、encrypt 流程。
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-091：Web Crypto API 做加解密的概览：generateKey、importKey、encrypt 流程。
**答**：
- 三大步：**密钥**（`generateKey` 生成或 `importKey` 导入原始字节/PBKDF2 派生）→ **操作**（encrypt/decrypt/sign/verify/deriveBits）→ **存储**（`exportKey` 导出或 indexDB 存 CryptoKey 对象本身）。
- 对称加密推荐 `AES-GCM`：密文 + 96 位随机 IV + 认证标签一体的 AEAD 算法；IV 必须每次随机且不重复。
- 非对称场景 `RSA-OAEP`（加密小数据/密钥交换）与 `ECDSA/Ed25519`（签名验签）；混合加密 = RSA 包 AES 密钥 + AES 加数据。
- 口令场景：`PBKDF2`（或 `HKDF`）从口令派生密钥，`salt` 随机、`iterations` 10 万起步。
- 边界：subtle 只在安全上下文可用；私钥导出受 `extractable` 限制；它不做证书体系，HTTPS 传输安全仍由 TLS 保证。

```javascript
// 对称加解密最小闭环：AES-GCM
async function demo() {
  // 1) 生成密钥（encrypt/decrypt 两个用途，不可导出）
  const key = await crypto.subtle.generateKey(
    { name: 'AES-GCM', length: 256 }, false, ['encrypt', 'decrypt']
  );

  // 2) 加密：随机 12 字节 IV（GCM 推荐 96 位）
  const iv = crypto.getRandomValues(new Uint8Array(12));
  const plain = new TextEncoder().encode('机密数据：工资单');
  const cipher = await crypto.subtle.encrypt({ name: 'AES-GCM', iv }, key, plain);

  // 3) 解密：同一 key 与同一 IV
  const out = await crypto.subtle.decrypt({ name: 'AES-GCM', iv }, key, cipher);
  console.log(new TextDecoder().decode(out));
  return { key, iv, cipher };
}

// 口令派生密钥：PBKDF2 -> AES-GCM
async function keyFromPassword(password, salt) {
  const base = await crypto.subtle.importKey(
    'raw', new TextEncoder().encode(password), 'PBKDF2', false, ['deriveKey']
  );
  return crypto.subtle.deriveKey(
    { name: 'PBKDF2', salt, iterations: 150_000, hash: 'SHA-256' },
    base,
    { name: 'AES-GCM', length: 256 },
    false, ['encrypt', 'decrypt']
  );
}

// 非对称：RSA-OAEP 加密会话密钥（混合加密骨架）
async function hybrid() {
  const { publicKey, privateKey } = await crypto.subtle.generateKey(
    { name: 'RSA-OAEP', modulusLength: 2048, publicExponent: new Uint8Array([1, 0, 1]),
      hash: 'SHA-256' }, true, ['encrypt', 'decrypt']
  );
  const sessionKey = await crypto.subtle.generateKey({ name: 'AES-GCM', length: 256 }, true, ['encrypt', 'decrypt']);
  const rawKey = await crypto.subtle.exportKey('raw', sessionKey);
  const wrapped = await crypto.subtle.encrypt({ name: 'RSA-OAEP' }, publicKey, rawKey); // RSA 包 AES 密钥
  return { wrapped, privateKey };
}
```

## 十七、设备与传感
