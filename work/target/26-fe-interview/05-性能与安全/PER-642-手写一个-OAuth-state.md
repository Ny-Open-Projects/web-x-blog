---
title: [PER-642] 手写一个 OAuth state/PKCE 客户端工具：生成并校验 state、生成 PKCE code_verifier/challenge
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-642：手写一个 OAuth state/PKCE 客户端工具：生成并校验 state、生成 PKCE code_verifier/challenge

**答**：
- PKCE 流程客户端职责：登录前生成 `code_verifier`（随机 43~128 字符）与 `code_challenge = BASE64URL(SHA256(verifier))`，把 challenge 随授权请求发出、verifier 存 sessionStorage；回调时带上 verifier 供后端换 token。
- 要点：state 与 verifier 都要**按 Tab 隔离存储**（sessionStorage 天然按 Tab），过期时间（10 分钟）清理防残留；state 校验失败（CSRF/错绑）要直接中断并告警，不能宽容放行。
- 边界：base64url 编码要去 padding；SHA256 用 WebCrypto 异步 API；回调校验一次后立即清除存储（防重放）。
- 评分点：Tab 隔离与一次性清理。

```javascript

const OAuthClient = {
  async begin(authorizeUrl, clientId, redirectUri) {
    const verifier = this.b64url(crypto.getRandomValues(new Uint8Array(32)));
    const challenge = this.b64url(new Uint8Array(
      await crypto.subtle.digest('SHA-256', new TextEncoder().encode(verifier))));
    const state = this.b64url(crypto.getRandomValues(new Uint8Array(16)));
    sessionStorage.setItem('oauth', JSON.stringify({ verifier, state, ts: Date.now() })); // Tab 隔离
    const u = new URL(authorizeUrl);
    u.search = new URLSearchParams({ client_id: clientId, redirect_uri: redirectUri,
      response_type: 'code', state, code_challenge: challenge,
      code_challenge_method: 'S256' });
    location.assign(u);
  },
  async callback(code, state) {
    const s = JSON.parse(sessionStorage.getItem('oauth') ?? 'null');
    sessionStorage.removeItem('oauth');                      // 一次性，防重放
    if (!s || s.state !== state || Date.now() - s.ts > 600000) {
      report('oauth-state-fail'); return null;               // 校验失败即中断
    }
    return { code, verifier: s.verifier };                   // 交后端换 token
  },
  b64url(bytes) {
    return btoa(String.fromCharCode(...bytes)).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
  },
}
```
