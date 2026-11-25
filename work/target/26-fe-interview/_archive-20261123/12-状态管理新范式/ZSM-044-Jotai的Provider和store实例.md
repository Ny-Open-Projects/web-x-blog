---
title: [ZSM-044] Jotai 的 Provider 与自定义 store 有什么用？不包 Provider 会怎样？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-044：Jotai 的 Provider 与自定义 store 有什么用？不包 Provider 会怎样？
**答**：
- 不包 Provider 也能用：atom 值挂在模块级默认 store 上（全局单例）。
- 包 `<Provider>` 后，子树内用一份独立 store：测试隔离（每个用例新 store）、SSR 每请求新 store、微前端/多页面各自域，都靠它。
- `createStore()` + `useHydrateAtoms` 可给 store 预填初值（SSR 落地数据）；`getDefaultStore()` 可在组件外读写全局 store。
- atom 是「定义」，store 是「值容器」：同一 atom 定义在不同 store 里互不相干，这是理解测试隔离的关键。

```javascript
import { Provider, createStore, useHydrateAtoms } from 'jotai'

const store = createStore() // 组件外也可 store.get/countAtom 读写

function App({ initialUser }) {
  return (
    <Provider store={store}>
      <Hydrate initialUser={initialUser} />
    </Provider>
  )
}
function Hydrate({ initialUser }) {
  useHydrateAtoms([[userAtom, initialUser]], store) // SSR 数据落地
  return <Profile />
}
```
