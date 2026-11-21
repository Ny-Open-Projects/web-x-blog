---
title: [WEB-454] WebAuthn/Passkey 是什么，前端怎么接入
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-454：WebAuthn/Passkey 是什么，前端怎么接入

**答**：
- WebAuthn：基于公私钥的无密码认证；私钥留在设备安全芯片，服务端只存公钥——数据库泄漏也拿不到可登录的凭证
- Passkey 是 WebAuthn 的产品化叫法，密钥可跨设备云同步（iCloud/Google），登录从「输密码」变成「生物识别确认」
- 前端流程：注册（服务端下发 challenge → `navigator.credentials.create()` → 公钥上交）与登录（challenge → `navigator.credentials.get()` → 签名上交）
- 兼容降级：检测 `window.PublicKeyCredential`，不支持时回退密码+2FA
- 前端注意：challenge、origin、RP ID 的校验都在服务端，前端别自作主张；错误处理要区分「用户取消」与「不支持」

```javascript
if (window.PublicKeyCredential) {
  const cred = await navigator.credentials.get({
    publicKey: await fetch('/api/webauthn/options').then(r => r.json()),
  });
  await fetch('/api/webauthn/verify', { method: 'POST', body: JSON.stringify(cred) });
}
```
