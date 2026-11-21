---
title: [ZSM-250] 自建跨框架 vanilla store 适配层的设计原则
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-250：自建跨框架 vanilla store 适配层的设计原则

**答**：
- 接口最小化：get/set/subscribe 三件套足够；多余 API（中间件、devtools）按需加，接口越小桥接层越薄
- 订阅契约对齐 useSyncExternalStore：subscribe 返回退订函数、getSnapshot 引用稳定（变更时才换引用），这决定了 React 侧的正确性
- 每框架一个 20 行左右的 hook/组合式函数薄层，业务代码禁止直接 import store 核心之外的东西
- 测试策略：核心 store 用纯 JS 单测（零框架），适配层用对应框架的 renderHook 冒烟——分层让测试金字塔成立

```javascript
// 核心（~30 行，零依赖）
export function createStore(init) {
  let s = init; const subs = new Set()
  return {
    get: () => s,
    set: (patch) => { s = typeof patch === 'function' ? patch(s) : { ...s, ...patch }; subs.forEach((f) => f(s)) },
    subscribe: (f) => (subs.add(f), () => subs.delete(f)),
  }
}
// React 薄层
export const useApp = () => useSyncExternalStore(app.subscribe, app.get)
```
