---
title: [PER-1085] OAuth/授权码流程在前端的安全注意点
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1085：OAuth/授权码流程在前端的安全注意点

**答**：
- 授权码模式必须 PKCE（防止授权码拦截），隐式流程（implicit）已废弃。
- redirect_uri 精确匹配白名单，open redirect 缺陷会让授权码流向攻击者。
- state 参数防 CSRF（随机值回校验）；token 不放 URL fragment（浏览器历史泄露）。
- 前端只做跳转与回调接收，敏感交换在服务端完成（SPA 可用 PKCE 交换但要保护 refresh token）。

```javascript
// PKCE 客户端实现
async function startOAuth() {
  const verifier = btoa(crypto.getRandomValues(new Uint8Array(32)).join(''))
    .replace(/[+/=]/g, '');
  const challenge = btoa(String.fromCharCode(...new Uint8Array(
    await crypto.subtle.digest('SHA-256', new TextEncoder().encode(verifier)))))
    .replace(/[+/=]/g, '');
  const state = crypto.randomUUID();
  sessionStorage.setItem('oauth-state', state);
  sessionStorage.setItem('pkce-verifier', verifier);
  location.href = `/oauth/authorize?client_id=${CID}&redirect_uri=${REDIRECT}` +
    `&response_type=code&state=${state}&code_challenge=${challenge}` +
    `&code_challenge_method=S256`;
}
// 回调校验 state 后带 verifier 换 token
```
