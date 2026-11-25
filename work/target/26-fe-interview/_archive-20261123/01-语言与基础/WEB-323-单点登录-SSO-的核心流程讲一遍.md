---
title: [WEB-323] 单点登录 SSO 的核心流程讲一遍？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 鉴权]
type: 面试题
---

## WEB-323：单点登录 SSO 的核心流程讲一遍？
**答**：
- 统一认证中心（IdP）：业务 A 未登录 → 跳转 IdP，IdP 有全局会话则直接发授权码回来，没有则先登录一次。
- 拿到 token 后业务 A 建立自己的局部会话；用户访问业务 B 时再跳 IdP，全局会话仍在 → 免登录直接放行，这就是"单点"。
- 登出要单点登出：IdP 通知各业务清局部会话，否则"登出了 A，B 还在登录态"。

```javascript
// CAS/OIDC 通用流程
const sso = (user, app) => {
  if (!user.idpSession) return redirect('/idp/login?service=' + app); // 首次登录
  const code = issueCode(user, app);           // IdP 发码
  return redirect(app + '/cb?code=' + code);   // 业务端换 token/建会话
};
// 访问 appB：idpSession 仍在 → 直接发码，免登录
console.log('一次登录，处处通行；登出必须广播清会话');
```
