---
title: [ALG-174] 本地存储的接口 mock 数据、调试标记不想被用户一眼看懂，如何用 Base64 + XOR 做轻量混淆？为什么它不是加密？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-174：本地存储的接口 mock 数据、调试标记不想被用户一眼看懂，如何用 Base64 + XOR 做轻量混淆？为什么它不是加密？
**答**：XOR 满足自反性 `a ^ k ^ k = a`：编码时逐字节与密钥循环异或再 Base64（二进制转文本），解码反向即可。说它不是加密：密钥在前端代码里任何人都拿得到，XOR 无密钥分发机制、可被已知明文攻击瞬间破解；它只防"随手可见"，防不了有意攻击。敏感数据必须走真正的加密（WebCrypto AES-GCM）且密钥不下发前端。

```javascript
function xorObfuscate(str, key) {
  const bytes = new TextEncoder().encode(str);
  const k = new TextEncoder().encode(key);
  const out = bytes.map((b, i) => b ^ k[i % k.length]); // 循环密钥异或
  return btoa(String.fromCharCode(...out));             // 二进制转可见文本
}
function xorDeobfuscate(encoded, key) {
  const bytes = Uint8Array.from(atob(encoded), c => c.charCodeAt(0));
  const k = new TextEncoder().encode(key);
  // XOR 自反：a ^ k ^ k = a，同一函数即可还原
  return new TextDecoder().decode(bytes.map((b, i) => b ^ k[i % k.length]));
}
// xorObfuscate('debug-on', 'k3y') 存 localStorage；读取时 xorDeobfuscate 还原
// 注意：这仅是混淆不是加密，密钥在前端对攻击者完全可见
```
