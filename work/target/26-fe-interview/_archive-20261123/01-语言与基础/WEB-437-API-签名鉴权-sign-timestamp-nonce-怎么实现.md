---
title: [WEB-437] API 签名鉴权 sign+timestamp+nonce 怎么实现
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-437：API 签名鉴权 sign+timestamp+nonce 怎么实现

**答**：
- 目的：开放 API 无登录态时的请求防篡改与防重放；参数+时间戳+随机数一起签名
- 组成：sign = HMAC(secret, 排序后的参数串 + timestamp + nonce)，服务端同样计算比对
- timestamp 限制窗口（如 ±5 分钟）挡老包；nonce 服务端短时去重挡窗口内重放；二者配合缺一不可
- secret 不能放前端公开代码——纯前端的签名只防君子，真正的开放 API 签名应由后端/网关代算或 App 内置混淆密钥
- 前端职责：参数按字典序拼接、URL 编码统一（空格 vs +、斜杠转义是经典踩坑点）

```javascript
async function sign(params, secret) {
  const keys = Object.keys(params).sort();
  const base = keys.map(k => `${k}=${encodeURIComponent(params[k])}`).join('&')
    + `&timestamp=${Date.now()}&nonce=${crypto.randomUUID()}`;
  const key = await crypto.subtle.importKey('raw', new TextEncoder().encode(secret),
    { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  const mac = await crypto.subtle.sign('HMAC', key, new TextEncoder().encode(base));
  return { base, sign: btoa(String.fromCharCode(...new Uint8Array(mac))) };
}
```
