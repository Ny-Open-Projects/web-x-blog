---
title: [NODE-036] OAuth2 中各服务端角色的职责是什么？简化版授权码流程如何实现？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-036：OAuth2 中各服务端角色的职责是什么？简化版授权码流程如何实现？
**答**：
- 四角色：**资源所有者**（用户）、**客户端**（第三方应用）、**授权服务器**（发 token，如公司 SSO）、**资源服务器**（校验 token 提供数据，如 GitHub API）。
- 授权码流程：客户端跳授权页（带 `client_id`/`redirect_uri`/`state`/`scope`）→ 用户登录并同意 → 授权服务器 302 回调带 **code**（一次性、10 分钟内）→ 客户端后端用 code + `client_secret` 换 token（code 在后端交换，防暴露）。
- 服务端要点：`redirect_uri` 必须严格白名单（防授权码劫持）、`state` 防 CSRF、PKCE（SAP/移动端无 secret 场景用 `code_verifier`/`code_challenge`）。

```javascript
// 简化版授权服务器（理解原理用，生产用 keycloak/logto/passport）
const Koa = require('koa');
const crypto = require('node:crypto');
const app = new Koa();

const clients = { 'app-frontend': { secret: 's3cret', redirectUris: ['https://app.example.com/cb'] } };
const authCodes = new Map(); // code → { clientId, uid, expires, redirectUri }

// 1. 授权端点
app.get('/oauth/authorize', async (ctx) => {
  const { client_id, redirect_uri, state, response_type } = ctx.query;
  const client = clients[client_id];
  if (!client || !client.redirectUris.includes(redirect_uri)) ctx.throw(400, 'redirect_uri 非法'); // 白名单强校验
  if (response_type !== 'code') ctx.throw(400, '仅支持授权码模式');
  // 真实场景：此处渲染登录页，用户登录同意后签发 code
  const code = crypto.randomBytes(16).toString('hex');
  authCodes.set(code, { clientId: client_id, uid: 42, expires: Date.now() + 10 * 60 * 1000, redirectUri: redirect_uri });
  ctx.redirect(`${redirect_uri}?code=${code}&state=${state}`);
});

// 2. 换 token 端点（后端对后端）
app.post('/oauth/token', async (ctx) => {
  const { code, client_id, client_secret, redirect_uri } = ctx.request.body;
  const record = authCodes.get(code);
  if (!record || record.expires < Date.now()) ctx.throw(400, 'code 无效或已过期');
  if (record.clientId !== client_id || clients[client_id].secret !== client_secret) ctx.throw(401, '客户端凭证错误');
  if (record.redirectUri !== redirect_uri) ctx.throw(400, 'redirect_uri 不一致'); // 防换包截获 code
  authCodes.delete(code); // code 一次性
  ctx.body = { access_token: 'jwt-xxx', token_type: 'Bearer', expires_in: 3600, refresh_token: 'yyy' };
});
app.listen(9000);
```
