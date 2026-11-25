---
title: [916] TanStack Query 的类型安全在大型应用怎么建
date: 2026-11-17
categories: [状态管理新范式]
tags: [前端面试, 面试题, TanStack Query, 类型]
type: 面试题
---

## 916：TanStack Query 的类型安全在大型应用怎么建

**答**：
- 类型三层：queryFn 返回类型自动推导（data 类型跟 queryFn 走——不写死在 useQuery 泛型，避免手动泛型与实际不符）、Key 与 fn 绑定（keyFactory 返回 as const 元组）、错误类型统一（queryFn 抛结构化错误类，error 收窄）。
- 声明合并注册：declare module 的 Register 机制（v5）——Key 空间注册后拼错编译期报错，大型应用 Key 拼装错误的根治手段。
- select 的类型链：select 返回派生类型自动推导；注意 select 引用稳定性（内联箭头每次新引用导致缓存对象重建——用 useCallback 或模块级函数）。
- 追问钩子：为什么 data 可能是 undefined？——缓存可能无数据（未加载/被 gc），类型上 T | undefined 是诚实的；禁用 data! 断言是类型安全红线。

```ts
declare module '@tanstack/react-query' {
  interface Register { queryKey: MyKeyRegistry }   // v5 Key 注册
}
const useUser = (id: string) =>
  useQuery({ queryKey: userKeys.detail(id),
    queryFn: () => fetchUser(id) });   // data 自动推导为 User
```

