---
title: [PER-652] 手写一个 PBKDF2 密钥派生工具：从用户口令派生 AES 密钥，参数选择与暴力破解成本评估
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-652：手写一个 PBKDF2 密钥派生工具：从用户口令派生 AES 密钥，参数选择与暴力破解成本评估

**答**：
- 用户口令熵低不能直接当密钥，必须 KDF 派生：PBKDF2-HMAC-SHA256，迭代次数按设备能承受 + 攻击成本足够高选（OWASP 建议 600k 次起，前端可按设备分档）。
- 要点：salt 随机生成并存储（同口令不同用户派生不同密钥，防彩虹表）；派生结果作为 AES-GCM 密钥导入；迭代次数是性能与安全权衡——太慢影响首开体验，可用 Web Worker 避免卡 UI。
- 边界：WebCrypto `deriveBits` 完成；迭代参数要随密文存储（算法升级时老数据仍可解）；永不降级迭代次数重派生已有数据。
- 评分点：salt 随机存储与迭代参数随密文保存。

```javascript

async function deriveFromPassword(password, saltBytes, iterations = 600000) {
  const baseKey = await crypto.subtle.importKey('raw',
    new TextEncoder().encode(password), 'PBKDF2', false, ['deriveBits', 'deriveKey']);
  const key = await crypto.subtle.deriveKey(
    { name: 'PBKDF2', salt: saltBytes, iterations, hash: 'SHA-256' },
    baseKey, { name: 'AES-GCM', length: 256 }, false, ['encrypt', 'decrypt']);
  return key;
}
async function encryptWithPassword(password, plaintext) {
  const salt = crypto.getRandomValues(new Uint8Array(16));     // 随机 salt 随密文存
  const iters = deviceTier() === 'low' ? 300000 : 600000;      // 设备分档
  const key = await deriveFromPassword(password, salt, iters);
  const iv = crypto.getRandomValues(new Uint8Array(12));
  const ct = await crypto.subtle.encrypt({ name: 'AES-GCM', iv }, key,
    new TextEncoder().encode(plaintext));
  // salt + iterations + iv + 密文 全部持久化，缺一不可解
  return { blob: [salt, iv, new Uint8Array(ct)].map(b => btoa(String.fromCharCode(...b))),
    iterations: iters };
}
function deviceTier() { return (navigator.hardwareConcurrency ?? 4) >= 8 ? 'high' : 'low'; }
```
