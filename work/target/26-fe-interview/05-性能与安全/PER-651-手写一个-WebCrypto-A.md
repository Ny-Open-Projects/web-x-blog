---
title: [PER-651] 手写一个 WebCrypto AES-GCM 加解密工具：密钥导入、加密、解密与完整性验证
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-651：手写一个 WebCrypto AES-GCM 加解密工具：密钥导入、加密、解密与完整性验证

**答**：
- AES-GCM 是前端对称加密首选：自带认证（IV 被篡改解密直接抛错），不需要单独 HMAC；IV 必须**每次加密随机生成并随密文一起存储**（IV 复用是 GCM 最致命的错误）。
- 要点：密钥用 `crypto.subtle.importKey('raw')` 导入；输出格式 IV(12 字节) + 密文拼一起再 base64；解密拆出 IV 再 decrypt，GCM 自动作完整性校验。
- 边界：大文件分块加密（每块独立 IV）；密钥来源不能是前端硬编码（见加密边界卡）；`crypto.subtle` 只在 secure context 可用（HTTPS/localhost）。
- 评分点：IV 随机生成与随密文存储。

```javascript

async function aesGcm() {
  const enc = new TextEncoder(), dec = new TextDecoder();
  async function key(raw) {
    return crypto.subtle.importKey('raw', enc.encode(raw.padEnd(32, '0').slice(0, 32)),
      'AES-GCM', false, ['encrypt', 'decrypt']);
  }
  async function encrypt(k, plaintext) {
    const iv = crypto.getRandomValues(new Uint8Array(12));       // 每次随机 IV
    const ct = await crypto.subtle.encrypt({ name: 'AES-GCM', iv }, k, enc.encode(plaintext));
    const out = new Uint8Array(iv.length + ct.byteLength);
    out.set(iv); out.set(new Uint8Array(ct), iv.length);         // IV+密文打包
    return btoa(String.fromCharCode(...out));
  }
  async function decrypt(k, packed) {
    const bytes = Uint8Array.from(atob(packed), c => c.charCodeAt(0));
    const iv = bytes.slice(0, 12), ct = bytes.slice(12);
    return dec.decode(await crypto.subtle.decrypt({ name: 'AES-GCM', iv }, k, ct));
    // 密文或 IV 被篡改 -> 直接抛 OperationError（GCM 认证失败）
  }
  const k = await key('my-secret-key-32-bytes-aaaaaa');
  const c = await encrypt(k, '敏感数据');
  console.log(c, await decrypt(k, c));
}
```
