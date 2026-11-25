---
title: [ZSM-718] 热更新（HMR）与状态保持：模块替换时哪些状态该留、哪些该清
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-718：热更新（HMR）与状态保持：模块替换时哪些状态该留、哪些该清

**答**：
- HMR 丢状态的三个来源：1) **模块重新执行**——store 文件被替换，模块级单例重建（state 归零）；2) **组件树 remount**——accept 边界不对导致整树重载；3) **闭包过期**——保留的 store 与新代码的 reducer 不兼容（字段变了）。HMR 状态策略就是逐个解决。
- 保留策略分级：1) **UI 态丢弃**（弹窗/草稿——HMR 本来就是开发场景，丢了无害）；2) **开发会话态保留**（登录 token、路由位置、调试面板开关——重复登录烦死人）；3) **迁移保留**（store 字段结构变了，旧 state 走 migrate）。实现：`import.meta.hot.dispose` 时快照、新模块 init 时 `setState(migrate(snapshot))`。
- zustand HMR 陷阱：store 文件热更后「旧引用」还活着（组件持有的 selector 闭包指向旧 store）——订阅不更新、setState 不生效。解法：store 模块 self-accept + 全局挂载（`if (import.meta.hot) { window.__zustand_stores[xxx] = store }`）或把 store 创建与定义分离（定义热更、实例常驻）。
- Vite 的正确姿势：`import.meta.hot.accept((newModule) => ...)` 里把旧 state 塞进新 store；devtools 探针要 re-attach（旧探针随旧 store 一起死了）。
- 追问钩子：HMR 状态策略与测试隔离策略（ZSM-706）是同一问题的两面——「模块级单例的重建语义」在两个场景下都需要显式处理，架构上就写成 `resetStore()`/`restoreStore()` 统一 API。

```javascript
// zustand store 的 HMR 状态保持
// cart.ts
import { create } from 'zustand'

export const useCart = create((set) => ({ items: [], total: 0 }))

// HMR：dispose 时快照，重建时恢复 + migrate
if (import.meta.hot) {
  let saved = null
  import.meta.hot.dispose(() => {
    saved = useCart.getState()          // 模块替换前快照
  })
  import.meta.hot.accept((newModule) => {
    if (!saved) return
    // 字段迁移：新模块可能改了结构
    const migrated = migrateStoreState(saved, newModule.useCart.getInitialState())
    newModule.useCart.setState(migrated)   // 恢复到新实例
  })
}

function migrateStoreState(saved, initial) {
  const next = { ...initial }
  for (const k of Object.keys(initial)) {
    if (saved[k] !== undefined) next[k] = saved[k]     // 交集保留
  }
  return next
}

// Vite 插件层：统一处理所有 store（避免每个文件写样板）
// vite.config.ts: 插件在 transform 时自动注入 accept/dispose 代码
// 探针重挂载：devtools 收 store 变更事件（新模块 init 时重新 attachTracer）
```
