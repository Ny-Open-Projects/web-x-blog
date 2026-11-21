---
title: [SCN-490] 笔试题——实现 SSO 回跳流程（state 校验/code 交换/防开放重定向）？
date: 2026-11-20
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-490：手写 SSO 回跳：state 防 CSRF、code 交换 token、redirect_uri 白名单

**需求与边界**：
- 输入：回跳 URL 参数；输出：登录态。
- 边界要求：① state 随机数校验（发起时存储——防 CSRF）；② code 只能用一次（重放防护）；③ redirect_uri 白名单校验（防开放重定向）；④ token 不进 URL（内存/会话存储）；⑤ 回跳失败体验（错误码分型提示）。

**答**：
```javascript
// 发起：login(returnTo)
function login(returnTo) {
  const state = uid();                         // 随机 state
  sessionStorage.setItem('sso_state', state);
  sessionStorage.setItem('sso_return', sanitizeReturn(returnTo));
  location.href = `${AUTH}/authorize?client_id=X&` +
    `redirect_uri=${CALLBACK}&state=${state}&response_type=code`;
}
const sanitizeReturn = (p) =>                  // 防开放重定向
  p?.startsWith('/') && !p.startsWith('//') ? p : '/';
// 回跳：callback?code&state
async function handleCallback({ code, state }) {
  const saved = sessionStorage.getItem('sso_state');
  if (!state || state !== saved)
    throw new Error('STATE_MISMATCH');         // CSRF 防护
  sessionStorage.removeItem('sso_state');      // state 一次性
  const token = await api.exchange(code);      // code→token（后端换）
  setSession(token);                           // 内存+sessionStorage
  location.replace(sessionStorage.getItem('sso_return') || '/');
}
// code 一次性：后端换 token 时认证中心标记已用（重放拒绝）；
// 回跳失败：error=access_denied → 分型提示（拒绝/过期/配置错）。
```

**评分点**:
- state 随机+存储+一次性校验（CSRF 防护完整）。
- sanitizeReturn 防开放重定向（// 与外域拦截）。
- code 交换在后端（token 不进 URL/前端明文）。
- 回跳失败分型提示（用户体验）。
