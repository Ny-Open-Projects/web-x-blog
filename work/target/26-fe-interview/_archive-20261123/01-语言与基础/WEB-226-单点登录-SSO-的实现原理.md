---
title: [WEB-226] 单点登录（SSO）的实现原理？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 鉴权]
type: 面试题
---

## WEB-226：单点登录（SSO）的实现原理？

**答**：
- 核心思路：登录态收敛在统一认证中心（CAS/OAuth2/OIDC IdP），各子系统只存「本站的会话」，登录态由认证中心的 cookie 判定。
- 流程：用户访问系统 A 未登录 → 跳到 SSO 认证中心 → 中心若已登录（有自己的全局会话 cookie）直接签发票据回跳 A → A 用票据换会话；未登录则先在中心登录一次。此后访问系统 B，中心发现已登录，免密发票据。
- 现代实现是 OIDC（OAuth2 + 身份层）：A 拿 code 换 id_token（JWT，含用户身份），本地验证签名即建立会话。
- 注销单点（SLO）难做：需要认证中心广播登出到各子系统（front-channel/back-channel logout），实践中常只做中心登出 + 短会话兜底。

```javascript
// 系统A检测未登录 → 跳SSO（伪码）
app.get('/login', (req, res) => {
  const redirect = encodeURIComponent(`${req.protocol}://${req.host}/sso/cb`);
  res.redirect(`https://sso.example.com/authorize?client_id=appA&redirect_uri=${redirect}&state=${req.session.state = rand()}`);
});
// 回跳携带 code，服务端换 id_token 建立本地 session
```
