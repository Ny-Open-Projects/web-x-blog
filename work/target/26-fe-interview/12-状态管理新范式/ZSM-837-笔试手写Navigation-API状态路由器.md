---
title: [ZSM-837] 笔试：手写 Navigation API 状态路由器（entry.state + 降级 history）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-837：手写 Navigation API 状态路由器（entry.state + 降级 history）
**答**：实现 `createNavRouter()`：1) `navigate(path, state)`：优先 Navigation API（`navigation.navigate(path, { state })`），不可用降级 `history.pushState(state, '', path)`；2) `back()`：返回后恢复 `entry.state`（Navigation API）或 popstate 事件的 event.state（降级）——导航态（滚动/草稿）原生恢复；3) `onNavigate(fn)` 统一回调（两通道都走）；4) `current()`：`{ path, state }`；5) 附用例：push→back 的 state 恢复与降级通道一致。

```javascript
function createNavRouter() {
  const hasNavApi = typeof navigation !== 'undefined'
  const listeners = new Set()

  function navigate(path, state = {}) {
    if (hasNavApi) {
      navigation.navigate(path, { state })            // 原生：entry 携带 state
    } else {
      history.pushState(state, '', path)              // 降级：pushState
      emit({ path, state })
    }
  }

  function back() {
    hasNavApi ? navigation.back() : history.back()
    // 恢复由 currentEntry.state（原生）或 popstate（降级）驱动
  }

  function current() {
    if (hasNavApi) {
      return { path: navigation.currentEntry.url, state: navigation.currentEntry.getState() }
    }
    return { path: location.pathname, state: history.state }
  }

  function emit(entry) { listeners.forEach((fn) => fn(entry)) }

  // 降级通道：popstate
  if (!hasNavApi) {
    window.addEventListener('popstate', (e) => {
      emit({ path: location.pathname, state: e.state })
    })
  } else {
    navigation.addEventListener('currententrychange', (e) => {
      emit({ path: navigation.currentEntry.url, state: navigation.currentEntry.getState() })
    })
  }

  return { navigate, back, current, onNavigate: (fn) => (listeners.add(fn), () => listeners.delete(fn)) }
}

// 用例（模拟降级通道，jsdom 环境）
let navEntry = { url: '/', state: null }
const navigationMock = {
  _listeners: {},
  addEventListener(type, fn) { this._listeners[type] = fn },
  get currentEntry() { return { url: navEntry.url, getState: () => navEntry.state } },
  navigate(path, { state }) { navEntry = { url: path, state }; this._listeners['currententrychange']?.() },
  back() { /* 历史栈略 */ },
}
// 演示用：直接测降级分支语义一致
const router = createNavRouter()
router.onNavigate((e) => console.log('nav', e.path, e.state))
router.navigate('/detail', { selectedId: '7', scrollY: 500 })
console.log(router.current())
// { path: '/detail', state: { selectedId: '7', scrollY: 500 } }
// 后退恢复：entry.state 原生带回 selectedId/scrollY —— 草稿/滚动不丢（772 语义原生版）
```
**评分点**：
- 双通道封装（Navigation API 优先 / pushState+popstate 降级）
- entry.state 的导航态恢复（滚动/草稿原生保留）
- onNavigate 统一回调（两通道同构消费）
- current() 的通道无关读取
