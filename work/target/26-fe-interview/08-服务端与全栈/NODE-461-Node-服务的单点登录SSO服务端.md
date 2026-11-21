---
title: [NODE-461] Node 服务的 SSO（单点登录）服务端架构如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-461：SSO 服务端架构
**答**:
- SSO 中心化：统一认证中心（IdP）持有登录会话，各应用（SP）登录时重定向 IdP 验证——OIDC/SAML 标准协议（OIDC 为主流：id_token + access_token）。
- 会话协作：SP 本地会话（短）+ IdP 全局会话（长）——SP 会话过期静默续（oidc-client 的 silent renew iframe）不打断用户；用户登录一次，多应用免登。
- 单点登出：SP 登出 → 通知 IdP → IdP 广播各 SP（front-channel：隐藏 iframe 逐个清；back-channel：IdP 回调各 SP 注销接口）——logout 必须全链路否则"登出了还在登录态"事故。
- 安全：state + nonce 防 CSRF/重放、redirect_uri 白名单严格校验（开放重定向是 SSO 经典漏洞 ARC-355）、id_token 验签（JWKS 轮换）、token 短时效 + refresh。
- 企业集成：LDAP/AD 对接（企业内部 IdP 桥接）、多 IdP 路由（邮箱域名 → 对应 IdP）。
```javascript
// OIDC SP 中间件要点
app.use(oidc({
  issuer: 'https://sso.example.com',
  client_id: 'bff', redirect_uri: 'https://app.example.com/cb',
  scope: 'openid profile',
  silent_renew: true,                                            // iframe 静默续期
  logout_cb: async () => clearLocalSession()                     // back-channel 注销回调
}));
// /cb 校验 state（会话存储比对）→ 验签 id_token（JWKS）→ 建本地会话
```
