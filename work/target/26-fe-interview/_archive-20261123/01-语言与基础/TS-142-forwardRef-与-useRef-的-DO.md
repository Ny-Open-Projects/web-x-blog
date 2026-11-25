---
title: [TS-142] forwardRef 与 useRef 的 DOM 类型怎么标？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-142：forwardRef 与 useRef 的 DOM 类型怎么标？
**答**：
- `useRef<HTMLDivElement>(null)` 得到 `RefObject<HTMLDivElement | null>`，使用前判空，不要用 `!` 强断言。
- 自定义组件向外暴露 ref 用 `forwardRef<HTMLElement, Props>`，泛型第一参就是内部 DOM 元素类型。
- React 19 起 ref 可作为普通 prop 声明，forwardRef 逐步退场，但存量代码必须掌握。

```tsx
// 本体 DOM ref：标元素类型 + null
const boxRef = useRef<HTMLDivElement>(null);
return <div ref={boxRef}>...</div>;
// 使用时先判空
if (boxRef.current) boxRef.current.scrollIntoView();

// 值缓存 ref 与 DOM ref 区分：useRef<number>(0) 得 MutableRefObject<number>

// forwardRef：把 ref 透传给内部 input
interface FancyInputProps { label: string }
const FancyInput = forwardRef<HTMLInputElement, FancyInputProps>(
  (props, ref) => <input ref={ref} placeholder={props.label} />,
);
// 使用：<FancyInput ref={inputRef} label="搜索" />
// inputRef 类型 RefObject<HTMLInputElement | null>

// React 19：function FancyInput({ ref, label }: { ref?: Ref<HTMLInputElement>; label: string })
```

## 第三十一章 工具类型库源码级精选（TS-143 ~ TS-149）
