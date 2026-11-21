---
title: [ZSM-108] SWR 怎么和 Zustand 配合做状态分层？哪些数据该放 SWR，哪些放 store？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-108：SWR 怎么和 Zustand 配合做状态分层？哪些数据该放 SWR，哪些放 store？
**答**：
- 分层原则：服务端数据的「本体」只存 SWR 缓存，Zustand 存客户端状态（筛选条件、选中项、UI 开关），用 selector 桥接，绝不把接口数据再复制进 store——两份副本必然失同步。
- 桥接方式：组件里 `useSWR(key)` 取数 + `useStore(s => s.filters)` 取条件；全局动作（如退出登录清缓存）用全局 mutate 按 key 前缀批量失效。
- SWR 缓存本身不响应式暴露在组件外，组件外要用数据就走请求层函数或订阅 store 里的「派生冗余」小字段。
- 追问钩子：被问到「为什么不全放 Zustand」时答——SWR 提供去重/重验证/失效语义，手写进 store 等于重新实现一遍缓存层且容易漏。

```javascript
import useSWR from 'swr'
import { create } from 'zustand'
import { mutate } from 'swr'

// 客户端状态：筛选与选中
const useGoodsStore = create((set) => ({
  filter: 'all',
  selectedId: null,
  setFilter: (filter) => set({ filter }),
  select: (selectedId) => set({ selectedId }),
}))

function GoodsList() {
  const filter = useGoodsStore(s => s.filter)          // 条件来自 store
  const { data } = useSWR(`/api/goods?filter=${filter}`, fetcher) // 数据来自 SWR
  return <List items={data ?? []}/>
}

export async function onLogout() {
  await api.logout()
  // 服务端缓存整体失效（匹配前缀），客户端 store 由各组件自行 reset
  await mutate(key => Array.isArray(key) || typeof key === 'string' ?
    String(key).startsWith('/api/user') || key[0] === '/api/user' : false,
    undefined, { revalidate: true })
}
```
