---
title: [ZSM-252] qiankun 的 initGlobalState 通信机制是怎么实现的
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-252：qiankun 的 initGlobalState 通信机制是怎么实现的

**答**:
- initGlobalState(state) 返回 onGlobalStateChange（订阅）与 setGlobalState（写入），本质是一个全局发布订阅器 + state 缓存
- setGlobalState 默认浅合并（onGlobalStateChange 回调收到全量 state）；子应用通过 props 拿到这两个函数，依赖反转到主应用
- 微前端生命周期挂载时注册监听、卸载时清理（clearDataState/undefined 处理是常见泄漏点——子应用监听必须随 unmount 解除）
- 局限：无选择器粒度（整树通知）、无中间件、无持久化——复杂共享状态建议换成 vanilla store 下发，initGlobalState 只留作兜底

```javascript
// 主应用
const { onGlobalStateChange, setGlobalState } = initGlobalState({ user: null, theme: 'dark' })
onGlobalStateChange((s) => console.log('global →', s))

// 子应用 mount 生命周期
export async function mount(props) {
  props.onGlobalStateChange((s) => applyShared(s))
  props.setGlobalState({ theme: 'light' })
}
export async function unmount() { /* 必须解除监听 */ }
```
