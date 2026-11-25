---
title: [MFW-862] 怎么用 beforeLoad 做鉴权重定向又不丢失用户原本要访问的地址
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-862：怎么用 beforeLoad 做鉴权重定向又不丢失用户原本要访问的地址

**答**：
- 结论：重定向时把当前地址编码进 redirect 的 search（?redirect=/original），登录成功后读回跳回，避免硬编码首页。
- 落地：beforeLoad 抛 redirect({ to: /login, search: { redirect: location.href } })；登录页校验 redirect 为站内路径，防开放重定向。
- 追问钩子：怎么防开放重定向？——redirect 必须以斜杠开头且不含协议/跨域，或服务端签名校验。

```javascript
// beforeLoad：带上原始地址
beforeLoad: async ({ location }) => {
  if (!(await isLoggedIn())) {
    throw redirect({ to: '/login', search: { redirect: location.href } });
  }
}

// 登录页：安全跳回（防开放重定向）
function safeRedirect(to) {
  return to && to.startsWith('/') && !to.startsWith('//') ? to : '/';
}
async function onLogin() {
  await login();
  navigate({ to: safeRedirect(route.search.redirect) });
}
```
