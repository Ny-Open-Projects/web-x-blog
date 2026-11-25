---
title: [WEB-326] 企业内网选 SAML 还是 OIDC？给个判断依据。
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 鉴权]
type: 面试题
---

## WEB-326：企业内网选 SAML 还是 OIDC？给个判断依据。
**答**：
- SAML：XML 断言 + 浏览器重定向/POST，传统企业 AD/老系统支持好，但报文重、调试痛苦，前端主要是跳转方。
- OIDC：JSON + JWT，移动端/SPA 友好，生态新；新系统默认选 OIDC。
- 现实：ToB 产品常常两者都要接，用身份中台（如 Okta/Auth0）统一适配，业务端只对接中台一种协议。

```javascript
const pick = (env) => ({
  legacyAD: 'SAML', spaMobile: 'OIDC', both: '身份中台收敛',
}[env]);
console.log(pick('spaMobile')); // OIDC
// SAML 断言经浏览器 POST 传递（防 URL 泄露），OIDC 经回调参数传 code
```
