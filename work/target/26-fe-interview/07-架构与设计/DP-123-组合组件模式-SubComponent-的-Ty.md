---
title: [DP-123] 组合组件模式（SubComponent）的 TypeScript 类型如何定义？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-123：组合组件模式（SubComponent）的 TypeScript 类型如何定义？（高频）
**答**：
- 组合组件 = 父组件 + 挂在其身上的子组件（`Card.Header`），类型上需要：子组件类型定义、父组件类型用 `&` 挂载子组件、共享 context 的泛型约束。
- 两个关键类型技巧：`Partial<Record<K, FC<any>>>` 挂载集合；用 `InferProps`/泛型让父组件把泛型参数（如 value 类型）传给子组件。
- 收益：`<Card.Header />` 有完整提示与校验，约束"子组件必须用在父组件内"可结合 context 判空实现。

```tsx
import { createContext, useContext, type FC, type ReactNode } from 'react';
// 子组件 props 类型
interface CardHeaderProps { title: ReactNode; extra?: ReactNode; }
interface CardBodyProps { children: ReactNode; }
// 父组件 props：泛型约束数据形状
interface CardProps<T> { data: T; children: ReactNode; }
const CardCtx = createContext<{ data: unknown } | null>(null);
function CardHeader({ title, extra }: CardHeaderProps) { return <header>{title}{extra}</header>; }
function CardBody({ children }: CardBodyProps) {
  const ctx = useContext(CardCtx);
  if (!ctx) throw new Error('Card.Body 必须用在 Card 内');      // 结构约束运行时兜底
  return <div>{typeof children === 'function' ? children(ctx.data) : children}</div>;
}
// 父组件：函数体 + 类型断言挂载子组件（组合组件定型手法）
function Card<T>({ data, children }: CardProps<T>) {
  return <CardCtx.Provider value={{ data }}>{children}</CardCtx.Provider>;
}
type CardComponent = <T>(props: CardProps<T>) => ReactNode;
type CardComposite = CardComponent & {
  Header: FC<CardHeaderProps>;
  Body: FC<CardBodyProps & { children: ReactNode | ((data: unknown) => ReactNode) }>;
};
export default Card as CardComposite;
// 使用：类型完整、结构约束生效
// <Card data={user}><Card.Header title={user.name} /><Card.Body>{(u) => <p>{u.email}</p>}</Card.Body></Card>
```
