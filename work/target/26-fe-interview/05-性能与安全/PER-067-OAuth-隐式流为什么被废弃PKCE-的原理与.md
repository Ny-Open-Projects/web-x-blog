---
title: [PER-067] OAuth 隐式流为什么被废弃？PKCE 的原理与前端实现是什么？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-067：OAuth 隐式流为什么被废弃？PKCE 的原理与前端实现是什么？

**答**：
- 隐式流把 access token 直接放在 **URL fragment** 返回，token 会进浏览器历史、可能被恶意 JS 读取，且无法做客户端认证，OAuth 2.1 已明确废弃。
- PKCE（Proof Key for Code Exchange）：客户端先生成随机 `code_verifier`，把其 SHA-256 作为 `code_challenge` 发起授权；用授权码换 token 时必须带上原 `code_verifier`，服务端比对哈希。
- 价值：授权码被中间人或恶意 App 截获也无法换 token（没有 verifier），SPA 无后端也能安全使用授权码流。
- 落地细节：verifier 用 crypto 随机生成 43-128 字符；state 防 CSRF；redirect_uri 精确匹配。

```javascript
// SPA 端 PKCE：生成 verifier 与 challenge，再发起授权码请求
function base64url(buf) {
  return btoa(String.fromCharCode(...new Uint8Array(buf)))
    .replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}

async function createPkcePair() {
  const verifier = base64url(crypto.getRandomValues(new Uint8Array(32))); // 随机 43 字符
  const digest = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(verifier));
  return { verifier, challenge: base64url(digest) }; // challenge = BASE64URL(SHA256(verifier))
}

async function login() {
  const { verifier, challenge } = await createPkcePair();
  sessionStorage.setItem('pkce_verifier', verifier); // 换 token 时要用，会话级存储
  const state = base64url(crypto.getRandomValues(new Uint8Array(16)));
  sessionStorage.setItem('oauth_state', state);
  const authUrl = new URL('https://auth.example.com/authorize');
  authUrl.search = new URLSearchParams({
    response_type: 'code',
    client_id: 'spa-client',
    redirect_uri: 'https://app.example.com/callback',
    scope: 'openid profile',
    state,                                  // 防 CSRF
    code_challenge: challenge,
    code_challenge_method: 'S256',          // 声明哈希方式，不能用 plain
  }).toString();
  location.assign(authUrl);                 // 跳转授权页，回调带回 code
}

// 回调页：用 code + verifier 换 token，token 不经过 URL
async function exchangeCode(code) {
  const verifier = sessionStorage.getItem('pkce_verifier');
  const res = await fetch('/api/auth/token', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ code, code_verifier: verifier, redirect_uri: 'https://app.example.com/callback' }),
  });
  return res.json(); // { accessToken, expiresIn } 由代理服务端与授权服务器交互
}
```
