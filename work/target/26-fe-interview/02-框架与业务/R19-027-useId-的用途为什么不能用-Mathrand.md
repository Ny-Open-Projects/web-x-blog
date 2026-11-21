---
title: [R19-027] useId 的用途？为什么不能用 Math.random 生成 id？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-027：useId 的用途？为什么不能用 Math.random 生成 id？
**答**：
- useId 生成服务端与客户端一致的稳定唯一 id，主要用于无障碍属性 htmlFor/aria 关联。
- Math.random 或自增计数器会导致 SSR hydration mismatch，两棵树的属性对不上。
- 同一组件多次渲染生成不同 id，useId 天然支持组件复用，也可加前缀区分用途。
- 适合 label-input 关联、SVG 引用等场景，不适合给列表项当 key。

```jsx
import { useId } from 'react';

function Field({ label }) {
  // SSR 与客户端生成一致的 id，且组件复用时各自唯一
  const id = useId();

  return (
    <>
      <label htmlFor={id}>{label}</label>
      <input id={id} />
    </>
  );
}

export default function Form() {
  return (
    <>
      <Field label="用户名" />
      <Field label="邮箱" />
    </>
  );
}
```
