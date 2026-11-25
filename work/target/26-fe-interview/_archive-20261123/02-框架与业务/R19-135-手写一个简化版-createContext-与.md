---
title: [R19-135] 手写一个简化版 createContext 与 useContext？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-135：手写一个简化版 createContext 与 useContext？
**答**：
- 简化思路：用一个**模块级 Provider 栈**——渲染 Provider 时把 value 压栈，`useContext` 取栈顶，出栈即还原。
- 真实 React 更进一步：value 挂在 fiber 树上沿链向上查找，并在 value 变化时**跳过中间 memo 组件**直接向下游传播。
- 局限也由此而来：一个 value 变化会让**所有消费组件**重渲染，与订阅粒度无关——这是 Context 性能问题的本质。
- 示例同时演示"defaultValue 只有在组件树中找不到 Provider 时才生效"。

```jsx
// mini-context.js —— 手写 createContext：Provider 栈实现
export function createContext(defaultValue) {
  const stack = [];                      // 模块级 Provider 栈
  const Context = {
    $$type: 'context',
    defaultValue,
    _stack: stack,
    Provider({ value, children }) {
      stack.push(value);                 // 渲染时压栈
      try {
        return typeof children === 'function' ? children() : children;
      } finally {
        stack.pop();                     // 渲染完出栈，作用域即还原
      }
    },
  };
  return Context;
}

export function useContext(Context) {
  // 栈非空取栈顶（最近的 Provider）；否则用 defaultValue
  return Context._stack.length
    ? Context._stack[Context._stack.length - 1]
    : Context.defaultValue;
}

// ---- 使用与坑位演示 ----
import { render, useState } from './mini-react';

const ThemeContext = createContext('light');

function Button() {
  const theme = useContext(ThemeContext);   // 每次主题变化都会重渲染
  return { type: 'button', props: { label: `theme is ${theme}` } };
}

function App() {
  const [theme, setTheme] = useState('light');
  return ThemeContext.Provider({
    value: theme,
    children: () => Button(),               // 主题一变 Button 必重渲染
  });
}

// 优化手法：value 下沉 —— 把"只读主题"和"切换函数"拆成两个 Context，
// 或把 value 用 useMemo 稳定引用，避免无关消费组件被波及。
```
