---
title: [TS-137] React.FC 有哪些争议？推荐哪种组件 Props 写法？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-137：React.FC 有哪些争议？推荐哪种组件 Props 写法？
**答**：
- 争议一：FC 历史上隐式塞入 children（18.2 前的 PropsWithChildren），不需要 children 的组件也能传。
- 争议二：泛型组件挂在 FC 上受限，返回类型被锁死、displayName 等附加属性徒增噪音。
- 推荐：普通函数 + 显式 Props 接口，children 按需显式声明，类型意图一目了然。

```tsx
// 反对 React.FC 的三个理由：
// 1. 隐式 children（@types/react 18.2 前永远可传），语义失真
// 2. 泛型组件 <T> 无法直接通过 FC 声明
// 3. 返回类型与附加静态属性锁死签名

// 推荐：普通函数 + 显式 Props
interface ButtonProps {
  label: string;
  onClick: () => void;
  children?: React.ReactNode; // 需要才声明
}
function Button({ label, onClick, children }: ButtonProps) {
  return <button onClick={onClick}>{label}{children}</button>;
}
```
