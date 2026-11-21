---
title: [WEB-150] Passkey/WebAuthn 的注册与登录流程是怎样的？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-150：Passkey/WebAuthn 的注册与登录流程是怎样的？
**答**：
- 注册：服务端下发 challenge → 浏览器调 navigator.credentials.create() → 认证器（指纹/FaceID/安全钥匙）生成密钥对，私钥不出设备 → 公钥 + credentialId 上报服务端存档。
- 登录：服务端下发新 challenge → navigator.credentials.get() → 认证器用私钥对 challenge 签名 → 服务端用存档公钥验签。
- 安全本质：挑战-应答 + 站点域绑定（rp.id），钓鱼站点拿不到可用凭据，天然防钓鱼防撞库。
- 前端要点：challenge 必须服务端随机生成且一次性；ArrayBuffer 的编码/解码工具函数必配；体验上做"密码与 passkey 优先"的分流。

```javascript
// 注册：浏览器请求认证器生成凭据
const credential = await navigator.credentials.create({
  publicKey: {
    challenge: new Uint8Array(serverOptions.challenge),        // 服务端一次性随机数
    rp: { name: 'Example', id: 'example.com' },
    user: { id: new TextEncoder().encode(serverOptions.userId), name: 'u@example.com', displayName: 'U' },
    pubKeyCredParams: [{ type: 'public-key', alg: -7 }],       // ES256
    authenticatorSelection: { residentKey: 'required', userVerification: 'preferred' },
  },
});
// 把公钥与 credentialId 上报（ArrayBuffer 转 base64url 后 POST）
await fetch('/api/webauthn/register', { method: 'POST', body: serialize(credential) });

// 登录：拿到 challenge 后让认证器签名
const assertion = await navigator.credentials.get({
  publicKey: { challenge: new Uint8Array(loginOptions.challenge), rpId: 'example.com' },
});
await fetch('/api/webauthn/login', { method: 'POST', body: serialize(assertion) }); // 服务端用公钥验签
```

## 二十五、安全攻防专题
