---
title: [PER-136] SSO 回调页必须做哪些安全校验？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-136：SSO 回调页必须做哪些安全校验？

**答**：
- **state 校验**防 CSRF：发起时用 CSPRNG 生成 state 存 sessionStorage，回调时严格比对且**只消费一次**，不匹配立即中断。
- **redirect 白名单**：回调后的跳转目标来自发起时登记的白名单/相对路径，绝不信任回调 query 里的 redirect 参数（防开放重定向拿 code）。
- **code 交换在服务端**：code 换 token 走后端与 IdP 的接口（带 client_secret），前端只见会话 Cookie，token 永不出现在 URL 与前端存储。
- **nonce 防 token 重放**（OIDC）：id_token 里的 nonce 与本地保存值比对；回调页一次性使用后清 pending 状态。

```javascript
// SSO 回调四道闸：state 防 CSRF、redirect 白名单、code 服务端交换、pending 一次性
export async function handleOAuthCallback(query) {
  const pending = JSON.parse(sessionStorage.getItem('oauth_pending') || 'null');

  // 1. state 必须与发起时保存的完全一致
  if (!pending || query.state !== pending.state) throw new Error('state 校验失败，疑似 CSRF');

  // 2. 跳转目标只认发起时登记的相对路径，回调 query 里的 redirect 一律不信任
  const next = /^\/(?!\/)/.test(pending.redirect ?? '') ? pending.redirect : '/home';

  // 3. code 由后端与 IdP 交换 token，前端只见会话 Cookie
  await fetch('/api/auth/sso/callback', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ code: query.code, state: query.state }),
  });

  sessionStorage.removeItem('oauth_pending'); // 4. 一次性消费，防重放
  history.replaceState(null, '', location.pathname); // 清地址栏里的 code 与 state
  location.assign(next);
}

// 发起侧：state 用 CSPRNG 生成并登记跳转目标
export function startOAuth(scopes, redirect = location.pathname) {
  const state = Array.from(crypto.getRandomValues(new Uint8Array(16)),
    (b) => b.toString(16).padStart(2, '0')).join('');
  sessionStorage.setItem('oauth_pending', JSON.stringify({ state, redirect, ts: Date.now() }));
  location.assign(`https://idp.example.com/authorize?client_id=web&response_type=code&scope=${scopes}&state=${state}`);
}
```
