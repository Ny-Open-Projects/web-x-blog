---
title: [ZSM-165] RSC/Server Actions 时代，客户端状态管理的版图缩小到了什么？还剩哪些是客户端库的活？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-165：RSC/Server Actions 时代，客户端状态管理的版图缩小到了什么？还剩哪些是客户端库的活？
**答**：
- 被收走的：纯展示页的数据获取与缓存（RSC 直出、`use cache` 承担缓存），这类页面不再需要客户端缓存库。
- 还剩的：交互期缓存（轮询/焦点重取/乐观更新）、跨组件客户端共享（主题/会话/UI 态）、复杂派生（atom 森林）、瞬态高频状态（ref/transient）——即「服务端直出覆盖不到的客户端动态部分」。
- 版图变化的表达：过去 Redux 一个人管所有，现在服务端状态归 RSC + Query/SWR（客户端交互部分），客户端状态归 Zustand/Jotai，Jotai 的「原子派生」价值反而更突出。
- 面试表达：别下结论「状态管理库要死了」，给出「服务端状态在服务端解决，客户端状态管理更聚焦」的动态视角。

```javascript
// RSC 直出：这部分不再需要客户端缓存
// app/products/page.tsx (server)
export default async function Page() {
  const products = await getProducts()            // 服务端取数 + use cache
  return <ProductGrid products={products}/>       // 静态部分直出
}

// 客户端交互岛：仍是客户端库的主场
'use client'
function CartActions({ productId }) {
  const addCart = useCartStore(s => s.add)        // 客户端领域状态：Zustand
  const [pending, start] = useTransition()

  function buy() {
    start(async () => {
      await serverAction.buy(productId)           // Server Action：跨端调用
      await queryClient.invalidateQueries({ queryKey: ['cart'] })
    })
  }
  return <button onClick={buy} disabled={pending}>立即购买</button>
}
```
