---
title: [TS-139] children 的类型该用 ReactNode 还是 ReactElement？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-139：children 的类型该用 ReactNode 还是 ReactElement？
**答**：
- ReactNode：一切可渲染物（element、string、number、boolean、null、数组），容器组件默认用它。
- ReactElement：单个元素对象，有 type/props，能 cloneElement 注入 props、能 Children.only 校验。
- render props 场景用函数签名 `(args) => ReactElement`，三者不可混用。

```tsx
// 三种 children 类型对应三种组件形态
type Wrapper1 = { children: React.ReactNode };                     // 常规容器
type Wrapper2 = { children: React.ReactElement };                  // 需要注入/克隆 children
type Wrapper3 = { children: (count: number) => React.ReactElement }; // render props

function InjectProps({ children }: Wrapper2) {
  // React.Children.only(children) 保证确实是单个 element
  return React.cloneElement(children, { size: "lg" } as Partial<React.HTMLAttributes<HTMLElement>>);
  // 若声明为 ReactNode，cloneElement 直接报错：Node 上没有 type/props
}

function Counter({ children }: Wrapper3) {
  return children(42); // 调用子级拿到 UI
}
```
