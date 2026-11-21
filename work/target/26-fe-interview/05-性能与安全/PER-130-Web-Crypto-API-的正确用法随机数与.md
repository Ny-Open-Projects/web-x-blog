---
title: [PER-130] Web Crypto API 的正确用法？随机数与密钥管理的常见错误？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-130：Web Crypto API 的正确用法？随机数与密钥管理的常见错误？

**答**：
- 安全随机数一律 `crypto.getRandomValues`，`Math.random` 只能用于非安全场景（动画扰动、抽样）。
- 密钥不硬编码、不进 localStorage：非对称密钥用 `subtle.generateKey` 生成，私钥不可导出（`extractable: false`）；对称密钥由服务端按会话下发或现场派生。
- 加密选 AES-GCM，IV 每次随机生成且与密文一起存储，绝不复用；密码派生用 PBKDF2（迭代 ≥ 31 万次），禁止 MD5/SHA1 与自研算法。
- 常见错误：把"前端加密"当机密性保证——前端代码是公开的，前端加密只防中间人之外的低级泄漏，机密性必须靠 TLS + 服务端。

```javascript
// 随机数：安全场景一律 crypto.getRandomValues，禁止 Math.random
function randomBytes(len) {
  const b = new Uint8Array(len);
  crypto.getRandomValues(b);
  return b;
}
export const csrfToken = () =>
  Array.from(randomBytes(16), (x) => x.toString(16).padStart(2, '0')).join('');

// 密钥管理：subtle 生成，私钥不可导出，永不落地
const { publicKey, privateKey } = await crypto.subtle.generateKey(
  { name: 'RSASSA-PKCS1-v1_5', modulusLength: 2048, hash: 'SHA-256' },
  false, // extractable=false：私钥导不出内存
  ['sign', 'verify']
);

// 加密：AES-GCM，IV 每次随机且随密文一起存
export async function encryptJson(key, obj) {
  const iv = randomBytes(12); // GCM 推荐 12 字节 IV，绝不复用
  const ct = await crypto.subtle.encrypt(
    { name: 'AES-GCM', iv }, key, new TextEncoder().encode(JSON.stringify(obj)));
  return { iv: Array.from(iv), ct: Array.from(new Uint8Array(ct)) };
}

// 密码派生：PBKDF2 高迭代，禁止 MD5/SHA1 与自研算法
export async function deriveKey(password, salt) {
  const base = await crypto.subtle.importKey('raw', new TextEncoder().encode(password), 'PBKDF2', false, ['deriveKey']);
  return crypto.subtle.deriveKey(
    { name: 'PBKDF2', salt, iterations: 310000, hash: 'SHA-256' }, base,
    { name: 'AES-GCM', length: 256 }, false, ['encrypt', 'decrypt']);
}
```
