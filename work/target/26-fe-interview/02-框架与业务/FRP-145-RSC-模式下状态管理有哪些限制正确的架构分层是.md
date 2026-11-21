---
title: [FRP-145] RSC 模式下状态管理有哪些限制？正确的架构分层是什么？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-145：RSC 模式下状态管理有哪些限制？正确的架构分层是什么？

**答**：
- server 组件没有实例：**不能**用 useState/useEffect/useRef/Context/浏览器 API——每次请求都是一次性的 render，没有"组件生命周期"可言。
- 服务端到客户端只能传**可序列化** props（不能传函数实例；Server Action 引用是特例）；客户端到服务端只能通过 action 参数回传。
- 全局状态的归属：服务端状态放 db/服务端缓存（用 revalidate 控制）；客户端交互状态收敛到 client island 内部或客户端 store。
- 分层模式：server 组件做"数据获取 + 布局 + 静态渲染"，client island 做"交互与本地状态"，跨 island 共享用 URL 参数/客户端 store/Server Action。

```javascript
// 简化实现，帮助理解 RSC 的状态边界
// —— 错误示范：server 组件里用状态 ——
// async function Counter() {
//   const [n, setN] = useState(0);   // 编译/运行时报错：server 组件没有实例
//   return <button onClick={() => setN(n + 1)}>{n}</button>;  // onClick 也无法序列化
// }

// —— 正确分层：server 壳 + client island ——
async function ProductPage({ id }) {              // server：取数、布局
  const product = await db.product.find(id);
  const reviews  = await db.review.list(id);
  return (
    <>
      <h1>{product.name}</h1>                     {/* 静态部分零 JS */}
      <AddToCart product={product} />             {/* client island：交互状态 */}
      <ReviewList reviews={reviews} />            {/* server：静态渲染 */}
    </>
  );
}

function AddToCart({ product }) {                 // 'use client'
  const [qty, setQty] = useState(1);              // 本地状态只在 island 内
  return (
    <>
      <input value={qty} onChange={e => setQty(+e.target.value)} />
      <button onClick={() => addToCart(product.id, qty)}>加入购物车</button>
    </>
  );
}

// 跨 island 共享：Server Action + revalidate 作为"全局同步通道"
async function addToCart(id, qty) {
  'use server';
  await cart.add(id, qty);
  revalidateTag('cart-count');                    // 所有显示购物车数的 island 更新
}
// 心智模型：服务端是"唯一的真相源"，客户端 state 只是 island 内的临时 UI 状态
```
