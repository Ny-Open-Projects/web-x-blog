---
title: [R19-062] 什么是 Headless 组件模式？为什么需要它？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-062：什么是 Headless 组件模式？为什么需要它？
**答**：
- Headless 模式把"行为逻辑"（状态、事件、无障碍）与"UI 渲染"彻底分离：hook 只输出行为，渲染交给调用方。
- 解决的问题：同一套交互逻辑（如 Toggle、Select）要适配多种视觉稿时，传统组件只能靠海量 CSS 变量或 API 膨胀来适配。
- 实现三件套：核心 hook（useToggle）+ 渲染代理（children as function）+ 可控受控/非受控。
- Headless UI、Radix、TanStack Table 都是这一模式；面试官常问它与 Compound 的区别——Headless 连 UI 都不给，Compound 只固定结构。

```jsx
// useToggle.ts —— Headless 核心：只提供行为，不关心 UI
import { useCallback, useState } from 'react';

export function useToggle({ defaultOpen = false, controlled, onChange } = {}) {
  const [internal, setInternal] = useState(defaultOpen);
  const isControlled = controlled !== undefined;
  const open = isControlled ? controlled : internal;

  const setOpen = useCallback((next) => {
    const value = typeof next === 'function' ? next(open) : next;
    if (!isControlled) setInternal(value);
    onChange?.(value);
  }, [open, isControlled, onChange]);

  const toggle = useCallback(() => setOpen(v => !v), [setOpen]);
  return { open, setOpen, toggle, isControlled };
}

// Disclosure：UI 完全交给调用方，行为全部来自 hook
export function Disclosure({ children }) {
  const toggle = useToggle();
  return children(toggle);
}

// 用法：想渲染成下拉、抽屉还是折叠面板，都由使用方决定
// <Disclosure>{({ open, toggle }) => open && <Drawer onClose={toggle} />}</Disclosure>
```
