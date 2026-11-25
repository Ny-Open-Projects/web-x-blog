---
title: [ZSM-634] focusManager 与 online 状态监听：refetchOnWindowFocus 的内部设计
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-634：focusManager 与 online 状态监听：refetchOnWindowFocus 的内部设计

**答**：
- focusManager 是单例：监听 `visibilitychange`（document 可见性）+ `focus` 事件（窗口聚焦），暴露 `isFocused`。每个 Query 的 retryer/observer 通过 `focusManager.subscribe` 挂钩——切回 tab 时对 stale query 批量 refetch（refetchOnWindowFocus）。
- 设计细节：1) **一次聚焦只触发一轮**——聚焦瞬间多个 query 都要拉，TanStack 用「聚焦事件 → cache 里逐个判断 shouldFetchOnFocus」的批处理，且同一 query 的重复触发被在途 fetch 去重；2) SSR 环境 focusManager 检测 `typeof window` 自动空转；3) 测试环境 `focusManager.setFocused(true/false)` 手动控制，mock 无需真实切 tab。
- onlineManager 同构：监听 `online/offline` 事件，`isOnline` 供 retryer 的 networkMode 判断——离线时 fetch pause，online 事件触发 pause 中的 retryer 继续。
- 扩展性：两者都支持 `setEventListener(fn)` 替换默认监听（RN/小程序环境接自己的生命周期，App 前后台切换对应 visibilitychange）。
- 追问钩子：refetchOnWindowFocus 造成的「每次切回都请求」困扰，解法是把 staleTime 设为合理值——focus refetch 只对 stale query 生效，fresh 的不动。

```javascript
// focusManager / onlineManager 骨架
class FocusManager {
  #focused
  #listeners = new Set()
  setup(onFocus) {
    if (typeof window === 'undefined') return   // SSR 空转
    onFocus((focused) => { this.#focused = focused; this.#listeners.forEach((l) => l(focused)) })
  }
  isFocused() { return this.#focused ?? (typeof document === 'undefined' ? true : document.visibilityState !== 'hidden') }
  subscribe(listener) { this.#listeners.add(listener); return () => this.#listeners.delete(listener) }
  setFocused(focused) { this.#focused = focused }   // 测试手动注入
}
const focusManager = new FocusManager()
focusManager.setup((onFocus) => {
  document.addEventListener('visibilitychange', () => onFocus(document.visibilityState !== 'hidden'))
  window.addEventListener('focus', () => onFocus(true))
})

// 挂载时的 focus refetch 判定（简化）
cache.subscribe((event) => {
  if (event.type === 'focus') {
    cache.getAll().forEach((query) => {
      if (query.isStaleByTime() && query.options.refetchOnWindowFocus) {
        query.fetch()   // 在途请求自动去重（fetch 复用同一 promise）
      }
    })
  }
})

// RN/小程序适配：替换事件源
focusManager.setEventListener((onFocus) => {
  AppState.addEventListener('change', (state) => onFocus(state === 'active'))
})
```
