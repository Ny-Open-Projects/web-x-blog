---
title: [ZSM-014] Next.js App Router 里 Zustand 怎么把服务端初始数据带进 store？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-014：Next.js App Router 里 Zustand 怎么把服务端初始数据带进 store？
**答**：
- RSC 里 fetch 数据 → 序列化传给客户端边界组件 → 客户端在模块缓存里按请求创建 store（SSR 期间请求级缓存，CSR 期间页面级缓存）。
- 缓存策略：用全局 Map 按「请求标识 + store 名」缓存实例，避免 RSC 树重渲染时重复建 store；客户端刷新路由时可保留或重置。
- 数据流分层：初始「服务端状态」建议交给 TanStack Query 的 hydrate，store 只放交互态；两者混放会变成双源。
- 不要把函数/类实例塞进 RSC → 客户端的 props，只能传可序列化数据。

```javascript
// RSC
export default async function Page() {
  const data = await getUser()
  return <StoreInitializer init={{ user: data }} />
}
// 客户端边界：一次性写入
'use client'
function StoreInitializer({ init }) {
  useEffect(() => { useAppStore.setState(init) }, [])
  return null
}
```
