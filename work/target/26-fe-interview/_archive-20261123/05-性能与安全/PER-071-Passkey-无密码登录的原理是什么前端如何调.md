---
title: [PER-071] Passkey 无密码登录的原理是什么？前端如何调用 WebAuthn？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-071：Passkey 无密码登录的原理是什么？前端如何调用 WebAuthn？

**答**：
- Passkey 基于公私钥：注册时服务端下发 challenge，认证器生成密钥对，**私钥留在设备**（TPM/安全芯片或密码管理器），服务端只存公钥；登录时用私钥对 challenge 签名，服务端验签。
- 相比密码的优势：无密码可撞库、私钥不出设备天然抗钓鱼（域名绑定 rp.id）、验证器内置生物识别。
- 前端职责：`navigator.credentials.create` 注册、`navigator.credentials.get` 认证；challenge、userId 必须来自服务端会话，前端不得自造。
- 兼容性兜底：不支持的平台回落密码 + 短信/OTP，登录页用 `PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable` 探测。

```javascript
// 注册 Passkey
async function registerPasskey() {
  // challenge 与 user.id 必须由服务端生成，经当前已认证会话下发
  const options = await fetch('/api/webauthn/register-options', { credentials: 'include' })
    .then((r) => r.json());
  const credential = await navigator.credentials.create({
    publicKey: {
      challenge: base64urlToBuffer(options.challenge),
      rp: { name: 'Example', id: 'example.com' },       // rp.id 绑定域名，抗钓鱼
      user: { id: base64urlToBuffer(options.userId), name: options.username, displayName: options.username },
      pubKeyCredParams: [{ type: 'public-key', alg: -7 }], // ES256
      authenticatorSelection: { residentKey: 'required', userVerification: 'required' },
      timeout: 60000,
    },
  });
  // 公钥上传服务端保存，私钥永远不会离开认证器
  await fetch('/api/webauthn/register', {
    method: 'POST', credentials: 'include',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(serializeCredential(credential)),
  });
}

// 登录 Passkey
async function loginPasskey() {
  const options = await fetch('/api/webauthn/login-options').then((r) => r.json());
  const assertion = await navigator.credentials.get({
    publicKey: { challenge: base64urlToBuffer(options.challenge), userVerification: 'required', timeout: 60000 },
  });
  const res = await fetch('/api/webauthn/verify', {
    method: 'POST', credentials: 'include',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(serializeAssertion(assertion)), // 签名 + authenticatorData，服务端用公钥验签
  });
  if (res.ok) location.assign('/home');
}
```

## 十二、接口与数据安全
