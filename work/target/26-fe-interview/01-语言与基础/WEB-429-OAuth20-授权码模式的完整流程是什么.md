---
title: [WEB-429] OAuth 2.0 授权码模式的完整流程是什么
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 鉴权]
type: 面试题
---

## WEB-429：OAuth 2.0 授权码模式的完整流程是什么

**答**：
- 流程：前端跳转授权页（带 client_id、redirect_uri、scope、state、code_challenge）→ 用户登录授权 → 携 code 回跳 → 后端用 code + client_secret 换 token
- 关键设计：code 是一次性、短时效（几分钟）的中间凭证，token 交换在后端完成，secret 不暴露给浏览器
- state 是防 CSRF 的必填随机串：回跳时必须校验，否则攻击者可把自己的 code 注入受害者会话
- SPA 场景：没有后端或 secret 无法保密，就用 PKCE（下题），绝不能用隐式模式（已废弃）
- 前端职责：正确拼接授权 URL、保存/校验 state、处理错误回跳（access_denied 等）、授权后的登录态接管

```javascript
// 发起授权跳转
const state = crypto.randomUUID();
sessionStorage.setItem('oauth_state', state);
const url = new URL('https://auth.example.com/authorize');
url.searchParams.set('response_type', 'code');
url.searchParams.set('client_id', CLIENT_ID);
url.searchParams.set('redirect_uri', location.origin + '/callback');
url.searchParams.set('scope', 'profile order');
url.searchParams.set('state', state);
location.href = url;

// 回调页校验
const p = new URLSearchParams(location.search);
if (p.get('state') !== sessionStorage.getItem('oauth_state')) {
  throw new Error('state 校验失败，疑似 CSRF');
}
```
