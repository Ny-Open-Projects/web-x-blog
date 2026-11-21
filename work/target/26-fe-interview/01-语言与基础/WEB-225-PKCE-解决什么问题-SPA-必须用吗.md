---
title: [WEB-225] PKCE 解决什么问题？SPA 必须用吗？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 鉴权]
type: 面试题
---

## WEB-225：PKCE 解决什么问题？SPA 必须用吗？

**答**：
- PKCE（Proof Key for Code Exchange）解决「授权码被拦截」：恶意 App 注册同样的 redirect scheme 截获授权码，或系统浏览器回跳被劫持。
- 机制：发起授权时带上 `code_challenge = SHA256(code_verifier)`；换 token 时服务端要求出示原始 verifier 并校验哈希一致。截获了 code 没有 verifier 也换不到 token。
- SPA 必须用吗：是。OAuth 2.1 规定所有公共客户端（无 client_secret 的 SPA/App）强制 PKCE；即使 SPA 通过 BFF 代持 secret，PKCE 也是纵深防御。
- 细节：verifier 用加密随机数（43~128 字符），每次登录新生成，用完即弃。

```javascript
// PKCE 三步
const verifier = base64url(crypto.getRandomValues(new Uint8Array(32)));
// 1. 发授权: ...&code_challenge=SHA256(verifier)&code_challenge_method=S256
const challenge = base64url(await crypto.subtle.digest(
  'SHA-256', new TextEncoder().encode(verifier)));
// 2. 换 token 时出示 verifier
const body = new URLSearchParams({
  grant_type: 'authorization_code', code, redirect_uri,
  code_verifier: verifier,      // 服务端校验 SHA256(verifier) === challenge
});
```
