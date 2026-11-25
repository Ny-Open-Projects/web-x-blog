---
title: [WEB-317] OAuth2 的四种授权模式分别什么时候用？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 鉴权]
type: 面试题
---

## WEB-317：OAuth2 的四种授权模式分别什么时候用？
**答**：
- 授权码模式（最标准）：有后端的 Web 应用，授权码经前端回调换取 token，安全性靠服务端保密 client_secret。
- PKCE 授权码：无后端场景（SPA/移动端）替代 client_secret，防止授权码被截获。
- 客户端凭证：服务与服务间调用（无用户参与）；密码模式：高度信任的一方应用，现基本弃用；隐式模式已废弃（token 走 URL 泄露风险）。

```javascript
// 授权码 + PKCE 流程
const pkce = {
  verifier: rand64(),
  challenge: b64(sha256(rand64())),
};
// 1. /authorize?response_type=code&code_challenge=...&redirect_uri=...
// 2. 用户登录同意 → 302 回调?code=xxx
// 3. POST /token { code, code_verifier } → { access_token, refresh_token }
console.log('SPA 必配 PKCE：授权码即使被截也无法换 token');
```
