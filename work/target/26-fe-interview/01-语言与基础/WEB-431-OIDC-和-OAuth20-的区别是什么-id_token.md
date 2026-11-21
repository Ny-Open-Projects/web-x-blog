---
title: [WEB-431] OIDC 和 OAuth 2.0 的区别是什么
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 鉴权]
type: 面试题
---

## WEB-431：OIDC 和 OAuth 2.0 的区别是什么

**答**：
- 一句话：OAuth 2.0 是「授权」协议（让它访问我的资源），OIDC 是建在 OAuth 2.0 上的「认证」层（证明你是谁）
- 核心增量：授权响应里多一个 `id_token`——JWT 格式，含 iss/sub/aud/exp，还有用户名、邮箱等 claims
- 配套端点：userinfo（拿详细资料）、discovery（`/.well-known/openid-configuration` 自发现配置）、jwks（验签公钥）
- 前端注意：id_token 只做「身份断言」不做 API 凭证；验证要校验签名（走 jwks）、iss、aud、exp
- 典型误区：把 id_token 当 access_token 发给业务后端，后端拿它验签名看似能过，但语义错、权限模型乱

```javascript
// 解析并粗验 id_token（严格验签应在后端或用库完成）
const payload = JSON.parse(atob(idToken.split('.')[1].replace(/-/g, '+').replace(/_/g, '/')));
const ok = payload.aud === CLIENT_ID && payload.exp * 1000 > Date.now() && payload.iss === 'https://auth.example.com';
```
