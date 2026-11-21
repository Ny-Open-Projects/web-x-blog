---
title: [PER-643] 手写一个 HMAC 请求签名器：防篡改 + 防重放的时间窗签名方案（前端侧实现）
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-643：手写一个 HMAC 请求签名器：防篡改 + 防重放的时间窗签名方案（前端侧实现）

**答**：
- 签名结构：`signature = HMAC-SHA256(secret, method + path + timestamp + bodyHash)`，请求带 `X-Timestamp` 与 `X-Signature`；服务端校验签名 + 时间窗（±5 分钟）+ nonce 去重，实现防篡改与防重放双目标。
- 前端要点：bodyHash 对原始 body 字符串算（先签名后 JSON 序列化顺序要固定——用稳定序列化）；secret 的管理是边界（见前端加密边界卡，长期 secret 放前端只能防君子，真正防篡改要服务端会话密钥）。
- 边界：GET 无 body 时 bodyHash 为空串的 hash；重试时 timestamp 要重新生成（旧签名过期即失效，天然防重放）；nonce 由客户端生成并上报，服务端窗口内去重。
- 评分点：稳定序列化与时间窗重试语义。

```javascript

async function signRequest(method, path, body, secret) {
  const ts = Date.now().toString();
  const nonce = crypto.randomUUID();
  const bodyStr = body === undefined ? '' : JSON.stringify(body);   // 稳定序列化
  const bodyHash = bodyStr ? await sha256Hex(bodyStr) : await sha256Hex('');
  const base = `${method.toUpperCase()}\n${path}\n${ts}\n${nonce}\n${bodyHash}`;
  const key = await crypto.subtle.importKey('raw', new TextEncoder().encode(secret),
    { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  const sig = await crypto.subtle.sign('HMAC', key, new TextEncoder().encode(base));
  const signature = btoa(String.fromCharCode(...new Uint8Array(sig)));
  return {
    headers: { 'X-Timestamp': ts, 'X-Nonce': nonce, 'X-Signature': signature },
    body: bodyStr,
  };
}
async function sha256Hex(s) {
  const d = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s));
  return [...new Uint8Array(d)].map(b => b.toString(16).padStart(2, '0')).join('');
}
// 服务端校验：重算 base 比对签名 + |now-ts| < 5min + nonce 未出现过
```
