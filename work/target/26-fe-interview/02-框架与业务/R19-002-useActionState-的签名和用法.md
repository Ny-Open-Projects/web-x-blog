---
title: [R19-002] useActionState 的签名和用法？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-002：useActionState 的签名和用法？
**答**：
- 签名：`const [state, formAction, isPending] = useActionState(fn, initialState)`。
- fn 接收 `(previousState, formData)` 两个参数，返回值会成为新的 state。
- 表单提交自动串行化：前一个 action 未完成时，后续提交会排队等待。
- isPending 标识 action 执行中，最适合管理表单提交结果与错误信息。

```jsx
import { useActionState } from 'react';

async function submit(prevState, formData) {
  const name = formData.get('name');
  if (!name) return { error: '姓名不能为空' };
  await saveName(name);
  return { error: null };
}

export default function NameForm() {
  const [state, formAction, isPending] = useActionState(submit, { error: null });

  return (
    <form action={formAction}>
      <input name="name" />
      <button disabled={isPending}>{isPending ? '提交中' : '提交'}</button>
      {state.error && <p role="alert">{state.error}</p>}
    </form>
  );
}
```
