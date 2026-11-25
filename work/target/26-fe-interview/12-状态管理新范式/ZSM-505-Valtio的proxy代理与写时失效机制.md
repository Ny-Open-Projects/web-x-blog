---
title: [ZSM-505] Valtio 的 proxy 代理是如何实现「改哪更新哪」的
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-505：Valtio 的 proxy 代理是如何实现「改哪更新哪」的

**答**：
- `proxy()` 用 `Proxy` 包住对象，get 时把访问路径注册进「使用中的版本快照」，set 时标记该节点及其祖先为 dirty 并调度版本号递增。
- 每次代理对象 set/ delete 后通过 `touch` 沿 `parents` 向上冒泡更新版本，组件订阅的是自己读过的具体属性路径（通过 `proxyStateVersion` 与快照 diff 比对），所以只改 `state.a.b` 时只读了 `a.b` 的组件重渲。
- 读组件拿到的是 `snapshot()`——基于 immutable 缓存的代理副本：`getSnapshot` 会把代理逐层转成普通对象（未修改的层直接复用缓存），保证 `useSnapshot` 的引用稳定。
- 异步批处理：一次事件循环里多次 set 合并为一次通知（`notifySync` / `notify`，微任务或同步调度可选），避免连续赋值触发多次渲染。
- 追问钩子：Proxy 局限——Map/Set 需要 polyfill 代理、循环引用会被 `snapshot` 特殊处理、跨 iframe 的对象不可代理。

```javascript
// 极简 proxy 状态核心（Valtio 思路）
const versionMap = new WeakMap() // proxy -> version
const listeners = new Map()      // proxy -> Set<fn>

function proxy(obj, path = '') {
  return new Proxy(obj, {
    get(t, k) {
      const v = t[k]
      return (typeof v === 'object' && v !== null) ? proxy(v, path + k + '.') : v
    },
    set(t, k, val) {
      t[k] = val
      bump(t)                    // 子节点版本 +1
      parents.get(t)?.forEach(bump) // 冒泡祖先（真实实现里记录 parents）
      notify(t)
      return true
    },
  })
}

function bump(t) { versionMap.set(t, (versionMap.get(t) ?? 0) + 1) }
function notify(t) {
  listeners.get(t)?.forEach((fn) => fn())
  queueMicrotask(() => { /* 合并批处理：一帧只 flush 一次 */ })
}
```
