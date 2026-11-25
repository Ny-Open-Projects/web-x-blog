---
title: [MFW-682] React.memo 在 RSC 的语义
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-682：React.memo 在 RSC

**答**:
- memo 在 RSC 的语义：1) **server 组件不能用 memo**（server 组件每次请求重渲染——「缓存」由 Data Cache/Full Route Cache 承担（RBL-508）——memo 是 client 交互态的优化）；2) **client 组件的 memo**（props 不变跳过 re-render——与 RSC 的交互：RSC re-render → client props 变化 → memo 比较 props（引用比较——新对象 props = memo 失效））；3) memo 的 props 比较（浅比较——RSC 传下来的 props 引用稳定性（server 渲染的 props 每次新对象 → memo 失效——除非 props 稳定引用）。
- RSC 传 props 的引用稳定性：Flight 反序列化每次生成新对象（引用不稳定）→ client memo 的 props 比较失效（每次 RSC patch = client 全 re-render）；「引用稳定」的优化：client 组件内部比较（zustand selector/useMemo——props 解构后的字段比较 RBL-547）。
- 追问钩子：为什么「RSC patch 会让 client memo 失效」且怎么解？——Flight 反序列化 = 每次新对象引用（JSON parse 语义 RBL-503）；memo 的浅比较（引用不等 → re-render——即使值相同）；解法：client 组件「内部 selector」（zustand/useMemo 按 value 比较——不做 props 层的引用比较）；或「React 的 memo 自定义比较函数」（propsAreEqual——值比较开销 vs re-render 成本的权衡）；RSC 架构下 memo 的角色变化：从「跳过 re-render」变为「需要值比较辅助」。

```tsx
// RSC 传 props 给 client memo
// server: <ProductCard product={{ ... }} />  ← 每次渲染新对象
'use client';
// 反模式：直接 memo（RSC patch 总是 re-render）
const Card = memo(function Card({ product }) { ... });   // 浅比较：新引用 → 失效
// 修正：自定义比较（值比较）
const Card = memo(function Card({ product }) { ... },
  (prev, next) => prev.product.id === next.product.id &&
    prev.product.price === next.product.price);          // 值级比较
// 或：client 内部 store selector（RBL-547）
'use client';
function Card({ productId }) {
  const product = useProductStore(s => s.products[productId]);   // selector：值稳定
  return <span>{product.price}</span>;
}
```
