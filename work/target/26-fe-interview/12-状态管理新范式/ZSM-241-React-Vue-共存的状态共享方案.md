---
title: [ZSM-241] React 和 Vue 共存的项目状态怎么共享
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-241：React 和 Vue 共存的项目状态怎么共享

**答**：
- 核心思路：状态核心做成框架无关（vanilla JS + 订阅模式），各框架写薄适配层订阅——React 用 useSyncExternalStore，Vue 用 ref/watch 桥接
- 现成方案：Zustand vanilla store、Valtio proxy、RxJS、或自写 mini store；不要在 React Context 里塞给 Vue 用（依赖注入体系不通）
- 桥接层职责单一：订阅 + 转引用 + 转写调用，禁止业务逻辑进桥，否则两边心智分裂
- 边界：SSR 需要每请求独立 store 实例传给两个框架的渲染入口；序列化传参（props）仍是首选，全局桥只放「真全局」状态

```javascript
// framework-agnostic store
function createStore(init) {
  let state = init; const subs = new Set()
  return {
    get: () => state,
    set: (p) => { state = { ...state, ...p }; subs.forEach((f) => f(state)) },
    sub: (f) => (subs.add(f), () => subs.delete(f)),
  }
}
export const appStore = createStore({ theme: 'dark' })
```
