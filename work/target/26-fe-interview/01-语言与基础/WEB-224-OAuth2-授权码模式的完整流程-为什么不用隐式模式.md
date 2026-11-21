---
title: [WEB-224] OAuth2 授权码模式的完整流程？为什么弃用隐式模式？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 鉴权]
type: 面试题
---

## WEB-224：OAuth2 授权码模式的完整流程？为什么弃用隐式模式？

**答**：
- 授权码流程：跳转授权页（带 client_id/redirect_uri/scope/state）→ 用户登录同意 → 带一次性 code 回跳 redirect_uri → 前端/后端用 code + client_secret 换 access_token → 拿 token 调 API。
- 关键设计：access_token 不经过浏览器 URL，只暴露短期一次性 code；state 随机值防 CSRF（回调时校验一致）。
- 弃用隐式模式（implicit）的原因：token 直接拼在 URL fragment 里返回，会进浏览器历史/Referer 泄漏，且无法做客户端认证。OAuth 2.1 已删除，SPA 一律用授权码 + PKCE。
- 前端工程要点：code 换 token 应放 BFF 后端做（secret 不落浏览器）；redirect_uri 必须精确匹配防开放重定向。

```javascript
// SPA + PKCE 授权跳转
async function login() {
  const verifier = base64url(crypto.getRandomValues(new Uint8Array(32)));
  const challenge = base64url(await sha256(verifier));
  sessionStorage.setItem('pkce_verifier', verifier);
  location.href = `https://auth.example.com/authorize?` +
    `client_id=spa&redirect_uri=${origin}/cb&response_type=code&` +
    `scope=profile&state=${crypto.randomUUID()}&code_challenge=${challenge}&code_challenge_method=S256`;
}
// 回调页：校验 state 后，把 code 发给 BFF 换 token
```
