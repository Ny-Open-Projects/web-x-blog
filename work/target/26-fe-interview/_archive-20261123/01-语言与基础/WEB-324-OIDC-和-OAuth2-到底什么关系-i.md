---
title: [WEB-324] OIDC 和 OAuth2 到底什么关系？id_token 是干嘛的？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 鉴权]
type: 面试题
---

## WEB-324：OIDC 和 OAuth2 到底什么关系？id_token 是干嘛的？
**答**：
- OAuth2 是授权框架（拿到 access_token 访问资源），不定义"你是谁"；OIDC 是 OAuth2 之上的身份层，回答"这个用户是谁"。
- OIDC 新增 id_token（JWT）：包含 sub（用户唯一标识）、iss、aud、exp，客户端本地验证即可知道登录者身份。
- 配套 /userinfo 接口和 scopes（openid profile email）；前端注意 id_token 只验身份不用于调 API，调 API 用 access_token。

```javascript
const idToken = decode(jwt);
// { iss: 'https://idp.com', aud: 'web-app', sub: 'u_123', exp: ... }
function verifyIdToken(t, client) {
  if (t.iss !== 'https://idp.com') throw '签发者不对';
  if (t.aud !== client.id) throw '受众不对';
  if (Date.now() / 1000 > t.exp) throw '过期';
  return t.sub; // 登录身份
}
console.log('id_token 认人，access_token 办事');
```
