---
title: [PER-065] Token 有哪些泄露渠道？前端如何系统性地减少暴露面？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-065：Token 有哪些泄露渠道？前端如何系统性地减少暴露面？

**答**：
- 泄露渠道全解：**XSS 读取 storage**、**URL 查询参数**（进浏览器历史、Referer、网关日志）、**日志打印**（console 上报把 token 带走）、**Referer 头**（站外跳转带全 URL）、**第三方脚本**（共享 window 可读 storage）、**localStorage 持久化**（设备失窃即失守）。
- 防御优先级：优先 Cookie HttpOnly + SameSite（JS 读不到）；SPA 必须 JS 持有 token 时，**内存保存 + refresh token 旋转**，refresh 存 HttpOnly Cookie。
- 工程约束：token 永不出现在 URL；日志与埋点 SDK 统一脱敏白名单；出站请求统一拦截器禁止把 token 发往第三方域。

```javascript
// Token 安全仓库：只存内存，刷新走 HttpOnly Cookie，URL 与日志零暴露
const tokenStore = { access: null, expireAt: 0 };

async function getAccessToken() {
  if (tokenStore.access && Date.now() < tokenStore.expireAt - 30000) {
    return tokenStore.access; // 未过期直接用
  }
  // refresh token 在 HttpOnly Cookie 里，JS 拿不到也偷不走
  const res = await fetch('/api/auth/refresh', { method: 'POST', credentials: 'include' });
  if (!res.ok) { location.assign('/login'); throw new Error('need login'); }
  const data = await res.json();
  tokenStore.access = data.accessToken;       // 只进内存，不落 storage
  tokenStore.expireAt = Date.now() + data.expiresIn * 1000;
  return tokenStore.access;
}

// 出站拦截：token 只发自家域，第三方请求强制剥离 Authorization
fetch('/api/orders', { headers: { Authorization: `Bearer ${await getAccessToken()}` } });

// 日志脱敏：统一包装，任何 token 形态的值都不进日志
const origLog = console.log;
console.log = (...args) => origLog(...args.map((a) =>
  typeof a === 'string' ? a.replace(/eyJ[\w-]+\.[\w-]+\.[\w-]+/g, '[REDACTED_JWT]') : a
));
```
