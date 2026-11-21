---
title: [WEB-430] PKCE 是什么，为什么 SPA 必须带
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 鉴权]
type: 面试题
---

## WEB-430：PKCE 是什么，为什么 SPA 必须带

**答**：
- PKCE（ Proof Key for Code Exchange）：授权前生成随机 code_verifier，哈希出 code_challenge 随跳转带上；换 token 时出示原始 verifier
- 解决的问题：纯前端应用没有 secret，攻击者若截获授权码（自定义 scheme 回跳被劫持、历史记录泄漏），没有 verifier 依然换不到 token
- 流程三步：verifier（43~128 位随机串）→ challenge = BASE64URL(SHA256(verifier)) → 换 token 时带 verifier，服务端哈希比对
- 隐式模式（response_type=token）已被 OAuth 2.1 废弃，面试答出这一点是加分项
- 工程要点：verifier 存 sessionStorage（回调同 tab 可读），不要进 URL 或 localStorage 长存

```javascript
// 生成 PKCE 参数
async function pkce() {
  const verifier = base64url(crypto.getRandomValues(new Uint8Array(32)));
  const digest = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(verifier));
  return { verifier, challenge: base64url(new Uint8Array(digest)) };
}
```
