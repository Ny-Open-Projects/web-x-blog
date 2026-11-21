---
title: [MFW-004] Server Component 里不能做哪些事？为什么？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-004：Server Component 里不能做哪些事？为什么？
**答**：
- 不能用任何产生**状态与副作用于浏览器**的能力：useState/useReducer/useEffect/useLayoutEffect/useRef（服务端没有交互、没有重渲染、没有 DOM）。
- 不能绑定事件处理器（onClick/onChange）与浏览器 API（window/document/localStorage）——组件根本不会在浏览器执行。
- 不能把**不可序列化的 props** 往下传给 Client Component：函数、class 实例、Symbol、Date 需要先转成字符串/数字（序列化走 Flight 协议）。
- 不能使用 Context Provider 直接包裹后让客户端读（Provider 本身若是 Server 组件，value 传不下去）——Provider 要标 `'use client'`。
- 反过来记：Server Component **擅长**的是数据获取、密钥操作、访问后端资源、减少客户端体积。

```jsx
// ❌ 典型错误：在 Server Component 里用 hooks 和事件
export default async function Cart() {
  const items = await getCart();
  const [count, setCount] = useState(0);   // 编译报错
  return <button onClick={() => setCount(count + 1)}>加购</button>; // 报错
}

// ✅ 拆分：数据留服务端，交互下放客户端
export default async function Cart() {
  const items = await getCart();
  return <CartList initialItems={items} />; // 传纯数据
}

// app/cart-list.tsx
'use client';
export function CartList({ initialItems }) {
  const [items, setItems] = useState(initialItems);
  return (
    <ul>
      {items.map((i) => (
        <li key={i.id} onClick={() => setItems(items.filter((x) => x.id !== i.id))}>
          {i.title}
        </li>
      ))}
    </ul>
  );
}
```
