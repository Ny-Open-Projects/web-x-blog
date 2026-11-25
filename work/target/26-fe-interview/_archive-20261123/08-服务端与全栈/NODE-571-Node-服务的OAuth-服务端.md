---
title: [NODE-571] Node 服务作为 OAuth Provider（开放授权中心）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-571：OAuth Provider 实现
**答**:
- 角色：自建授权中心（第三方应用接入我方用户资源——ARC-397 开放 API 的授权层）：授权码模式（authorization code + PKCE——公开客户端必须 PKCE）、refresh token 轮换（每次刷新换新 RT——旧 RT 失效检测重用 = 令牌泄露告警）。
- 关键实现：授权端点（登录态校验 + scope 授权页——用户显式同意）、redirect_uri 精确匹配（白名单——防开放重定向）、code 一次性（10 分钟有效期 + 用后即毁）、token 签发（access token 短效 + RT 长效绑客户端——RT 撤销机制）。
- scope 治理：scope 分级（只读/写入/敏感——敏感 scope 额外确认）、scope 到权限映射（资源服务按 scope 精细控制）、scope 收缩（授权变更——用户可查看/撤销已授权应用）。
- 安全：客户端认证（confidential client secret/私钥 JWT——public client 仅 PKCE）、令牌内省（资源服务校验 token——introspection 端点或本地 JWKS 验签）、授权审计（谁在何时授权了什么应用——用户可查）。
```javascript
// 授权端点核心校验
app.get('/oauth/authorize', async (req) => {
  if (!clients.verifyRedirect(req.clientId, req.redirectUri)) throw new InvalidRedirect(); // 精确匹配
  const code = await issueCode({ userId: req.user.id, clientId: req.clientId,
    scope: req.scope, challenge: req.codeChallenge, exp: 600 }); // 10min 一次性
  redirect(`${req.redirectUri}?code=${code}&state=${req.state}`);
});
// token：issueToken({ code 校验一次性 + PKCE verifier 比对 }) → access(15m) + refresh(轮换)
```
