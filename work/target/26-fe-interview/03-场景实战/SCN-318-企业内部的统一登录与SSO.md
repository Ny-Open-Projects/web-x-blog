---
title: [SCN-318] 企业 SSO——统一登录多系统共享的接入体验？
date: 2026-11-20
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-318：企业 SSO（一个登录多系统通行的前端接入）怎么实现？

**答**:
- SSO 流程：统一认证中心（OAuth2/OIDC/CAS），跳转流程（子系统未登录→重定向认证中心→登录→带 code 回跳→子系统换 token），静默续期（token 过期→iframe 静默刷新/刷新 token——无感续期 SCN-010 无感刷新复用）。
- 前端接入体验：各子系统接入 SDK 统一（登录拦截/换 token/登出广播——SDK 封装避免各系统自己实现走样）、登出联动（单点登出：认证中心登出→各系统登出广播——SCN 多标签同步复用机制）、多系统会话一致性（认证中心会话是根会话）。
- 异常与降级：认证中心故障（子系统降级本地缓存 token 宽限期——可用性优先的兜底）、回跳丢失（第三方 cookie 限制的浏览器——SameSite/分区 cookie 处理，或改用 token 中转页）、慢回跳体验（回跳 loading+超时重试）。
- 安全细节：state 防 CSRF、redirect_uri 白名单（开放重定向漏洞防护）、token 不进 URL（history state/内存持有）、多端会话管理（设备列表与踢出）。

```javascript
// SSO SDK
sso.init({ clientId, redirectUri, authCenter });
router.beforeEach(async (to) => {
  if (!sso.token) return sso.login(to.fullPath);   // 重定向认证中心
});
sso.on('expired', () => sso.silentRenew());        // iframe 静默续期
sso.on('logout', () => clearLocalAndRedirect());   // 单点登出广播
// 安全：state 随机数校验；redirectUri 白名单服务端校验；
//   token 存内存 + sessionStorage（不进 URL）。
// 降级：authCenter down → 宽限期用缓存 token（≤30min）。
```
