---
title: [ZSM-011] 如何在 React 组件外（路由守卫、定时器、事件回调）读写 Zustand store？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-011：如何在 React 组件外（路由守卫、定时器、事件回调）读写 Zustand store？
**答**：
- store 创建函数返回的对象就是 vanilla store：`getState()` 读最新值、`setState()` 写、`subscribe()` 订阅，全部可在组件外同步调用。
- 不能在组件外调用 `useStore()`（那是 hook），直接用 getState 可避免「为了拿状态而伪造组件」的别扭写法。
- 典型场景：axios 拦截器里取 token、路由守卫判断登录态、WebSocket onmessage 里推 IM 消息。
- 注意并发：getState 返回当前快照引用，异步回调里多次读取要重新调用，不要缓存旧快照。

```javascript
const useAuth = create(set => ({ token: '', setToken: t => set({ token: t }) }))

// axios 拦截器：组件外读
axios.interceptors.request.use(cfg => {
  cfg.headers.Authorization = `Bearer ${useAuth.getState().token}`
  return cfg
})

// WebSocket：组件外写
ws.onmessage = e => {
  const msg = JSON.parse(e.data)
  useImStore.setState(s => ({ messages: [...s.messages, msg] }))
}
```
