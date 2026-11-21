---
title: [WEB-147] SSO 单点登录的原理是什么？CAS 和 OIDC 有什么区别？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-147：SSO 单点登录的原理是什么？CAS 和 OIDC 有什么区别？
**答**：
- 核心思想：把登录收敛到独立的认证中心（IdP），各业务系统只做"验证票据"，用户登录一次即可访问多个系统。
- CAS 模式：业务系统重定向到 CAS 登录 → CAS 发票据 ticket 回来 → 业务系统拿 ticket 去 CAS 后端验证 → 建立本系统会话。
- OIDC：在 OAuth2.0 上加了一层身份语义——id_token（JWT）直接声明"你是谁"，userinfo 接口补充属性，access_token 才是调 API 的凭证。
- 关键体验：回访时业务系统发现未登录，重定向到 CAS，CAS 的会话 Cookie 还在 → 免密直接发新票据，用户无感。
- 前端职责：正确处理回调路由、保管好 state/nonce、登出要联动 IdP 单点登出。

```javascript
// OIDC 授权码模式下的前端发起侧（nonce 防 id_token 重放）
const oidc = {
  authorizationEndpoint: 'https://sso.example.com/authorize',
  clientId: 'web-app',
  redirectUri: 'https://app.example.com/callback',
  scope: 'openid profile email',   // openid 必带，启用 OIDC 身份语义
  nonce: crypto.randomUUID(),      // IdP 会把它原样放回 id_token
};
sessionStorage.setItem('oidc_nonce', oidc.nonce);
location.assign(
  `${oidc.authorizationEndpoint}?response_type=code&client_id=${oidc.clientId}` +
  `&redirect_uri=${encodeURIComponent(oidc.redirectUri)}&scope=${oidc.scope}&nonce=${oidc.nonce}`
);
```
