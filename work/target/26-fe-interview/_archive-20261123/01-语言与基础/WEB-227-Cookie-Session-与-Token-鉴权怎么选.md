---
title: [WEB-227] Cookie-Session 与 Token 鉴权怎么选？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 鉴权]
type: 面试题
---

## WEB-227：Cookie-Session 与 Token 鉴权怎么选？

**答**：
- Cookie-Session：登录态存服务端（内存/Redis），cookie 只存 session ID。优点：可主动注销、体积小、HttpOnly 防 XSS 偷取；缺点：依赖服务端状态，跨域/多端（App）不友好，水平扩展要共享存储。
- Token（JWT）：登录态签进 token，服务端无状态，天然支持多端与微服务间传递。缺点：无法主动撤回（需黑名单回补状态）、payload 占请求头体积、依赖 localStorage 时怕 XSS。
- 选择经验：传统 Web 单体选 session；多端/微服务/API 开放平台选 JWT（短有效期+refresh）；对安全要求极高的支付类用 session + 双因素。
- 混合方案很常见：BFF 层用 session cookie 面向浏览器（HttpOnly），BFF 与微服务之间用 JWT 传递用户上下文。

```javascript
// 两套方案对比示意
// Session:
//   浏览器: Cookie: sid=abc (HttpOnly)
//   服务端: redis.get('sess:abc') → { userId, roles }
// JWT:
//   浏览器: Authorization: Bearer eyJhbGci...
//   服务端: jwt.verify(token) → { userId, roles } 无需查库
if (req.headers.authorization) {
  req.user = verifyJWT(req.headers.authorization.slice(7)); // 无状态
} else if (req.cookies.sid) {
  req.user = await redis.hgetall(`sess:${req.cookies.sid}`); // 可注销
}
```
