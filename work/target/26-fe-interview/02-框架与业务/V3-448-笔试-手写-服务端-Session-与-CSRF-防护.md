---
title: [V3-448] 笔试：手写 CSRF 防护中间件（双提交 Cookie + SameSite）
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-448：笔试：手写 CSRF 防护中间件（双提交 Cookie + SameSite）
**答**：实现 CSRF 中间件：登录时下发 csrf token（cookie 可读版 + session 存储版）；写操作（POST/PUT/DELETE）校验请求头 X-CSRF-Token 与 session 中的一致；GET 与开放接口跳过；失败 403。

```javascript
export default defineEventHandler(async (event) => {
  const method = event.method
  if (['GET', 'HEAD', 'OPTIONS'].includes(method)) return
  if (event.path.startsWith('/api/open/')) return // 开放接口跳过
  const sessionToken = getSession(event)?.csrf
  const headerToken = getHeader(event, 'x-csrf-token')
  const cookieToken = parseCookies(event).csrf
  if (!sessionToken) {
    // 首次访问下发
    const token = crypto.randomUUID()
    setCookie(event, 'csrf', token, { sameSite: 'lax', secure: true, httpOnly: false }) // 前端需读
    getSession(event).csrf = token
    return
  }
  // 双提交校验：header 与 cookie 一致 且 header 与 session 一致
  if (headerToken !== cookieToken || headerToken !== sessionToken) {
    throw createError({ statusCode: 403, statusMessage: 'CSRF token invalid' })
  }
})
// 前端：读 cookie csrf 放入请求头；SameSite=Lax 是第二道防线
```
**评分点**：
- 双提交 Cookie 原理（cookie 可读 + header 比对，跨站攻击者读不到 cookie）。
- 安全方法跳过、开放接口白名单。
- SameSite=Lax 与 CSRF 双防线关系。
- 403 语义正确。
