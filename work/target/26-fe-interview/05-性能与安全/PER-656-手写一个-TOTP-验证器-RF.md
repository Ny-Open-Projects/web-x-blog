---
title: [PER-656] 手写一个 TOTP 验证器（RFC 6238）：基于 WebCrypto 生成与校验 6 位动态码
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-656：手写一个 TOTP 验证器（RFC 6238）：基于 WebCrypto 生成与校验 6 位动态码

**答**：
- TOTP = HOTP(K, T) 其中 T = floor((now - T0) / 步长30s)；HMAC-SHA256（或 SHA1，兼容 Google Authenticator 用 SHA1）对 8 字节计数器取模 10^6。
- 要点：计数器转 8 字节大端；HMAC 结果动态截断（dynamic truncation：取末字节低 4 位做偏移，取 4 字节去符号位 mod 1000000）；校验允许 ±1 时间窗（时钟偏差）。
- 边界：secret 是 base32 编码（otpauth:// URI 里），解码要自己实现 base32；窗口校验要防重放（同一 T 值用过即拒绝，服务端职责）。
- 评分点：动态截断与 ±1 窗口。

```javascript

function base32Decode(s) {
  const A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567';
  let bits = 0, val = 0; const out = [];
  for (const c of s.replace(/=+$/, '').toUpperCase()) {
    val = (val << 5) | A.indexOf(c); bits += 5;
    if (bits >= 8) { out.push((val >>> (bits - 8)) & 0xff); bits -= 8; }
  }
  return new Uint8Array(out);
}
async function totp(secretB32, { t0 = 0, step = 30, digits = 6, offset = 0 } = {}) {
  const counter = Math.floor((Date.now() / 1000 - t0 + offset * step) / step);
  const msg = new ArrayBuffer(8);
  new DataView(msg).setUint32(4, counter);                     // 大端 8 字节
  const key = await crypto.subtle.importKey('raw', base32Decode(secretB32),
    { name: 'HMAC', hash: 'SHA-1' }, false, ['sign']);
  const mac = new Uint8Array(await crypto.subtle.sign('HMAC', key, msg));
  const idx = mac[mac.length - 1] & 0x0f;                      // 动态截断
  const bin = ((mac[idx] & 0x7f) << 24) | (mac[idx + 1] << 16) | (mac[idx + 2] << 8) | mac[idx + 3];
  return String(bin % 10 ** digits).padStart(digits, '0');
}
async function verify(secretB32, input) {                      // ±1 窗口容忍时钟偏差
  for (const off of [-1, 0, 1]) {
    if ((await totp(secretB32, { offset: off })) === input) return true;
  }
  return false;
}
```
