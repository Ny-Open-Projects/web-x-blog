---
title: [PER-655] 手写一个 WebAuthn 注册与断言流程（浏览器侧）：创建凭据、请求断言与结果校验要点
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-655：手写一个 WebAuthn 注册与断言流程（浏览器侧）：创建凭据、请求断言与结果校验要点

**答**：
- 注册（navigator.credentials.create）：服务端下发 challenge，浏览器生成公钥凭据（生物识别/安全钥匙），把公钥与 attestation 交给服务端绑定账号。
- 登录（navigator.credentials.get）：服务端下发新 challenge + allowCredentials，浏览器用私钥签名 challenge 返回断言，服务端用注册公钥验签——**challenge 一次性与 origin 校验是核心**。
- 前端要点：challenge 直接透传 base64url（别在前端做业务转换）；userHandle/credentialId 的编码转换（ArrayBuffer <-> base64url）；用户可选 `userVerification: 'required'` 强制生物校验。
- 边界：不支持的浏览器降级到 TOTP；排除凭据列表（excludeCredentials）防同一把钥匙重复注册。

```javascript

const b64u = (buf) => btoa(String.fromCharCode(...new Uint8Array(buf)))
  .replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
const fromB64u = (s) => Uint8Array.from(atob(s.replace(/-/g, '+').replace(/_/g, '/')), c => c.charCodeAt(0));

async function register(username) {
  const { challenge, userId } = await api('/webauthn/register-options');
  const cred = await navigator.credentials.create({
    publicKey: {
      challenge: fromB64u(challenge),
      rp: { name: 'Example', id: location.hostname },
      user: { id: fromB64u(userId), name: username, displayName: username },
      pubKeyCredParams: [{ type: 'public-key', alg: -7 }],      // ES256
      authenticatorSelection: { userVerification: 'required', residentKey: 'preferred' },
      excludeCredentials: await getExistingCreds(),              // 防重复注册同一钥匙
    },
  });
  // 上报 { id: cred.id, rawId: b64u(cred.rawId), response.clientDataJSON/attestationObject }
  return api('/webauthn/register-verify', serialize(cred));
}
async function login() {
  const { challenge } = await api('/webauthn/assert-options');
  const assert = await navigator.credentials.get({
    publicKey: { challenge: fromB64u(challenge), userVerification: 'required' },
  });
  // 服务端：验签 challenge + clientDataJSON.origin === 域名 + challenge 未用过
  return api('/webauthn/assert-verify', serialize(assert));
}
```
