---
title: [R19-003] useFormStatus 的作用和使用限制？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-003：useFormStatus 的作用和使用限制？
**答**：
- 读取最近的祖先 `<form>` 在提交时的 pending、data、method、action 状态。
- 它是 Context 读取器：必须渲染在 `<form>` 标签内部，放在外面拿到的永远是初始值。
- 典型场景是把提交按钮抽成独立组件，按钮自身感知"提交中"并禁用。
- 来自 react-dom 而不是 react，注意导入路径。

```jsx
import { useFormStatus } from 'react-dom';

function SubmitButton() {
  const { pending } = useFormStatus();
  return (
    <button type="submit" disabled={pending}>
      {pending ? '提交中...' : '提交'}
    </button>
  );
}

function ArticleForm({ action }) {
  return (
    <form action={action}>
      <input name="title" />
      {/* SubmitButton 在 form 内部才能读到 pending */}
      <SubmitButton />
    </form>
  );
}
```
