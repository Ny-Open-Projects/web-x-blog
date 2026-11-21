---
title: [ZSM-219] token 过期后 Query 全军覆没怎么联动刷新与恢复
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-219：token 过期后 Query 全军覆没怎么联动刷新与恢复

**答**：
- 401 统一在 fetch 层拦截：单飞（single-flight）刷新 token，刷新成功后重放原请求；Query 层无感知
- QueryCache 的 onError 收尾：仍 401 说明刷新失败 → 清缓存 + 跳登录；刷新成功重放的查询自然成功，无需 invalidate 全部
- 兜底：登录成功/登出时 `queryClient.clear()` 或按前缀 invalidate，避免上一账号数据残留（安全问题）
- 不要在多个 queryFn 里各自处理 401，收敛到请求层 + cache 事件两层，组件层零感知

```javascript
let refreshing = null
async function request(url, opt) {
  const res = await fetch(url, opt)
  if (res.status === 401 && !url.includes('/refresh')) {
    refreshing ??= refreshToken().finally(() => (refreshing = null))  // single-flight
    const ok = await refreshing
    if (ok) return request(url, opt)      // 重放原请求
    queryClient.clear(); location.href = '/login'   // 刷新失败
  }
  return res
}
```
