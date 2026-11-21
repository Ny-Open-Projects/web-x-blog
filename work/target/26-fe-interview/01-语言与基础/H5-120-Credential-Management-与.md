---
title: [H5-120] Credential Management 与 passkey 的前端流程概览。
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-120：Credential Management 与 passkey 的前端流程概览。
**答**：
- passkey = 基于 WebAuthn 的免密登录凭据：**公私钥对**，私钥留在设备/密码管理器，服务端只存公钥；`navigator.credentials` 是前端入口。
- 注册流程：服务端下发 challenge + userId → `navigator.credentials.create({ publicKey })` 弹出生物识别/PIN → 返回 attestation（公钥）交给服务端存库。
- 登录流程：服务端下发 challenge + allowCredentials → `navigator.credentials.get({ publicKey })` → 返回 assertion（签名）由服务端验签。
- 条件 UI（conditional mediation）：`get({ mediation: 'conditional' })` 在**用户名输入框自动填充**出已存 passkey，无感登录（配合 `autocomplete="username webauthn"`）。
- 支持检测：`window.PublicKeyCredential` 存在性 + `PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable()` 判断本机认证器；需 HTTPS。

```javascript
// 1) 能力检测
async function passkeySupported() {
  if (!window.PublicKeyCredential) return false;
  return PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable();
}

// 2) 注册：服务端先给 challenge
async function registerPasskey() {
  const options = await fetch('/api/webauthn/register-options')
    .then(r => r.json());                     // challenge, user, rp 等

  const credential = await navigator.credentials.create({
    publicKey: {
      ...options,
      challenge: base64ToBuffer(options.challenge),
      user: { ...options.user, id: base64ToBuffer(options.user.id) },
    },
  });

  // 上报公钥凭据（ArrayBuffer 序列化为 base64url）
  await fetch('/api/webauthn/register', {
    method: 'POST',
    body: JSON.stringify(serialize(credential)),
  });
}

// 3) 登录（含条件 UI：输入框自动填充 passkey）
async function conditionalLogin(inputEl) {
  const options = await fetch('/api/webauthn/login-options').then(r => r.json());
  try {
    const assertion = await navigator.credentials.get({
      mediation: 'conditional',               // 无感条件 UI
      publicKey: {
        ...options,
        challenge: base64ToBuffer(options.challenge),
      },
    });
    await fetch('/api/webauthn/verify', { method: 'POST', body: JSON.stringify(serialize(assertion)) });
  } catch { /* 用户未选择，静默 */ }
}

function base64ToBuffer(b64) {
  return Uint8Array.from(atob(b64.replace(/-/g, '+').replace(/_/g, '/')), c => c.charCodeAt(0));
}
```
