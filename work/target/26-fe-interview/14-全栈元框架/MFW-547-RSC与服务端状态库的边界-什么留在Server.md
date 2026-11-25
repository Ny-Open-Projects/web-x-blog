---
title: [MFW-547] RSC 与服务端状态库：什么留在 Server、什么下沉 Client
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-547：RSC 与 Client 状态库的边界划分

**答**:
- RSC 架构下状态的去处：1) **服务端数据**（DB 数据——RSC 直接读、不进 client 状态库——props 下发；「不再需要 Redux 存 server 数据」——client store 只管客户端态）；2) **客户端状态**（UI 态/表单暂存/乐观更新——zustand/jotain）；3) **边界混合**（购物车：server 是 DB 真源 + client 乐观副本 useOptimistic——「乐观副本与真源同步」revalidateTag）。
- 反模式：把 RSC 数据灌进 client store（fetch 后 setState——失去 RSC 的流式/缓存优势：数据回流 client = 序列化成本 + Router Cache 失效）；「server 数据留 server」原则。
- 保留 client store 的场景：跨组件高频交互态（拖拽排序的中间态/复杂表单联动）；第三方组件的状态（地图/编辑器实例）。
- 追问钩子：为什么「RSC 后 Redux 大部分消失」但 store 生态没有死？——Redux 时代 store 承担两类职责：「server 数据的 client 镜像」（RTK Query/缓存）与「客户端交互态」；RSC 把第一类收归 server（Data Cache/Router Cache 是新的数据层）；剩下「纯客户端态」用轻量库（zustand 3KB）——store 生态的「减重」不是「死亡」：架构职责的重新划分让每层工具回归本位（RBL-854 平台职责三分的组件版）。

```javascript
// 状态的归属分层
// 1) server 数据：RSC 直读（不进 client store）
// app/page.tsx
export default async function Page() {
  const products = await getProducts();                  // server 侧数据流
  return <ProductList products={products} />;
}
// 2) client 交互态：轻量 store
// components/editor.tsx ('use client')
const useEditor = create((set) => ({ nodes: [], add: (n) => set(s => ({ nodes: [...s.nodes, n] })) }));
// 3) 乐观副本：useOptimistic（真源在 server）
function AddToCart({ productId }) {
  const [optimisticItems, add] = useOptimistic(cartItems,
    (cur, item) => [...cur, item]);                      // 乐观副本
  return <form action={async () => {
    add({ productId });                                  // 立即 UI 反馈
    await serverAddToCart(productId);                    // 真源写入 + revalidate
  }}>...</form>;
}
// 反模式：RSC 数据灌 client store（丢失流式/缓存优势）
```
