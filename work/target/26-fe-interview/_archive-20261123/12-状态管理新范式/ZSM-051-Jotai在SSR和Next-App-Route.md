---
title: [ZSM-051] Jotai 在 Next.js App Router 里怎么安全使用？useHydrateAtoms 时机有什么讲究？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-051：Jotai 在 Next.js App Router 里怎么安全使用？useHydrateAtoms 时机有什么讲究？
**答**：
- RSC 内不能写状态，只把可序列化数据传到客户端边界；所有 atom 创建与消费在 'use client' 模块。
- SSR 每请求一个 store（Provider store），用 useHydrateAtoms 在**首次渲染前**注入初值，保证服务端 HTML 与客户端首渲染一致（防 hydration mismatch）。
- hydrate 只在挂载时生效一次，之后再改传入值不会更新 atom（设计如此）；需要二次落地用 effect setState。
- 布局级 Provider + 页面级 hydrate：把 store 放 layout，hydrate 放页面，避免路由切换重置全局 atom。

```javascript
// layout.tsx (client boundary)
'use client'
export const StoreProvider = ({ children }) => <Provider>{children}</Provider>

// page.tsx 的客户端组件
'use client'
function Greeting({ name }) {
  useHydrateAtoms([[nameAtom, name]]) // 渲染期同步注入，首帧一致
  return <h1>{useAtomValue(nameAtom)}</h1>
}
// RSC: <Greeting name={await getName()} /> → 序列化传参
```
