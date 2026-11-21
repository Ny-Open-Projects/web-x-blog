---
title: [ZSM-409] 笔试：手写单飞 token 刷新（并发 401 只刷一次）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-409：手写单飞 token 刷新（并发 401 只刷一次）
**需求**：实现 `authedFetch(url, opt)`：1) 请求 401 时触发刷新 token；2) 并发多个 401 只发起一次刷新（单飞），其余等待同一 Promise；3) 刷新成功后所有等待者用新 token 重放原请求；4) 刷新失败广播登出（清状态 + 跳登录），等待者 reject；5) 刷新接口自身 401 直接登出（防循环）；6) 重放次数上限 1 次（防死循环）。

```javascript
let refreshing = null
let currentToken = localStorage.getItem('token')

async function authedFetch(url, opt = {}, _retry = true) {
  const res = await fetch(url, { ...opt, headers: { ...opt.headers, Authorization: `Bearer ${currentToken}` } })
  if (res.status !== 401) return res
  if (url.includes('/refresh') || !_retry) {
    logout(); throw new Error('auth failed')             // 防循环
  }
  refreshing ??= refreshToken().finally(() => (refreshing = null))   // 单飞
  const ok = await refreshing
  if (!ok) { logout(); throw new Error('session expired') }
  return authedFetch(url, opt, false)                    // 重放一次（上限）
}

async function refreshToken() {
  try {
    const r = await fetch('/api/refresh', { method: 'POST', credentials: 'include' })
    if (!r.ok) return false
    const { token } = await r.json()
    currentToken = token; localStorage.setItem('token', token)
    return true
  } catch { return false }
}

function logout() {
  currentToken = null
  localStorage.removeItem('token')
  bus.emit('auth:invalid')                               // 广播清场
}
```
**评分点**：
- 单飞核心：`refreshing ??= refreshToken()`，所有 401 等待同一 Promise，finally 置空允许下次刷新
- 防循环三保险：刷新接口不重试、_retry 上限 1 次、刷新失败统一登出
- 重放使用新 token；登出是广播清场而非散落处理
- 刷新竞态边界（刷新期间新请求直接排队等刷新完成）可作为追问加分
