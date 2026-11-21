---
title: [ZSM-113] SWR 在 Next.js SSR/RSC 场景下怎么用？fallback 注入和双取数问题怎么解？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-113：SWR 在 Next.js SSR/RSC 场景下怎么用？fallback 注入和双取数问题怎么解？
**答**：
- App Router 下优先用 RSC 直接取数传 props；只有需要客户端交互（轮询、重验证、乐观更新）的组件才下沉成 client component 配 SWR。
- fallback 注入：server component 取好数据后传给 `<SWRConfig value={{ fallback }}>` 包裹的 client 部分，key 必须与客户端 useSWR 的 key 完全一致，否则会双取。
- 双取数问题：同一数据 RSC 取一次 + SWR 又取一次。解法是「RSC 取 → fallback 灌 → 客户端组件只读缓存」，SWR 看到缓存有值且 dedupingInterval 内就不发请求。
- 每请求隔离：App Router 每次请求的 fallback 不能串味，SWR v2 的 provider 是按 SWRConfig 实例创建的，配合 `new Map()` 初始缓存即可实现请求级隔离。

```javascript
// app/goods/page.js —— Server Component
import { GoodsClient } from './goods-client'

export default async function Page() {
  const list = await getGoods()          // RSC 取数（走 Node 直连服务）
  return <GoodsClient fallback={{ '/api/goods': list }} initial={list}/>
}

// goods-client.js —— Client Component
'use client'
import { SWRConfig, useSWRConfig } from 'swr'

export function GoodsClient({ fallback, initial }) {
  return (
    <SWRConfig value={{ fallback }}>
      <GoodsList/>
    </SWRConfig>
  )
}

function GoodsList() {
  // 缓存已被 fallback 灌满，首屏不发请求；焦点/失效时才 revalidate '/api/goods'
  const { data, mutate } = useSWR('/api/goods')
  return <List items={data} onRefresh={() => mutate()}/>
}
```
