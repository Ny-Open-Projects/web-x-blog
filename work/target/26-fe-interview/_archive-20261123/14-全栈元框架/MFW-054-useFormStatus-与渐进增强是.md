---
title: [MFW-054] Server Action 的渐进增强是什么，useFormStatus 解决什么问题？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-054：Server Action 的渐进增强是什么，useFormStatus 解决什么问题？
**答**：
- 渐进增强：`<form action={serverAction}>` 是原生 form 的 action 属性，JS 还没加载完时提交也能走服务端（框架内置回退），表单不依赖 hydration 就可用——这是元框架对「无 JS 可用」的回应。
- `useFormStatus` 必须放在 form **内部的子组件**里才读得到父级 form 的提交状态（Context 机制），用来做 pending 转圈、禁用按钮防重复提交。
- `useActionState` 把「上次返回值 + pending」包成一个受控状态，适合错误提示回显。
- 对比老方案：以前要在 onSubmit 里手动 setState(true) 再 fetch，现在提交状态由框架托管，且天然支持 JS 禁用场景。

```tsx
// SubmitButton.tsx —— 必须是 <form> 的子组件
'use client';
import { useFormStatus } from 'react-dom';

function SubmitButton() {
  const { pending } = useFormStatus();
  return (
    <button disabled={pending}>
      {pending ? '提交中…' : '下单'}
    </button>
  );
}
```

```tsx
// page.tsx
import { createOrder } from './actions';
import { SubmitButton } from './SubmitButton';

export default function OrderForm() {
  return (
    // JS 未加载时也能提交：浏览器原生 POST 回退
    <form action={createOrder}>
      <input name="productId" type="hidden" value="p_1001" />
      <input name="quantity" type="number" defaultValue={1} />
      <SubmitButton />
    </form>
  );
}
```
