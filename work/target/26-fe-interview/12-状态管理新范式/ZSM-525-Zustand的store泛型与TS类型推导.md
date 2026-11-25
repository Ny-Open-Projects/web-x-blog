---
title: [ZSM-525] Zustand 的 TypeScript 类型推导链路是怎么实现的
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-525：Zustand 的 TypeScript 类型推导链路是怎么实现的

**答**：
- 核心是 `create<T>()(...)` 的**柯西化（curried）签名**：直接 `create((set) => ...)` 在中间件存在时类型推断会退化（TS 无法从中间件参数反推 T），先 `create<T>()` 显式标注，再传 initializer，让 T 先固定。
- initializer 返回对象的类型被 `Mutate<StoreApi<T>, Mps>`（中间件元组映射类型）折叠：每个中间件对应一个 `mp`（mutator）类型标记，`zustand/middleware` 里 devtools/persist/immer 各自定义 `<T, Mps extends [Mutators]>` 的重载，把 T 逐层变形。
- `useStore` 返回值来自 `T extends object` 的 `ExtractState`：`T extends { getState: () => infer S } ? S : never`，即从 StoreApi 上抽出 state 类型；selector 返回类型是 `S` 上再算 `ReturnType<selector>`。
- 中间件顺序影响类型（devtools 在外层时 mutate 类型多一层包装），所以 TS 报错常提示「中间件排列不对」，这与运行时推荐顺序（devtools → subscribeWithSelector → persist → immer）一致。
- 追问钩子：常见类型坑——`set` 的 updater 返回 `Partial<T>`，但 immer 中间件里 draft 是 `T` 非 `Partial`；还有 persist 的 `partialize` 返回子集需要 `PersistOptions<T, PartialT>` 双泛型。

```typescript
import { create } from 'zustand'
import { devtools, persist } from 'zustand/middleware'

interface CartState {
  items: { id: string; qty: number }[]
  add: (id: string) => void
}

// 柯西化：先固定 T 再接中间件链
export const useCart = create<CartState>()(
  devtools(
    persist(
      (set) => ({
        items: [],
        add: (id) => set((s) => ({ items: [...s.items, { id, qty: 1 }] })),
      }),
      { name: 'cart', partialize: (s) => ({ items: s.items }) }  // PersistOptions<CartState, Pick<...>>
    )
  )
)

// ExtractState 原理（简化源码类型）
type ExtractState<S> = S extends { getState: () => infer T } ? T : never
type CartStateExtracted = ExtractState<typeof useCart>   // CartState
```
