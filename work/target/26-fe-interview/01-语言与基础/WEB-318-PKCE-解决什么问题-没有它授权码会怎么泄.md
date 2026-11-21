---
title: [WEB-318] PKCE 解决什么问题？没有它授权码会怎么泄露？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 鉴权]
type: 面试题
---

## WEB-318：PKCE 解决什么问题？没有它授权码会怎么泄露？
**答**：
- SPA/移动端没有 client_secret，任何拿到授权码+client_id 的程序都能换 token；PKCE 用一次性 verifier/challenge 绑定"发起授权的那个实例"。
- 只有持有原 verifier 的客户端能换 token，中间截获授权码的程序无 verifier 无法兑现。
- 现在 PKCE 是 OAuth2.1 强制项，连有后端的应用也建议开启（防授权码注入）。

```javascript
function pkce() {
  const verifier = base64url(crypto.getRandomValues(new Uint8Array(32)));
  const challenge = base64url(crypto.subtle.digest('SHA-256', verifier));
  return { verifier, challenge };
}
// 换 token 时服务器校验 sha256(verifier) === challenge
console.log('发起时给 challenge，兑现时对 verifier，一一绑定');
```
